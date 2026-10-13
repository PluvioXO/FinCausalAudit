#!/usr/bin/env python3
"""Recompute v3 AUROC from raw, *unclipped* risk scores (fixes score-tie issue)."""
from pathlib import Path
import pandas as pd
from sklearn.metrics import roc_auc_score, average_precision_score
ROOT=Path(__file__).resolve().parents[1]
raw=pd.read_csv(ROOT/'data/v3_full/tables/probe_risk_predictions_all.csv')
corrected=pd.read_csv(ROOT/'data/derived/v3_corrected/corrected_probe_metrics.csv')
records=[]
for (model,seed,split), g in raw[raw.split.isin(['test_id','test_ood'])].groupby(['model_id','seed','split']):
    for pred in ('risk_internal','risk_confidence','risk_metadata','risk_text_output',
                 'risk_text_only','risk_output_only','risk_perm_control','risk_rule_verifier'):
        if pred not in g.columns:continue
        ok=g[['error',pred]].dropna()
        if ok.error.nunique()<2:continue
        auc=roc_auc_score(ok.error,ok[pred])
        records.append({'model_id':model,'seed':int(seed),'split':split,'predictor':pred,'auroc':auc})
recomputed=pd.DataFrame(records)
merged=recomputed.merge(corrected[['model_id','seed','split','predictor','auroc']],
    how='left',on=['model_id','seed','split','predictor'],suffixes=('_recomputed','_archived'),validate='one_to_one')
missing=merged.auroc_archived.isna().sum()
if missing:print(f'Warning: {missing} metrics absent from archived correction (may be undefined).')
good=merged.auroc_archived.notna()
error=(merged.loc[good,'auroc_recomputed']-merged.loc[good,'auroc_archived']).abs()
print(f'Compared {good.sum()} corrected v3 ROC estimates; max absolute difference: {error.max():.3g}')
assert error.max()<1e-9
print('V3 raw-score AUROC verification passed.')
