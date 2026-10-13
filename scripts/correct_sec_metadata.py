#!/usr/bin/env python3
"""Reproduce SEC *metadata-only* period-year corrections; never change prompts or predictions.

The original v4 SEC prompt's ``FISCAL YEAR`` token incorrectly differs by +2
from the SEC period-end year. This generates an audit mapping, NOT corrected
model inferences. See README. No API access required.
"""
from pathlib import Path
import pandas as pd
ROOT=Path(__file__).resolve().parents[1]
source=pd.read_csv(ROOT/'data/v4_full/sec/benchmark.csv')
source['original_prompt_year']=source['year'].astype(int)
source['corrected_period_year']=pd.to_datetime(source.period_end).dt.year
source['year_label_offset']=source.original_prompt_year-source.corrected_period_year
assert set(source.year_label_offset)=={2}
# Match the columns from v6 supporting metadata table, excluding the original user_prompt.
archived=pd.read_csv(ROOT/'data/derived/v6_sec_metadata/sec_period_labels_corrected.csv')
cols=archived.columns.tolist()
computed=source[cols].sort_values('uid').reset_index(drop=True)
expected=archived[cols].sort_values('uid').reset_index(drop=True)
pd.testing.assert_frame_equal(computed,expected,check_dtype=False)
print(f'SEC year metadata: {source.case_id.nunique()} task cases / '
      f'{source[["cik","period_end"]].drop_duplicates().shape[0]} distinct company-periods; '
      f'{source.company.nunique()} companies.')
print('Corrected audit table exactly matches archived v6 supplementary mapping.')
print('IMPORTANT: original prompt years remain incorrect; measurements were NOT re-run.')
