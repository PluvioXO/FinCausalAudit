def concatenate_or_empty(xs):return pd.concat(xs,ignore_index=True) if xs else pd.DataFrame()
PROBE_SUMMARY=concatenate_or_empty(ALL_PROBES)
# Recover identifiers from individual model-seed folders, rather than assuming
# cached prediction rows already contain model_id. Some jobs legitimately
# emit a zero-byte CSV if the probe is UNESTIMABLE.
RISK_FILE_AUDIT = []
risk_frames = []
for manifest in ALL_RUNS:
    model_id = str(manifest["model_id"])
    seed = int(manifest["seed"])
    path = ROOT / "runs" / f"{slug(model_id)}__{seed}" / "probe_risk_predictions.csv"
    status_path = path.parent / "probe_status.json"
    probe_status = "unknown"
    if status_path.exists():
        try:
            probe_status = json.loads(status_path.read_text()).get("status", "unknown")
        except (ValueError, OSError):
            probe_status = "unreadable status"

    audit = dict(model_id=model_id, seed=seed, filename=str(path),
                 probe_status=probe_status, rows_loaded=0, file_state="missing")
    if not path.is_file():
        print(f"WARNING: risk predictions missing for {model_id}, seed {seed} (probe: {probe_status})")
        RISK_FILE_AUDIT.append(audit)
        continue

    if path.stat().st_size == 0:
        audit["file_state"] = "empty_file"
        print(f"SKIP: empty risk prediction CSV for {model_id}, seed {seed} (probe: {probe_status})")
        RISK_FILE_AUDIT.append(audit)
        continue

    try:
        frame = pd.read_csv(path)
    except pd.errors.EmptyDataError:
        audit["file_state"] = "no_columns"
        print(f"SKIP: no readable columns in {path} (probe: {probe_status})")
        RISK_FILE_AUDIT.append(audit)
        continue
    except (OSError, UnicodeError, pd.errors.ParserError) as exc:
        audit["file_state"] = "read_error"
        audit["detail"] = repr(exc)
        print(f"WARNING: cannot read {path}: {exc}")
        RISK_FILE_AUDIT.append(audit)
        continue

    if frame.empty:
        audit["file_state"] = "no_rows"
        print(f"SKIP: risk predictions have no rows for {model_id}, seed {seed} (probe: {probe_status})")
        RISK_FILE_AUDIT.append(audit)
        continue

    missing_cols = {"case_id", "variant", "split", "pred_letter"} - set(frame.columns)
    if missing_cols:
        audit["file_state"] = "missing_columns"
        audit["detail"] = str(sorted(missing_cols))
        print(f"WARNING: {path} lacks required columns: {sorted(missing_cols)}")
        RISK_FILE_AUDIT.append(audit)
        continue

    # Catch stale or mismatched files rather than silently mixing model results.
    if "model_id" in frame and not frame["model_id"].astype(str).eq(model_id).all():
        raise ValueError(f"Conflicting model ID found in {path}")
    if "seed" in frame and not pd.to_numeric(frame["seed"], errors="coerce").eq(seed).all():
        raise ValueError(f"Conflicting seed found in {path}")
    frame["model_id"] = model_id
    frame["seed"] = seed
    risk_frames.append(frame)
    audit["file_state"] = "loaded"
    audit["rows_loaded"] = int(len(frame))
    RISK_FILE_AUDIT.append(audit)

RISK_PREDICTIONS = concatenate_or_empty(risk_frames)
if not RISK_PREDICTIONS.empty:
    RISK_PREDICTIONS = RISK_PREDICTIONS.drop_duplicates(
        subset=["model_id", "seed", "case_id", "variant", "split"]
    ).reset_index(drop=True)

(ROOT / "reports").mkdir(parents=True, exist_ok=True)
pd.DataFrame(RISK_FILE_AUDIT).to_csv(
    ROOT / "reports" / "risk_prediction_file_audit.csv", index=False
)
print(f"Risk CSVs: {sum(a['file_state']=='loaded' for a in RISK_FILE_AUDIT)} loaded; "
      f"{sum(a['file_state']!='loaded' for a in RISK_FILE_AUDIT)} unavailable; "
      f"{len(RISK_PREDICTIONS)} prediction rows recovered.")
if RISK_PREDICTIONS.empty:
    print("WARNING: no model-level risk predictions available. "
          "Answer-bias analysis will be omitted; check probe_status.json and the audit CSV.")
