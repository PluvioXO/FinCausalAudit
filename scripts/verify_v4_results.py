#!/usr/bin/env python3
"""Regenerate published v4 summary statistics from archived model-score CSVs.
Run from anywhere: python scripts/verify_v4_results.py
Requires: pandas and scikit-learn. No GPU or internet access required.
"""
from pathlib import Path
import sys
import pandas as pd
from sklearn.metrics import roc_auc_score

ROOT = Path(__file__).resolve().parents[1]
TABLE = ROOT/'data/v4_full/exports/full/tables'
metrics = pd.read_csv(TABLE/'probe_metrics_all.csv')
scores = pd.read_csv(TABLE/'probe_scores_all.csv')
quality = pd.read_csv(TABLE/'job_quality_status.csv')
benchmark = pd.read_csv(ROOT/'data/v4_full/sec/benchmark.csv')

assert len(quality) == 18, f'Expected 18 jobs; found {len(quality)}'
assert quality.causal_valid.astype(str).str.lower().eq('true').all(), 'Not all causal identity checks passed'
assert scores.model_id.nunique()==6, 'Expected 6 models'
assert sorted(scores.split.unique().tolist()) == ['test_id','test_ood'], 'Unexpected scored splits'
print(f'Validated {len(quality)} model-seed jobs; 6 models; all causal identity checks pass.')

raw_summary=[]
for (model,seed,split),g in scores.groupby(['model_id','seed','split']):
    if g.error.nunique()<2:
        continue
    for predictor in ('internal_risk','text_output_risk','confidence_risk'):
        auc=roc_auc_score(g.error.to_numpy(),g[predictor].to_numpy())
        saved=metrics[(metrics.model_id==model)&(metrics.seed==seed)&
                      (metrics.split==split)&(metrics.predictor==predictor)]
        if len(saved)!=1:
            raise AssertionError(f'Missing/nonunique metric: {model} {seed} {split} {predictor}')
        diff=abs(float(saved.auroc.iloc[0])-auc)
        # Confidence scores were CSV-rounded; discrepancy is < 0.0005 in source.
        tol=0.0005 if predictor=='confidence_risk' else 1e-8
        if diff>tol:
            raise AssertionError(f'ROC mismatch for {model} {seed} {split} {predictor}: {diff}')
        raw_summary.append(dict(model_id=model,seed=int(seed),split=split,
                                predictor=predictor,auroc=auc,n=len(g),errors=int(g.error.sum())))

summary=pd.DataFrame(raw_summary)
for split in ('test_id','test_ood'):
    s=summary[summary.split.eq(split)]
    mean=s.groupby('predictor').auroc.mean()
    probe=mean['internal_risk']; text=mean['text_output_risk']
    n=s[s.predictor.eq('internal_risk')].shape[0]
    print(f'{split}: n_runs={n}; internal={probe:.6f}; text+output={text:.6f}; difference={probe-text:+.6f}')
    expected = ((0.927906,0.765324) if split=='test_id' else (0.741757,0.641541))
    assert abs(probe-expected[0])<0.00001 and abs(text-expected[1])<0.00001

# The SEC year field in the original prompts is erroneous: do not rewrite inputs/labels.
period_year=pd.to_datetime(benchmark.period_end).dt.year
assert set((benchmark.year-period_year).unique())=={2}
assert benchmark.case_id.nunique()==139
assert benchmark[['cik','period_end']].drop_duplicates().shape[0]==70
assert benchmark.company.nunique()==14
print('SEC: 139 distinct tasks, 70 issuer-period observations, 14 companies; all prompt years +2.')
print('All v4 verification checks passed.')
