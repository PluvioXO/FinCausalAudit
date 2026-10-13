import json,ast
from pathlib import Path
src=Path('/mnt/data/FinCausalAudit_v3_2_Colab_Fixed_Aggregation.ipynb');nb=json.loads(src.read_text())
old='''def binary_metrics(y,prob):
    y=np.asarray(y,dtype=int);prob=np.clip(np.asarray(prob,dtype=float),1e-6,1-1e-6)
    if len(y)==0 or len(np.unique(y))<2:
        return dict(auroc=np.nan,auprc=np.nan,brier=np.nan,n=len(y),errors=int(y.sum()))
    return dict(auroc=float(roc_auc_score(y,prob)),auprc=float(average_precision_score(y,prob)),
                brier=float(brier_score_loss(y,prob)),n=len(y),errors=int(y.sum()))
'''
new='''def binary_metrics(y, prob):
    """AUROC/AUPRC must rank RAW finite scores. Clipping creates false ties."""
    y = np.asarray(y, dtype=int)
    raw = np.asarray(prob, dtype=float)
    if len(y) != len(raw) or not np.isfinite(raw).all():
        raise ValueError("Invalid model-risk scores for evaluation")
    if len(y) == 0 or len(np.unique(y)) < 2:
        return dict(auroc=np.nan, auprc=np.nan, brier=np.nan,
                    n=len(y), errors=int(y.sum()))
    return dict(auroc=float(roc_auc_score(y, raw)),
                auprc=float(average_precision_score(y, raw)),
                brier=float(brier_score_loss(y, np.clip(raw, 0., 1.))),
                n=len(y), errors=int(y.sum()))
'''
code=''.join(nb['cells'][13]['source']);assert code.count(old)==1;code=code.replace(old,new)
nb['cells'][13]['source']=code.splitlines(keepends=True)
# Repair existing cached rows before export and figures.
marker='if not RISK_PREDICTIONS.empty:\n    LETTER_BIAS='
repair='''# Repair metrics from saved model scores, including legacy cached jobs that
# produced AUROC after clipping small probabilities. No model forward passes.
RISK_PREDICTORS = [
    'risk_internal', 'risk_confidence', 'risk_metadata',
    'risk_text_output', 'risk_text_only', 'risk_output_only',
    'risk_perm_control', 'risk_rule_verifier'
]
if not RISK_PREDICTIONS.empty:
    corrected_rows = []
    for (model_id, seed, split), group in RISK_PREDICTIONS.groupby(
        ['model_id', 'seed', 'split'], sort=False
    ):
        for predictor in RISK_PREDICTORS:
            if predictor not in group.columns:
                raise ValueError(f'Missing {predictor} for {model_id} / {seed}')
            corrected_rows.append(dict(model_id=model_id, seed=int(seed),
                                       split=split, predictor=predictor,
                                       **binary_metrics(group.error, group[predictor])))
    remaining = PROBE_SUMMARY.loc[
        ~PROBE_SUMMARY.predictor.isin(RISK_PREDICTORS)
    ] if not PROBE_SUMMARY.empty else pd.DataFrame()
    PROBE_SUMMARY = pd.concat([remaining, pd.DataFrame(corrected_rows)],
                              ignore_index=True)
    # Paired-bootstrap point differences were computed on raw scores originally.
    differences = PROBE_SUMMARY[
        PROBE_SUMMARY.predictor.eq('DIFF_internal_minus_risk_text_output')
    ]
    primary = PROBE_SUMMARY.pivot_table(
        index=['model_id', 'seed', 'split'], columns='predictor', values='auroc'
    )
    for row in differences.itertuples(index=False):
        idx = (row.model_id, int(row.seed), row.split)
        if idx not in primary.index: continue
        actual = primary.loc[idx, 'risk_internal'] - primary.loc[idx, 'risk_text_output']
        if np.isfinite(actual) and np.isfinite(row.auroc):
            if abs(actual - row.auroc) > 1e-5:
                raise AssertionError(f'AUROC point-estimate mismatch for {idx}: '
                                     f'{actual} vs saved paired difference {row.auroc}')
    print(f'Metrics repaired from saved raw scores: {len(corrected_rows)} rows.')

'''
cell=''.join(nb['cells'][31]['source']);assert marker in cell;cell=cell.replace(marker,repair+marker,1)
nb['cells'][31]['source']=cell.splitlines(keepends=True)
nb['cells'][0]['source']=''.join(nb['cells'][0]['source']).replace('v3 — Cross-family','v3.3 — Cross-family').splitlines(keepends=True)
# Ensure all Python code cells parse; original cell 1 may start with shell % magics, skip those lines.
for i,c in enumerate(nb['cells']):
 if c['cell_type']!='code':continue
 code=''.join(c['source']);
 try:ast.parse(code)
 except SyntaxError as exc:
  if any(line.lstrip().startswith(('%','!')) for line in code.splitlines()):continue
  raise SyntaxError(f'Cell {i}: {exc}') from exc
out=Path('/mnt/data/FinCausalAudit_v3_3_Metric_Safe_Colab.ipynb');out.write_text(json.dumps(nb,indent=1,ensure_ascii=False)+'\n'); print(out)