BEHAV_RESULTS=concatenate_or_empty(ALL_BEHAV)
CAUSAL_RAW=concatenate_or_empty(ALL_CAUSAL)
CAUSAL_SUMMARY=concatenate_or_empty(ALL_CSUM)
SAE_RAW=concatenate_or_empty(ALL_SAE)
SEC_PREDICTIONS=concatenate_or_empty(ALL_SECREAL)
FREEFORM=concatenate_or_empty(ALL_FREE)
CROSS_TASK=concatenate_or_empty(ALL_CROSSTASK)
CROSS_SELECTION=concatenate_or_empty(ALL_CROSS_SELECTION)
STEERING_RAW=concatenate_or_empty(ALL_STEERING)
STEERING_SUMMARY=concatenate_or_empty(ALL_STEER_SUMMARY)
SWAP_PREDICTIONS=concatenate_or_empty(ALL_SWAP)
SWAP_METRICS=concatenate_or_empty(ALL_SWAP_METRICS)
SEMANTIC_PAIRS=concatenate_or_empty(ALL_SEMANTIC)
if not RISK_PREDICTIONS.empty:
    LETTER_BIAS=(RISK_PREDICTIONS.groupby(['model_id','seed','split'],as_index=False)
      .agg(n_predictions=('pred_letter','size'),fraction_B=('pred_letter',lambda x:float((x=='B').mean()))))
    LETTER_BIAS['near_constant_answer']=((LETTER_BIAS.fraction_B<.05) | (LETTER_BIAS.fraction_B>.95))
else: LETTER_BIAS=pd.DataFrame()
TABLES={'probe_metrics_all':PROBE_SUMMARY,'probe_risk_predictions_all':RISK_PREDICTIONS,
        'paired_behaviour_all':BEHAV_RESULTS,'causal_raw_all':CAUSAL_RAW,
        'causal_summary_all':CAUSAL_SUMMARY,'sae_ablation_all':SAE_RAW,
        'sec_realworld_all':SEC_PREDICTIONS,'freeform_all':FREEFORM,
        'cross_task_all':CROSS_TASK,'cross_task_layer_selection_all':CROSS_SELECTION,
        'steering_raw_all':STEERING_RAW,'steering_summary_all':STEERING_SUMMARY,
        'label_swap_predictions_all':SWAP_PREDICTIONS,'label_swap_metrics_all':SWAP_METRICS,
        'paired_semantic_sensitivity_all':SEMANTIC_PAIRS,
        'letter_bias_all':LETTER_BIAS}
for filename,frame in TABLES.items():
    if not frame.empty:frame.to_csv(ROOT/'tables'/f'{filename}.csv',index=False)

# Figure 1 — test-ID AUROC across models (per-seed lines; no invented confidence bands).
if not PROBE_SUMMARY.empty:
    plot=PROBE_SUMMARY[(PROBE_SUMMARY.split=='test_id')&
                       PROBE_SUMMARY.predictor.isin(('risk_internal','risk_confidence','risk_text_output','risk_rule_verifier'))]
    if not plot.empty:
        fig,ax=plt.subplots(figsize=(11,5))
        labels=['Internal probe','Confidence only','Text + outputs','Rule-based verifier']
        predictors=['risk_internal','risk_confidence','risk_text_output','risk_rule_verifier']
        models=P['model_ids'];x=np.arange(len(models));width=.19
        for j,pred_name in enumerate(predictors):
            cur=plot[plot.predictor==pred_name]
            means=[cur[cur.model_id.eq(m)].auroc.mean() for m in models]
            ax.bar(x+(j-1.5)*width,means,width,label=labels[j],alpha=.8)
            for i,m in enumerate(models):
                vals=cur[cur.model_id.eq(m)].auroc.dropna().values
                if len(vals):ax.scatter(np.full(len(vals),x[i]+(j-1.5)*width),vals,s=15,c='black',zorder=5)
        ax.set_xticks(x,[m.split('/')[-1] for m in models],rotation=10,ha='right')
        ax.set_ylim(0,1.04);ax.set_ylabel('Independent test AUROC')
        ax.set_title('Error-detection AUROC by model; dots denote benchmark seeds')
        ax.legend(loc='lower left',fontsize=8,ncol=2)
        fig.tight_layout();fig.savefig(ROOT/'figures'/'01_model_comparison_auroc.png',dpi=190);plt.show();plt.close(fig)

