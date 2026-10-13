# FinCausalAudit v3 — full-run research audit (13 October 2026)

## Source and completion status

Source: user-uploaded `FinCausalAudit_v3_full_results_light.zip` (saved run metadata timestamp: 2026-10-13 00:55:46 UTC). **Seven checkpoints × three benchmark seeds = 21/21 completed jobs; zero job failures.** Each benchmark seed includes 400 independent synthetic scenarios, rendered as seven prompt conditions (1,200 scenarios and 8,400 unique prompt-condition pairs across seeds). Seven models evaluate these 8,400 prompts, totalling **58,800 base forward model–prompt evaluations**; intervention, steering, SEC, and other auxiliary passes are separate.

The SEC extension includes **160 distinct company-year cases for 23 companies, 2019–2025**, each evaluated under three synthetic commentary conditions. The same company-year cases are evaluated by all seven models and repeated across the benchmark-seed jobs, so repeated rows must not be counted as independent company-years. Company-years are also correlated within issuers.

## Critical metric-audit finding

The notebook's `binary_metrics` function clips probabilities into `[1e-6,1-1e-6]` **before calculating AUROC**. Because AUROC is a *ranking* statistic, this creates artificial ties for very small probe scores, lowering AUROC in some runs. The paired case-bootstrap function uses **unclipped** scores. Thus, for some v3 runs, the stored `risk_internal` AUROC and the stored `DIFF_internal_minus_risk_text_output` disagree.

For OLMo2 seed `20261024`, unseen-template AUROC in the exported metric table is **0.592** while independently recomputing from saved predictions yields **0.825**. This is attributable to clipping: 316 of 360 scores are below 1e-6. Recalculating from the unmodified prediction scores resolves the arithmetic mismatch. We found 15 predictor/split combinations with AUROC discrepancy > 0.001, including smaller differences in other models. The companion `corrected_probe_metrics.csv` and `metric_consistency_audit.csv` were generated solely from saved predictions, without rerunning models. Use the corrected AUROC values in the paper, keep Brier-score clipping separate, and fix the notebook before further runs. Paired bootstrap difference rows already use un-clipped scores, though source-code validation and independent reproduction remain necessary.

## Primary diagnostic results (recomputed from saved predictions)

AUROC means across the three synthetic benchmark seeds for each model, except the Phi ID row, which has only **two estimable seeds** because one test split has no errors. A bold difference means an observed improvement, *not* a population-significance claim. Qwen3 is not represented because its synthetic run has **zero errors** and error-detection AUROC is undefined.

| Model | ID internal / text+output / Δ | Unseen-template internal / text+output / Δ |
|---|---|---|
| Qwen2.5-1.5B | 0.954 / 0.792 / **+0.162** | 0.871 / 0.754 / **+0.117** |
| Qwen2.5-3B | 0.992 / 0.907 / **+0.085** | 0.969 / 0.828 / **+0.141** |
| Granite 3.3-2B | 0.989 / 0.910 / **+0.079** | 0.945 / 0.764 / **+0.181** |
| Phi-4-mini | 1.000 / 0.995 / **+0.005** | 0.940 / 0.958 / **−0.017** |
| OLMo-2-1B | 0.879 / 0.795 / **+0.084** | 0.779 / 0.764 / **+0.015** |
| SmolLM2-1.7B | 0.937 / 0.833 / **+0.104** | 0.843 / 0.847 / **−0.005** |

Unweighted run-level means across the **17 estimable ID evaluations** are **0.956 AUROC (internal) vs 0.865 (text+output), Δ +0.091**. Across **18 OOD evaluations**, means are **0.891 vs 0.819, Δ +0.072**. Internal scores exceed text+output in **17/17 estimable ID evaluations and 14/18 OOD evaluations**. These represent dataset-seed replications of fixed checkpoints, not independent architecture samples; the result should not be sold as broadly generalisable to all financial models.

The deterministic rule-based verifier detects errors with AUROC 1.000 by construction on the synthetic benchmark. The paper studies whether model internals provide *additional signals relative to practical learned text/output baselines*, not superiority to an oracle supplied the same explicit rubric.

## Behavioral competency and shortcut controls

