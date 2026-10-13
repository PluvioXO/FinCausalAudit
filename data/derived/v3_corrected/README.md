# FinCausalAudit v3 — Results Audit Bundle

Based on the uploaded full-run ZIP. Contains:

- `Results_Review.md`: research narrative and limitations
- `corrected_probe_metrics.csv`: corrected per-run AUROC/AUPRC/Brier (recomputed from saved prediction scores without clipping for ranking metrics)
- `metric_consistency_audit.csv`: stored vs recalculated AUROC discrepancy
- `primary_per_seed.csv`: audit-ready per-run ID/OOD comparison
- `original_case_bootstrap_differences.csv`: original correctly un-clipped paired differences and case-bootstrap CIs
- `sec_accuracy_by_model.csv`, `semantic_tests_by_model.csv`, `letter_bias_all.csv`: subsidiary experiments
- `patch_v3_notebook.py`: a reproducible patch-build script for Colab v3.3

The notebook bug affects AUROC because clipping produces artificial ties; correcting it does not imply model inference must rerun. Causal quality checks still fail all jobs and cannot be repaired from aggregate saved CSVs.