# Figure 2 — paired behavioural effects, case-clustered CIs.
if not BEHAV_RESULTS.empty:
    plot=BEHAV_RESULTS[(BEHAV_RESULTS.split=='test_id')&BEHAV_RESULTS.metric.eq('correct_logit_margin')&
                       BEHAV_RESULTS.variant.isin(('misleading','injection','trusted_misleading'))]
    if not plot.empty:
        fig,ax=plt.subplots(figsize=(10,5))
        key=plot.groupby(['model_id','variant'],sort=False).mean(numeric_only=True).reset_index()
        models=P['model_ids'];variants=('misleading','injection','trusted_misleading')
        x=np.arange(len(models))
        for j,v in enumerate(variants):
            vals=[key[(key.model_id==m)&(key.variant==v)].mean_delta.mean() for m in models]
            ax.bar(x+(j-1)*.25,vals,width=.24,label=v)
        ax.axhline(0,c='black',linewidth=1);ax.set_xticks(x,[m.split('/')[-1] for m in models],rotation=10)
        ax.set_ylabel('Paired change in correct-choice logit margin')
        ax.set_title('Behavioural effects on the held-out synthetic benchmark')
        ax.legend();fig.tight_layout();fig.savefig(ROOT/'figures'/'02_paired_margin_by_model.png',dpi=190);plt.show();plt.close(fig)

# Figure 3 — model-specific layerwise intervention effects (no pooling raw depth indices).
if not CAUSAL_SUMMARY.empty:
    for family in ('authority_token','whole_final_token'):
        for model_id in P['model_ids']:
            part=CAUSAL_SUMMARY[(CAUSAL_SUMMARY.patch_family==family)&CAUSAL_SUMMARY.split.eq('test_id') &
                                CAUSAL_SUMMARY.model_id.eq(model_id) &
                                CAUSAL_SUMMARY.get('metric',pd.Series('raw_delta_margin',index=CAUSAL_SUMMARY.index)).eq('raw_delta_margin')]
            if part.empty:continue
            fig,ax=plt.subplots(figsize=(8,4))
            for name,g in part.groupby('condition'):
                mean_by_layer=g.groupby('block').effect.mean().sort_index()
                ax.plot(mean_by_layer.index,mean_by_layer.values,marker='o',label=name)
            ax.axhline(0,color='black',linewidth=.9)
            ax.set_xlabel('Decoder block index')
            ax.set_ylabel('Change in correct-choice margin')
            ax.set_title(f'{family.replace("_"," ")}: {model_id.split("/")[-1]}')
            ax.legend(fontsize=7);fig.tight_layout()
            fig.savefig(ROOT/'figures'/f'03_{family}_{slug(model_id)}.png',dpi=190);plt.show();plt.close(fig)

# Figure 4 — if data was actually fetched from SEC, show exploratory stress-test accuracy.
if not SEC_PREDICTIONS.empty:
    stat=SEC_PREDICTIONS.groupby(['model_id','variant']).correct.agg(['mean','count']).reset_index()
    stat.to_csv(ROOT/'tables'/'sec_accuracy_summary.csv',index=False)
    print('Real SEC XBRL exploratory stress test (NOT a full-text filing benchmark):')
    print(stat.to_string(index=False))


# V3 Figure 5 — behaviour under option relabeling. Rates are descriptive, with model/seed lines.
if not SWAP_PREDICTIONS.empty:
    sub=SWAP_PREDICTIONS[SWAP_PREDICTIONS.split.eq('test_id')]
    if not sub.empty:
        by_model=sub.groupby(['model_id','seed']).option_flip_consistent.mean().reset_index()
        fig,ax=plt.subplots(figsize=(9,4))
        groups=list(by_model.model_id.unique())
        x=np.arange(len(groups))
        means=[by_model.loc[by_model.model_id.eq(m),'option_flip_consistent'].mean() for m in groups]
        ax.bar(x,means,width=.65)
        for j,m in enumerate(groups):
            vals=by_model[by_model.model_id.eq(m)].option_flip_consistent.values
            ax.scatter(np.full(len(vals),j),vals,s=22,c='black',zorder=5)
        ax.set_ylim(0,1);ax.set_ylabel('Fraction switching letter after A/B option swap')
        ax.set_xticks(x,[m.split('/')[-1] for m in groups],rotation=20,ha='right')
        ax.set_title('Response-label invariance (held-out cases; per-seed dots)')
        fig.tight_layout();fig.savefig(ROOT/'figures'/'05_label_swap_invariance.png',dpi=190);plt.show();plt.close(fig)