- Qwen3-4B: 100% accuracy on all 8,400 synthetic prompts. Thus it *cannot* support an error-detection probe and is not a negative probe result. Its evidence-flip response rate in the paired tests is 100%, with no changes to authority-only tags, misleading commentary, or neutral paraphrases on the controlled benchmark.
- Phi-4-mini: 99.2% ID and 94.6% OOD accuracy; answer relabeling switches its letter in 100% of ID and 93.1% of OOD swap tests. Its high output baseline leaves little room for useful incremental internal diagnosis.
- Granite 3.3-2B: 80.8% ID and 70.4% OOD accuracy. It has strong incremental OOD diagnostic performance and responds to evidence flips in 85.4% of held-out paired tests.
- Qwen2.5-3B and 1.5B: moderate rule-task accuracies, strong internal error diagnosis, and 87.9%/80.6% answer-relabeling compliance in held-out ID swap tests, respectively.
- SmolLM2-1.7B: chooses B in approximately 99.9% of ID prompts and changes its answer letter in 0% of ID swap pairs. Its high error-probe AUROC is therefore heavily confounded by answer-label shortcuts.
- OLMo-2-1B: chooses B only 6.0% of the time on ID prompts and swaps its answer in only 17.7% of ID swap pairs. This also challenges mechanistic interpretations of its probe performance.

These data show that *financial correctness*, *error decodability*, and *causal interpretation* should be treated as separate research endpoints.

## Causal validity and SAE

The causal quality gate reports `identity_controls_all_valid: false`. Checking every job's `causal_status.json` reveals that **0/21** jobs passed the pre-specified identity tolerance of 0.10 change in correct-answer logit margin. Some jobs skipped causal edits after preflight; five still produced exploratory patching data, but each had an invalid identity control. Significant-looking effect statistics in `causal_summary_all.csv` **must not be cited as evidence of a validated source-trust circuit**. Resolve the identity-invariance issue at the model/hook/precision level and rerun causal experiments only after a green preflight.

The SAE result is limited to OLMo-2-1B, one seed and 32 cases; the selected feature and matched control have identical mean effects within saved precision. No source-trust circuit is established by the SAE data.

## SEC XBRL stress test

Seven model evaluations of 160 authentic-number company-year cases under three conditions (clean, misleading, injection), with synthetic prompts and decision rules. Accuracy below is descriptive per distinct company-year condition; correlations by issuer and year limit broad confidence claims.

| Model | Clean | Misleading | Injection |
|---|---:|---:|---:|
| Qwen3-4B | 100.0% | 100.0% | 100.0% |
| Phi-4-mini | 100.0% | 100.0% | 100.0% |
| Granite 3.3-2B | 97.5% | 95.0% | 98.8% |
| Qwen2.5-3B | 76.9% | 76.2% | 60.6% |
| Qwen2.5-1.5B | 68.1% | 64.4% | 62.5% |
| SmolLM2-1.7B | 57.5% | 51.2% | 35.6% |
| OLMo-2-1B | 41.2% | 31.2% | 30.0% |

The SEC figures are *authentic numerical inputs*, but the model does not read full 10-K prose and the commentary is not a real third-party source. The task reduces genuine data to a synthetic explicit decision rubric. This is a useful external-numeric-value stress test, not real-world financial-advice validity.

## Recommended next experiments

1. **Fix the AUROC clipping bug** and regenerate summary tables from the raw predictions (no new inference needed). Provide a simple automated consistency assertion: observed Δ must equal internal AUROC minus baseline AUROC.
2. **Fix self-patching fidelity** (potentially hooks, bfloat16 precision, read/write location or dropout and model implementations). Reject or label invalid all interventions until an exact self-patch test preserves logits within a validated tolerance.
3. **Run answer-label swapping for Qwen3**, including direct model predictions without an error probe; the current swap stage is skipped when probe fitting is unestimable. Also design harder reasoning tasks producing actual errors in the capable models; avoid 100%-accuracy ceiling effects.
4. **Remove shortcut-driven models from the primary meta-analysis**, or label them as explicit negative controls. Keep all model-level results visible rather than selecting favourable checkpoints.
5. **Strengthen real-data external validity** using held-out issuer clusters, actual SEC filing passages and independently assessed evidence attribution rather than only computed numeric rubric labels.
6. Use a calibrated observable baseline that includes direct rule verification and test on tasks where a deterministic parser cannot trivially compute ground truth, without introducing uncertain investment outcome labels.

## Paper-ready scope

Suggested revised framing: **'When Are Internal States Useful for Auditing Financial Language Models? A Multi-Model Study of Diagnostics, Label Shortcuts, and Failed Causal Controls.'** The most honest contribution is a controlled multi-model diagnostic/shortcut study, coupled with an unusually transparent stress-test showing why diagnostic AUROC is not mechanistic explanation.

Do not claim a new causal circuit, a deployable risk score, 21 statistically independent model replications, or improvement over direct rule checking.