# V3 Figure 6 — evidence dependence separated from source-authority and neutral paraphrase effects.
if not SEMANTIC_PAIRS.empty:
    sub=SEMANTIC_PAIRS[SEMANTIC_PAIRS.split.eq('test_id')]
    if not sub.empty:
        cols=['evidence_prediction_flipped','authority_prediction_changed','neutral_paraphrase_changed']
        g=sub.groupby('model_id')[cols].mean();fig,ax=plt.subplots(figsize=(10,4))
        x=np.arange(len(g));w=.26
        for j,col in enumerate(cols):ax.bar(x+(j-1)*w,g[col].values,width=w,label=col.replace('_',' '))
        ax.set_ylim(0,1);ax.set_ylabel('Paired response-change fraction')
        ax.set_xticks(x,[m.split('/')[-1] for m in g.index],rotation=20,ha='right')
        ax.legend(fontsize=7);fig.tight_layout()
        fig.savefig(ROOT/'figures'/'06_evidence_vs_authority_sensitivity.png',dpi=190);plt.show();plt.close(fig)

lines=['# FinCausalAudit v3 — automatically computed findings draft','',
       '> **Preliminary and synthetic-primary results.** Verify every number and graph against the raw CSVs before submission.',
       '',f'Run profile: `{PROFILE}`; completed model/seed jobs: **{len(ALL_RUNS)} of {len(P["model_ids"])*len(P["seeds"])}**.',
       f'All independent synthetic benchmark cases across seeds: **{BENCH.case_id.nunique()}**.',
       'Main benchmark source authority is *synthetically assigned*, not authenticated.',
       'On the synthetically numeric rule-based task a regex-based verifier achieves 100% task-score accuracy by construction.',
       '', '## Primary: internal versus observable-signal error detection (held-out cases)']
if not PROBE_SUMMARY.empty:
    for (model_id,seed,split),group in PROBE_SUMMARY[PROBE_SUMMARY.split.isin(('test_id','test_ood'))].groupby(['model_id','seed','split']):
        lines.append(f'### `{model_id}` — seed `{seed}`, `{split}`')
        for r in group.itertuples(index=False):
            if str(r.predictor).startswith('DIFF_'):
                lines.append(f'- {r.predictor}: AUROC difference {r.auroc:.3f} (case-bootstrap 95% CI {r.ci_lo:.3f} to {r.ci_hi:.3f}).')
            else:
                lines.append(f'- {r.predictor}: AUROC {r.auroc:.3f} (n={r.n}, errors={r.errors}; undefined metrics shown as `nan`).')
else:lines.append('No estimable probe evaluations. Do not claim an internal error-detection advantage.')
lines+=['','## Source-specific and holistic causal edits','',
        'A higher correct-choice margin after an edit does not, by itself, imply that source trustworthiness is localized in the modified residual component.']
if not CAUSAL_SUMMARY.empty:
    for (family,condition,metric),group in CAUSAL_SUMMARY.groupby(['patch_family','condition','metric']):
        effects=group.effect.dropna()
        if len(effects):
            lines.append(f'- {family} / {condition} / {metric}: mean over reported per-model/seed/layer tests = {effects.mean():+.3f} (descriptive; consult disaggregated CIs and FDR in causal_summary_all.csv).')
else:lines.append('- No causal experiments completed.')
lines+=['','## Activation steering with held-out controls','']
if not STEERING_SUMMARY.empty:
    for r in STEERING_SUMMARY[STEERING_SUMMARY.split.eq('test_id')].itertuples(index=False):
        lines.append(f'- {r.model_id}; seed {r.seed}; {r.variant}/{r.condition}: margin effect {r.mean_delta:+.3f} [{r.ci_lo:+.3f}, {r.ci_hi:+.3f}]; n={r.n_cases}.')
else:lines.append('No measured steering results; do not claim successful steering.')
lines+=['','## Leave-one-task-out robustness','']
if not CROSS_TASK.empty:
    for (model_id,seed,split),g in CROSS_TASK.groupby(['model_id','seed','split']):
        for predictor in ('risk_internal','risk_text_output','risk_confidence'):
            m=binary_metrics(g.error,g[predictor]);lines.append(f'- {model_id}; seed {seed}; {split}; {predictor}: AUROC={m["auroc"]:.3f}, n={m["n"]}, errors={m["errors"]}.')
else: lines.append('Skipped/unestimable; no leave-one-task-out transfer claim supported.')
lines+=['','## Falsification: paired answer-letter swaps','']
if not SWAP_PREDICTIONS.empty:
    for (model_id,split),g in SWAP_PREDICTIONS.groupby(['model_id','split']):
        lines.append(f'- {model_id}/{split}: forced-choice letter flips in {g.option_flip_consistent.mean():.1%} of paired prompts; n_cases={g.case_id.nunique()}.')
    for (model_id,split),g in SWAP_METRICS.groupby(['model_id','split']):
        p=g[g.predictor.isin(('risk_internal','risk_text_output'))]
        for predictor,z in p.groupby('predictor'):
            lines.append(f'- {model_id}/{split}/{predictor}: mean AUROC {z.auroc.mean():.3f} across benchmark seeds.')
else:lines.append('Not run; no answer-swap invariance claim.')
lines+=['','## Answer-letter collapse audit','']
if not LETTER_BIAS.empty:
    for r in LETTER_BIAS[LETTER_BIAS.split.isin(('test_id','test_ood'))].itertuples(index=False):
        lines.append(f'- {r.model_id}/{r.seed}/{r.split}: predicted B fraction={r.fraction_B:.1%}, near-constant={r.near_constant_answer}; n={r.n_predictions}.')
lines+=['','## Evidence, commentary and authority paired tests','']
if not SEMANTIC_PAIRS.empty:
    for model_id,g in SEMANTIC_PAIRS[SEMANTIC_PAIRS.split=='test_id'].groupby('model_id'):
        lines.append(f'- {model_id}: evidence-flip response rate {g.evidence_prediction_flipped.mean():.1%}; authority-only response rate {g.authority_prediction_changed.mean():.1%}; neutral paraphrase response rate {g.neutral_paraphrase_changed.mean():.1%}.')
lines+=['','## Causal control validity','']
for manifest in ALL_RUNS:
    status=manifest.get('causal_status',{})
    lines.append(f'- {manifest["model_id"]}/{manifest["seed"]}: identity controls valid={status.get("identity_controls_valid","unknown")}; maximum drift={status.get("identity_max_abs_delta_margin","unknown")}.')

lines+=['','## SAE (exploratory)','']
if not SAE_RAW.empty:
    for k,g in SAE_RAW.groupby('condition'):
        lines.append(f'- {k}: mean held-out delta-correct-margin {g.delta_margin.mean():+.3f}, n={g.case_id.nunique()} cases (not a mechanistic validation).')
else: lines.append('Not run or failed; inspect failure log and job manifests.')
lines+=['','## Real-data stress test (optional)','']
if not SEC_PREDICTIONS.empty:
    lines.append(f'SEC XBRL tests: {SEC_PREDICTIONS.case_id.nunique()} company-year examples, with verifiable source metadata. This is numeric extracted-data evaluation, NOT direct financial-document reading.')
else: lines.append('Not enabled or no qualifying SEC financial data was retrieved; **do not claim real-data validation**.')
lines+=['','## Submission-critical limitations and checks',
        '1. A/B forced-choice next-token measurement is not free-form evidence citation accuracy.',
        '2. Baselines trained on prompt text must be discussed even if the internal probe wins against confidence.',
        '3. The deterministic numeric verifier solves the synthetic target by construction; interpretability does not beat it.',
        '4. The experiment manipulates claimed textual authority, not objective reliability of audited financial filings.',
        '5. Compare matched donor patching, self-patches, unchanged-token controls, across-model replication, and null interventions.',
        '6. Source-token alignment failures and SAE failures are recorded, not quietly dropped.',
        '7. Check qualitative errors, content leakage, prompt truncation (disallowed), model revisions, ablation specificity and multiplicity.',
        '8. Cluster bootstrap intervals condition on the synthetic data generator; they are not broad market-world guarantees.',
        '9. Before a substantive deployment claim, test held-out real filing passages, audited provenance and independent factual annotations.',
        '10. Acceptance is determined by workshop reviewers; no amount of code makes it obvious or guaranteed.']
(ROOT/'reports'/'results_draft.md').write_text('\n'.join(lines)+'\n')
meta=dict(utc=datetime.now(timezone.utc).isoformat(),profile=PROFILE,seeds=P['seeds'],models=P['model_ids'],
          n_per_task=P['n_per_task'],n_cases_total=int(BENCH.case_id.nunique()),
          n_prompts_total=int(len(BENCH)),n_runs_finished=len(ALL_RUNS),n_runs_requested=len(P['seeds'])*len(P['model_ids']),
          n_failures=len(FAILURES),sec_enabled=ENABLE_SEC_REALWORLD,
          source_authenticity='synthetic except SEC opt-in',dataset_ood_description='unseen prompt and commentary templates',
          main_metric='forced-choice A vs B next-token probability',
          gpu=torch.cuda.get_device_name(0),dtype=str(DTYPE),python=platform.python_version(),
          torch=torch.__version__,transformers=version('transformers'),scikit_learn=version('scikit-learn'),
          source_links=['https://huggingface.co/'+m for m in P['model_ids']] +
           ['https://www.sec.gov/search-filings/edgar-application-programming-interfaces'])
(ROOT/'reports'/'run_metadata.json').write_text(json.dumps(meta,indent=2,default=str))
print('\n'.join(lines[:16]))
print('\nResearch files:',ROOT)

