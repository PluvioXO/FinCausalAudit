# FinCausalAudit v2 — automatically computed findings draft

> **Preliminary and synthetic-primary results.** Verify every number and graph against the raw CSVs before submission.

Run profile: `extended`; completed model/seed jobs: **9 of 9**.
All independent synthetic benchmark cases across seeds: **1200**.
Main benchmark source authority is *synthetically assigned*, not authenticated.
On the synthetically numeric rule-based task a regex-based verifier achieves 100% task-score accuracy by construction.

## Primary: internal versus observable-signal error detection (held-out cases)
### `HuggingFaceTB/SmolLM2-1.7B-Instruct` — seed `20261012`, `test_id`
- risk_internal: AUROC 0.959 (n=480, errors=240; undefined metrics shown as `nan`).
- risk_confidence: AUROC 0.503 (n=480, errors=240; undefined metrics shown as `nan`).
- risk_metadata: AUROC 0.529 (n=480, errors=240; undefined metrics shown as `nan`).
- risk_text_output: AUROC 0.887 (n=480, errors=240; undefined metrics shown as `nan`).
- risk_perm_control: AUROC 0.542 (n=480, errors=240; undefined metrics shown as `nan`).
- risk_rule_verifier: AUROC 1.000 (n=480, errors=240; undefined metrics shown as `nan`).
- DIFF_internal_minus_risk_confidence: AUROC difference 0.456 (case-bootstrap 95% CI 0.383 to 0.521).
- DIFF_internal_minus_risk_metadata: AUROC difference 0.429 (case-bootstrap 95% CI 0.346 to 0.513).
- DIFF_internal_minus_risk_text_output: AUROC difference 0.072 (case-bootstrap 95% CI 0.053 to 0.091).
### `HuggingFaceTB/SmolLM2-1.7B-Instruct` — seed `20261012`, `test_ood`
- risk_internal: AUROC 0.761 (n=240, errors=119; undefined metrics shown as `nan`).
- risk_confidence: AUROC 0.421 (n=240, errors=119; undefined metrics shown as `nan`).
- risk_metadata: AUROC 0.616 (n=240, errors=119; undefined metrics shown as `nan`).
- risk_text_output: AUROC 0.878 (n=240, errors=119; undefined metrics shown as `nan`).
- risk_perm_control: AUROC 0.568 (n=240, errors=119; undefined metrics shown as `nan`).
- risk_rule_verifier: AUROC 1.000 (n=240, errors=119; undefined metrics shown as `nan`).
- DIFF_internal_minus_risk_confidence: AUROC difference 0.340 (case-bootstrap 95% CI 0.213 to 0.435).
- DIFF_internal_minus_risk_metadata: AUROC difference 0.144 (case-bootstrap 95% CI 0.021 to 0.267).
- DIFF_internal_minus_risk_text_output: AUROC difference -0.117 (case-bootstrap 95% CI -0.195 to -0.048).
### `HuggingFaceTB/SmolLM2-1.7B-Instruct` — seed `20261013`, `test_id`
- risk_internal: AUROC 0.956 (n=480, errors=240; undefined metrics shown as `nan`).
- risk_confidence: AUROC 0.521 (n=480, errors=240; undefined metrics shown as `nan`).
- risk_metadata: AUROC 0.483 (n=480, errors=240; undefined metrics shown as `nan`).
- risk_text_output: AUROC 0.873 (n=480, errors=240; undefined metrics shown as `nan`).
- risk_perm_control: AUROC 0.456 (n=480, errors=240; undefined metrics shown as `nan`).
- risk_rule_verifier: AUROC 1.000 (n=480, errors=240; undefined metrics shown as `nan`).
- DIFF_internal_minus_risk_confidence: AUROC difference 0.435 (case-bootstrap 95% CI 0.363 to 0.501).
- DIFF_internal_minus_risk_metadata: AUROC difference 0.473 (case-bootstrap 95% CI 0.399 to 0.541).
- DIFF_internal_minus_risk_text_output: AUROC difference 0.083 (case-bootstrap 95% CI 0.061 to 0.107).
### `HuggingFaceTB/SmolLM2-1.7B-Instruct` — seed `20261013`, `test_ood`
- risk_internal: AUROC 0.856 (n=240, errors=117; undefined metrics shown as `nan`).
- risk_confidence: AUROC 0.442 (n=240, errors=117; undefined metrics shown as `nan`).
- risk_metadata: AUROC 0.451 (n=240, errors=117; undefined metrics shown as `nan`).
- risk_text_output: AUROC 0.815 (n=240, errors=117; undefined metrics shown as `nan`).
- risk_perm_control: AUROC 0.474 (n=240, errors=117; undefined metrics shown as `nan`).
- risk_rule_verifier: AUROC 1.000 (n=240, errors=117; undefined metrics shown as `nan`).
- DIFF_internal_minus_risk_confidence: AUROC difference 0.415 (case-bootstrap 95% CI 0.295 to 0.518).
- DIFF_internal_minus_risk_metadata: AUROC difference 0.405 (case-bootstrap 95% CI 0.281 to 0.513).
- DIFF_internal_minus_risk_text_output: AUROC difference 0.041 (case-bootstrap 95% CI -0.046 to 0.126).
### `HuggingFaceTB/SmolLM2-1.7B-Instruct` — seed `20261014`, `test_id`
- risk_internal: AUROC 0.921 (n=480, errors=240; undefined metrics shown as `nan`).
- risk_confidence: AUROC 0.503 (n=480, errors=240; undefined metrics shown as `nan`).
- risk_metadata: AUROC 0.510 (n=480, errors=240; undefined metrics shown as `nan`).
- risk_text_output: AUROC 0.864 (n=480, errors=240; undefined metrics shown as `nan`).
- risk_perm_control: AUROC 0.557 (n=480, errors=240; undefined metrics shown as `nan`).
- risk_rule_verifier: AUROC 1.000 (n=480, errors=240; undefined metrics shown as `nan`).
- DIFF_internal_minus_risk_confidence: AUROC difference 0.418 (case-bootstrap 95% CI 0.341 to 0.484).
- DIFF_internal_minus_risk_metadata: AUROC difference 0.411 (case-bootstrap 95% CI 0.333 to 0.472).
- DIFF_internal_minus_risk_text_output: AUROC difference 0.057 (case-bootstrap 95% CI 0.025 to 0.088).
### `HuggingFaceTB/SmolLM2-1.7B-Instruct` — seed `20261014`, `test_ood`
- risk_internal: AUROC 0.812 (n=240, errors=119; undefined metrics shown as `nan`).
- risk_confidence: AUROC 0.412 (n=240, errors=119; undefined metrics shown as `nan`).
- risk_metadata: AUROC 0.438 (n=240, errors=119; undefined metrics shown as `nan`).
- risk_text_output: AUROC 0.843 (n=240, errors=119; undefined metrics shown as `nan`).
- risk_perm_control: AUROC 0.597 (n=240, errors=119; undefined metrics shown as `nan`).
- risk_rule_verifier: AUROC 1.000 (n=240, errors=119; undefined metrics shown as `nan`).
- DIFF_internal_minus_risk_confidence: AUROC difference 0.400 (case-bootstrap 95% CI 0.298 to 0.488).
- DIFF_internal_minus_risk_metadata: AUROC difference 0.374 (case-bootstrap 95% CI 0.270 to 0.467).
- DIFF_internal_minus_risk_text_output: AUROC difference -0.031 (case-bootstrap 95% CI -0.090 to 0.025).
### `Qwen/Qwen2.5-1.5B-Instruct` — seed `20261012`, `test_id`
- risk_internal: AUROC 0.955 (n=480, errors=122; undefined metrics shown as `nan`).
- risk_confidence: AUROC 0.699 (n=480, errors=122; undefined metrics shown as `nan`).
- risk_metadata: AUROC 0.839 (n=480, errors=122; undefined metrics shown as `nan`).
- risk_text_output: AUROC 0.814 (n=480, errors=122; undefined metrics shown as `nan`).
- risk_perm_control: AUROC 0.515 (n=480, errors=122; undefined metrics shown as `nan`).
- risk_rule_verifier: AUROC 1.000 (n=480, errors=122; undefined metrics shown as `nan`).
- DIFF_internal_minus_risk_confidence: AUROC difference 0.257 (case-bootstrap 95% CI 0.169 to 0.346).
- DIFF_internal_minus_risk_metadata: AUROC difference 0.116 (case-bootstrap 95% CI 0.058 to 0.176).
- DIFF_internal_minus_risk_text_output: AUROC difference 0.141 (case-bootstrap 95% CI 0.085 to 0.201).
### `Qwen/Qwen2.5-1.5B-Instruct` — seed `20261012`, `test_ood`
- risk_internal: AUROC 0.863 (n=240, errors=99; undefined metrics shown as `nan`).
- risk_confidence: AUROC 0.587 (n=240, errors=99; undefined metrics shown as `nan`).
- risk_metadata: AUROC 0.716 (n=240, errors=99; undefined metrics shown as `nan`).
- risk_text_output: AUROC 0.722 (n=240, errors=99; undefined metrics shown as `nan`).
- risk_perm_control: AUROC 0.578 (n=240, errors=99; undefined metrics shown as `nan`).
- risk_rule_verifier: AUROC 1.000 (n=240, errors=99; undefined metrics shown as `nan`).
- DIFF_internal_minus_risk_confidence: AUROC difference 0.276 (case-bootstrap 95% CI 0.153 to 0.399).
- DIFF_internal_minus_risk_metadata: AUROC difference 0.147 (case-bootstrap 95% CI 0.033 to 0.267).
- DIFF_internal_minus_risk_text_output: AUROC difference 0.142 (case-bootstrap 95% CI 0.028 to 0.266).
### `Qwen/Qwen2.5-1.5B-Instruct` — seed `20261013`, `test_id`
- risk_internal: AUROC 0.952 (n=480, errors=130; undefined metrics shown as `nan`).
- risk_confidence: AUROC 0.714 (n=480, errors=130; undefined metrics shown as `nan`).
- risk_metadata: AUROC 0.770 (n=480, errors=130; undefined metrics shown as `nan`).
- risk_text_output: AUROC 0.809 (n=480, errors=130; undefined metrics shown as `nan`).
- risk_perm_control: AUROC 0.515 (n=480, errors=130; undefined metrics shown as `nan`).
- risk_rule_verifier: AUROC 1.000 (n=480, errors=130; undefined metrics shown as `nan`).
- DIFF_internal_minus_risk_confidence: AUROC difference 0.238 (case-bootstrap 95% CI 0.157 to 0.317).
- DIFF_internal_minus_risk_metadata: AUROC difference 0.182 (case-bootstrap 95% CI 0.120 to 0.249).
- DIFF_internal_minus_risk_text_output: AUROC difference 0.143 (case-bootstrap 95% CI 0.086 to 0.205).
### `Qwen/Qwen2.5-1.5B-Instruct` — seed `20261013`, `test_ood`
- risk_internal: AUROC 0.854 (n=240, errors=89; undefined metrics shown as `nan`).
- risk_confidence: AUROC 0.611 (n=240, errors=89; undefined metrics shown as `nan`).
- risk_metadata: AUROC 0.714 (n=240, errors=89; undefined metrics shown as `nan`).
- risk_text_output: AUROC 0.727 (n=240, errors=89; undefined metrics shown as `nan`).
- risk_perm_control: AUROC 0.529 (n=240, errors=89; undefined metrics shown as `nan`).
- risk_rule_verifier: AUROC 1.000 (n=240, errors=89; undefined metrics shown as `nan`).
- DIFF_internal_minus_risk_confidence: AUROC difference 0.243 (case-bootstrap 95% CI 0.114 to 0.370).
- DIFF_internal_minus_risk_metadata: AUROC difference 0.139 (case-bootstrap 95% CI 0.028 to 0.259).
- DIFF_internal_minus_risk_text_output: AUROC difference 0.127 (case-bootstrap 95% CI 0.005 to 0.255).
### `Qwen/Qwen2.5-1.5B-Instruct` — seed `20261014`, `test_id`
- risk_internal: AUROC 0.950 (n=480, errors=128; undefined metrics shown as `nan`).
- risk_confidence: AUROC 0.669 (n=480, errors=128; undefined metrics shown as `nan`).
- risk_metadata: AUROC 0.802 (n=480, errors=128; undefined metrics shown as `nan`).
- risk_text_output: AUROC 0.830 (n=480, errors=128; undefined metrics shown as `nan`).
- risk_perm_control: AUROC 0.602 (n=480, errors=128; undefined metrics shown as `nan`).
- risk_rule_verifier: AUROC 1.000 (n=480, errors=128; undefined metrics shown as `nan`).
- DIFF_internal_minus_risk_confidence: AUROC difference 0.281 (case-bootstrap 95% CI 0.193 to 0.365).
- DIFF_internal_minus_risk_metadata: AUROC difference 0.148 (case-bootstrap 95% CI 0.094 to 0.205).
- DIFF_internal_minus_risk_text_output: AUROC difference 0.120 (case-bootstrap 95% CI 0.074 to 0.170).
### `Qwen/Qwen2.5-1.5B-Instruct` — seed `20261014`, `test_ood`
- risk_internal: AUROC 0.872 (n=240, errors=89; undefined metrics shown as `nan`).
- risk_confidence: AUROC 0.517 (n=240, errors=89; undefined metrics shown as `nan`).
- risk_metadata: AUROC 0.711 (n=240, errors=89; undefined metrics shown as `nan`).
- risk_text_output: AUROC 0.813 (n=240, errors=89; undefined metrics shown as `nan`).
- risk_perm_control: AUROC 0.508 (n=240, errors=89; undefined metrics shown as `nan`).
- risk_rule_verifier: AUROC 1.000 (n=240, errors=89; undefined metrics shown as `nan`).
- DIFF_internal_minus_risk_confidence: AUROC difference 0.355 (case-bootstrap 95% CI 0.205 to 0.472).
- DIFF_internal_minus_risk_metadata: AUROC difference 0.161 (case-bootstrap 95% CI 0.030 to 0.293).
- DIFF_internal_minus_risk_text_output: AUROC difference 0.059 (case-bootstrap 95% CI -0.030 to 0.154).
### `Qwen/Qwen2.5-3B-Instruct` — seed `20261012`, `test_id`
- risk_internal: AUROC 0.997 (n=480, errors=124; undefined metrics shown as `nan`).
- risk_confidence: AUROC 0.790 (n=480, errors=124; undefined metrics shown as `nan`).
- risk_metadata: AUROC 0.898 (n=480, errors=124; undefined metrics shown as `nan`).
- risk_text_output: AUROC 0.917 (n=480, errors=124; undefined metrics shown as `nan`).
- risk_perm_control: AUROC 0.536 (n=480, errors=124; undefined metrics shown as `nan`).
- risk_rule_verifier: AUROC 1.000 (n=480, errors=124; undefined metrics shown as `nan`).
- DIFF_internal_minus_risk_confidence: AUROC difference 0.205 (case-bootstrap 95% CI 0.156 to 0.259).
- DIFF_internal_minus_risk_metadata: AUROC difference 0.099 (case-bootstrap 95% CI 0.067 to 0.138).
- DIFF_internal_minus_risk_text_output: AUROC difference 0.080 (case-bootstrap 95% CI 0.052 to 0.113).
### `Qwen/Qwen2.5-3B-Instruct` — seed `20261012`, `test_ood`
- risk_internal: AUROC 0.977 (n=240, errors=78; undefined metrics shown as `nan`).
- risk_confidence: AUROC 0.777 (n=240, errors=78; undefined metrics shown as `nan`).
- risk_metadata: AUROC 0.839 (n=240, errors=78; undefined metrics shown as `nan`).
- risk_text_output: AUROC 0.871 (n=240, errors=78; undefined metrics shown as `nan`).
- risk_perm_control: AUROC 0.426 (n=240, errors=78; undefined metrics shown as `nan`).
- risk_rule_verifier: AUROC 1.000 (n=240, errors=78; undefined metrics shown as `nan`).
- DIFF_internal_minus_risk_confidence: AUROC difference 0.200 (case-bootstrap 95% CI 0.121 to 0.285).
- DIFF_internal_minus_risk_metadata: AUROC difference 0.138 (case-bootstrap 95% CI 0.081 to 0.205).
- DIFF_internal_minus_risk_text_output: AUROC difference 0.106 (case-bootstrap 95% CI 0.053 to 0.167).
### `Qwen/Qwen2.5-3B-Instruct` — seed `20261013`, `test_id`
- risk_internal: AUROC 0.987 (n=480, errors=125; undefined metrics shown as `nan`).
- risk_confidence: AUROC 0.789 (n=480, errors=125; undefined metrics shown as `nan`).
- risk_metadata: AUROC 0.892 (n=480, errors=125; undefined metrics shown as `nan`).
- risk_text_output: AUROC 0.881 (n=480, errors=125; undefined metrics shown as `nan`).
- risk_perm_control: AUROC 0.539 (n=480, errors=125; undefined metrics shown as `nan`).
- risk_rule_verifier: AUROC 1.000 (n=480, errors=125; undefined metrics shown as `nan`).
- DIFF_internal_minus_risk_confidence: AUROC difference 0.186 (case-bootstrap 95% CI 0.135 to 0.239).
- DIFF_internal_minus_risk_metadata: AUROC difference 0.095 (case-bootstrap 95% CI 0.058 to 0.135).
- DIFF_internal_minus_risk_text_output: AUROC difference 0.106 (case-bootstrap 95% CI 0.066 to 0.146).
### `Qwen/Qwen2.5-3B-Instruct` — seed `20261013`, `test_ood`
- risk_internal: AUROC 0.985 (n=240, errors=72; undefined metrics shown as `nan`).
- risk_confidence: AUROC 0.845 (n=240, errors=72; undefined metrics shown as `nan`).
- risk_metadata: AUROC 0.870 (n=240, errors=72; undefined metrics shown as `nan`).
- risk_text_output: AUROC 0.878 (n=240, errors=72; undefined metrics shown as `nan`).
- risk_perm_control: AUROC 0.585 (n=240, errors=72; undefined metrics shown as `nan`).
- risk_rule_verifier: AUROC 1.000 (n=240, errors=72; undefined metrics shown as `nan`).
- DIFF_internal_minus_risk_confidence: AUROC difference 0.140 (case-bootstrap 95% CI 0.074 to 0.226).
- DIFF_internal_minus_risk_metadata: AUROC difference 0.115 (case-bootstrap 95% CI 0.069 to 0.174).
- DIFF_internal_minus_risk_text_output: AUROC difference 0.107 (case-bootstrap 95% CI 0.053 to 0.174).
### `Qwen/Qwen2.5-3B-Instruct` — seed `20261014`, `test_id`
- risk_internal: AUROC 0.989 (n=480, errors=124; undefined metrics shown as `nan`).
- risk_confidence: AUROC 0.812 (n=480, errors=124; undefined metrics shown as `nan`).
- risk_metadata: AUROC 0.897 (n=480, errors=124; undefined metrics shown as `nan`).
- risk_text_output: AUROC 0.897 (n=480, errors=124; undefined metrics shown as `nan`).
- risk_perm_control: AUROC 0.441 (n=480, errors=124; undefined metrics shown as `nan`).
- risk_rule_verifier: AUROC 1.000 (n=480, errors=124; undefined metrics shown as `nan`).
- DIFF_internal_minus_risk_confidence: AUROC difference 0.169 (case-bootstrap 95% CI 0.123 to 0.222).
- DIFF_internal_minus_risk_metadata: AUROC difference 0.092 (case-bootstrap 95% CI 0.056 to 0.131).
- DIFF_internal_minus_risk_text_output: AUROC difference 0.092 (case-bootstrap 95% CI 0.056 to 0.129).
### `Qwen/Qwen2.5-3B-Instruct` — seed `20261014`, `test_ood`
- risk_internal: AUROC 0.964 (n=240, errors=85; undefined metrics shown as `nan`).
- risk_confidence: AUROC 0.787 (n=240, errors=85; undefined metrics shown as `nan`).
- risk_metadata: AUROC 0.778 (n=240, errors=85; undefined metrics shown as `nan`).
- risk_text_output: AUROC 0.799 (n=240, errors=85; undefined metrics shown as `nan`).
- risk_perm_control: AUROC 0.443 (n=240, errors=85; undefined metrics shown as `nan`).
- risk_rule_verifier: AUROC 1.000 (n=240, errors=85; undefined metrics shown as `nan`).
- DIFF_internal_minus_risk_confidence: AUROC difference 0.177 (case-bootstrap 95% CI 0.088 to 0.284).
- DIFF_internal_minus_risk_metadata: AUROC difference 0.186 (case-bootstrap 95% CI 0.104 to 0.281).
- DIFF_internal_minus_risk_text_output: AUROC difference 0.165 (case-bootstrap 95% CI 0.077 to 0.265).

## Source-specific and holistic causal edits

A higher correct-choice margin after an edit does not, by itself, imply that source trustworthiness is localized in the modified residual component.
- authority_token / status_high_to_low / delta_minus_identity_control: mean over reported per-model/seed/layer tests = -0.142 (descriptive; consult disaggregated CIs and FDR in causal_summary_all.csv).
- authority_token / status_high_to_low / raw_delta_margin: mean over reported per-model/seed/layer tests = -0.023 (descriptive; consult disaggregated CIs and FDR in causal_summary_all.csv).
- authority_token / status_low_to_high / delta_minus_identity_control: mean over reported per-model/seed/layer tests = +0.155 (descriptive; consult disaggregated CIs and FDR in causal_summary_all.csv).
- authority_token / status_low_to_high / raw_delta_margin: mean over reported per-model/seed/layer tests = +0.275 (descriptive; consult disaggregated CIs and FDR in causal_summary_all.csv).
- authority_token / status_self_control / raw_delta_margin: mean over reported per-model/seed/layer tests = +0.120 (descriptive; consult disaggregated CIs and FDR in causal_summary_all.csv).
- authority_token / unchanged_earlier_token / delta_minus_identity_control: mean over reported per-model/seed/layer tests = +0.000 (descriptive; consult disaggregated CIs and FDR in causal_summary_all.csv).
- authority_token / unchanged_earlier_token / raw_delta_margin: mean over reported per-model/seed/layer tests = +0.120 (descriptive; consult disaggregated CIs and FDR in causal_summary_all.csv).
- whole_final_token / different_case_clean_matched / raw_delta_margin: mean over reported per-model/seed/layer tests = +0.455 (descriptive; consult disaggregated CIs and FDR in causal_summary_all.csv).
- whole_final_token / same_case_clean / raw_delta_margin: mean over reported per-model/seed/layer tests = +0.507 (descriptive; consult disaggregated CIs and FDR in causal_summary_all.csv).
- whole_final_token / same_case_evidence_flip / raw_delta_margin: mean over reported per-model/seed/layer tests = -1.707 (descriptive; consult disaggregated CIs and FDR in causal_summary_all.csv).
- whole_final_token / self_injection / raw_delta_margin: mean over reported per-model/seed/layer tests = +0.058 (descriptive; consult disaggregated CIs and FDR in causal_summary_all.csv).

## Activation steering with held-out controls

- Qwen/Qwen2.5-1.5B-Instruct; seed 20261012; clean/learned_direction: margin effect -0.021 [-0.104, +0.068]; n=24.
- Qwen/Qwen2.5-1.5B-Instruct; seed 20261012; clean/norm_matched_random: margin effect +0.104 [-0.026, +0.235]; n=24.
- Qwen/Qwen2.5-1.5B-Instruct; seed 20261012; injection/learned_direction: margin effect +0.057 [-0.016, +0.135]; n=24.
- Qwen/Qwen2.5-1.5B-Instruct; seed 20261012; injection/norm_matched_random: margin effect +0.089 [-0.078, +0.271]; n=24.
- Qwen/Qwen2.5-1.5B-Instruct; seed 20261012; misleading/learned_direction: margin effect +0.005 [-0.078, +0.094]; n=24.
- Qwen/Qwen2.5-1.5B-Instruct; seed 20261012; misleading/norm_matched_random: margin effect +0.052 [-0.089, +0.188]; n=24.
- Qwen/Qwen2.5-1.5B-Instruct; seed 20261012; trusted_misleading/learned_direction: margin effect +0.021 [-0.052, +0.089]; n=24.
- Qwen/Qwen2.5-1.5B-Instruct; seed 20261012; trusted_misleading/norm_matched_random: margin effect +0.068 [-0.078, +0.224]; n=24.
- Qwen/Qwen2.5-1.5B-Instruct; seed 20261013; clean/learned_direction: margin effect +0.068 [-0.005, +0.141]; n=24.
- Qwen/Qwen2.5-1.5B-Instruct; seed 20261013; clean/norm_matched_random: margin effect +0.068 [-0.016, +0.156]; n=24.
- Qwen/Qwen2.5-1.5B-Instruct; seed 20261013; injection/learned_direction: margin effect +0.068 [-0.031, +0.161]; n=24.
- Qwen/Qwen2.5-1.5B-Instruct; seed 20261013; injection/norm_matched_random: margin effect +0.057 [-0.047, +0.161]; n=24.
- Qwen/Qwen2.5-1.5B-Instruct; seed 20261013; misleading/learned_direction: margin effect +0.057 [-0.010, +0.135]; n=24.
- Qwen/Qwen2.5-1.5B-Instruct; seed 20261013; misleading/norm_matched_random: margin effect +0.010 [-0.057, +0.078]; n=24.
- Qwen/Qwen2.5-1.5B-Instruct; seed 20261013; trusted_misleading/learned_direction: margin effect +0.031 [-0.042, +0.104]; n=24.
- Qwen/Qwen2.5-1.5B-Instruct; seed 20261013; trusted_misleading/norm_matched_random: margin effect -0.021 [-0.089, +0.047]; n=24.
- Qwen/Qwen2.5-1.5B-Instruct; seed 20261014; clean/learned_direction: margin effect +0.089 [+0.021, +0.167]; n=24.
- Qwen/Qwen2.5-1.5B-Instruct; seed 20261014; clean/norm_matched_random: margin effect +0.062 [-0.000, +0.141]; n=24.
- Qwen/Qwen2.5-1.5B-Instruct; seed 20261014; injection/learned_direction: margin effect +0.016 [-0.052, +0.083]; n=24.
- Qwen/Qwen2.5-1.5B-Instruct; seed 20261014; injection/norm_matched_random: margin effect -0.026 [-0.094, +0.047]; n=24.
- Qwen/Qwen2.5-1.5B-Instruct; seed 20261014; misleading/learned_direction: margin effect +0.130 [+0.036, +0.219]; n=24.
- Qwen/Qwen2.5-1.5B-Instruct; seed 20261014; misleading/norm_matched_random: margin effect +0.083 [+0.000, +0.167]; n=24.
- Qwen/Qwen2.5-1.5B-Instruct; seed 20261014; trusted_misleading/learned_direction: margin effect +0.068 [-0.016, +0.151]; n=24.
- Qwen/Qwen2.5-1.5B-Instruct; seed 20261014; trusted_misleading/norm_matched_random: margin effect +0.042 [-0.042, +0.120]; n=24.
- HuggingFaceTB/SmolLM2-1.7B-Instruct; seed 20261012; clean/learned_direction: margin effect -0.000 [-0.031, +0.026]; n=24.
- HuggingFaceTB/SmolLM2-1.7B-Instruct; seed 20261012; clean/norm_matched_random: margin effect -0.016 [-0.042, +0.010]; n=24.
- HuggingFaceTB/SmolLM2-1.7B-Instruct; seed 20261012; injection/learned_direction: margin effect +0.031 [+0.000, +0.062]; n=24.
- HuggingFaceTB/SmolLM2-1.7B-Instruct; seed 20261012; injection/norm_matched_random: margin effect -0.000 [-0.026, +0.026]; n=24.
- HuggingFaceTB/SmolLM2-1.7B-Instruct; seed 20261012; misleading/learned_direction: margin effect -0.005 [-0.042, +0.031]; n=24.
- HuggingFaceTB/SmolLM2-1.7B-Instruct; seed 20261012; misleading/norm_matched_random: margin effect +0.000 [-0.036, +0.036]; n=24.
- HuggingFaceTB/SmolLM2-1.7B-Instruct; seed 20261012; trusted_misleading/learned_direction: margin effect -0.000 [-0.026, +0.026]; n=24.
- HuggingFaceTB/SmolLM2-1.7B-Instruct; seed 20261012; trusted_misleading/norm_matched_random: margin effect -0.016 [-0.047, +0.016]; n=24.
- HuggingFaceTB/SmolLM2-1.7B-Instruct; seed 20261013; clean/learned_direction: margin effect +0.016 [-0.016, +0.047]; n=24.
- HuggingFaceTB/SmolLM2-1.7B-Instruct; seed 20261013; clean/norm_matched_random: margin effect -0.005 [-0.036, +0.026]; n=24.
- HuggingFaceTB/SmolLM2-1.7B-Instruct; seed 20261013; injection/learned_direction: margin effect +0.016 [-0.021, +0.052]; n=24.
- HuggingFaceTB/SmolLM2-1.7B-Instruct; seed 20261013; injection/norm_matched_random: margin effect +0.021 [-0.016, +0.052]; n=24.
- HuggingFaceTB/SmolLM2-1.7B-Instruct; seed 20261013; misleading/learned_direction: margin effect -0.000 [-0.031, +0.031]; n=24.
- HuggingFaceTB/SmolLM2-1.7B-Instruct; seed 20261013; misleading/norm_matched_random: margin effect +0.005 [-0.031, +0.036]; n=24.
- HuggingFaceTB/SmolLM2-1.7B-Instruct; seed 20261013; trusted_misleading/learned_direction: margin effect +0.010 [-0.016, +0.042]; n=24.
- HuggingFaceTB/SmolLM2-1.7B-Instruct; seed 20261013; trusted_misleading/norm_matched_random: margin effect -0.026 [-0.062, +0.010]; n=24.
- HuggingFaceTB/SmolLM2-1.7B-Instruct; seed 20261014; clean/learned_direction: margin effect +0.005 [-0.021, +0.031]; n=24.
- HuggingFaceTB/SmolLM2-1.7B-Instruct; seed 20261014; clean/norm_matched_random: margin effect +0.016 [-0.016, +0.047]; n=24.
- HuggingFaceTB/SmolLM2-1.7B-Instruct; seed 20261014; injection/learned_direction: margin effect +0.005 [-0.026, +0.036]; n=24.
- HuggingFaceTB/SmolLM2-1.7B-Instruct; seed 20261014; injection/norm_matched_random: margin effect -0.005 [-0.042, +0.026]; n=24.
- HuggingFaceTB/SmolLM2-1.7B-Instruct; seed 20261014; misleading/learned_direction: margin effect +0.000 [-0.031, +0.031]; n=24.
- HuggingFaceTB/SmolLM2-1.7B-Instruct; seed 20261014; misleading/norm_matched_random: margin effect -0.005 [-0.042, +0.031]; n=24.
- HuggingFaceTB/SmolLM2-1.7B-Instruct; seed 20261014; trusted_misleading/learned_direction: margin effect +0.016 [-0.016, +0.052]; n=24.
- HuggingFaceTB/SmolLM2-1.7B-Instruct; seed 20261014; trusted_misleading/norm_matched_random: margin effect -0.010 [-0.042, +0.026]; n=24.
- Qwen/Qwen2.5-3B-Instruct; seed 20261012; clean/learned_direction: margin effect +0.647 [+0.045, +1.312]; n=24.
- Qwen/Qwen2.5-3B-Instruct; seed 20261012; clean/norm_matched_random: margin effect +0.730 [+0.154, +1.377]; n=24.
- Qwen/Qwen2.5-3B-Instruct; seed 20261012; injection/learned_direction: margin effect -0.028 [-0.467, +0.374]; n=24.
- Qwen/Qwen2.5-3B-Instruct; seed 20261012; injection/norm_matched_random: margin effect +0.065 [-0.381, +0.474]; n=24.
- Qwen/Qwen2.5-3B-Instruct; seed 20261012; misleading/learned_direction: margin effect +0.466 [-0.052, +0.977]; n=24.
- Qwen/Qwen2.5-3B-Instruct; seed 20261012; misleading/norm_matched_random: margin effect +0.670 [+0.158, +1.178]; n=24.
- Qwen/Qwen2.5-3B-Instruct; seed 20261012; trusted_misleading/learned_direction: margin effect +0.477 [+0.029, +0.966]; n=24.
- Qwen/Qwen2.5-3B-Instruct; seed 20261012; trusted_misleading/norm_matched_random: margin effect +0.536 [+0.162, +0.890]; n=24.
- Qwen/Qwen2.5-3B-Instruct; seed 20261013; clean/learned_direction: margin effect +0.407 [+0.007, +0.860]; n=24.
- Qwen/Qwen2.5-3B-Instruct; seed 20261013; clean/norm_matched_random: margin effect +0.389 [-0.011, +0.858]; n=24.
- Qwen/Qwen2.5-3B-Instruct; seed 20261013; injection/learned_direction: margin effect +0.345 [-0.178, +0.897]; n=24.
- Qwen/Qwen2.5-3B-Instruct; seed 20261013; injection/norm_matched_random: margin effect +0.279 [-0.270, +0.842]; n=24.
- Qwen/Qwen2.5-3B-Instruct; seed 20261013; misleading/learned_direction: margin effect +0.743 [+0.316, +1.231]; n=24.
- Qwen/Qwen2.5-3B-Instruct; seed 20261013; misleading/norm_matched_random: margin effect +0.728 [+0.300, +1.221]; n=24.
- Qwen/Qwen2.5-3B-Instruct; seed 20261013; trusted_misleading/learned_direction: margin effect +0.631 [+0.169, +1.189]; n=24.
- Qwen/Qwen2.5-3B-Instruct; seed 20261013; trusted_misleading/norm_matched_random: margin effect +0.697 [+0.246, +1.241]; n=24.
- Qwen/Qwen2.5-3B-Instruct; seed 20261014; clean/learned_direction: margin effect +0.275 [-0.080, +0.761]; n=24.
- Qwen/Qwen2.5-3B-Instruct; seed 20261014; clean/norm_matched_random: margin effect +0.289 [-0.083, +0.778]; n=24.
- Qwen/Qwen2.5-3B-Instruct; seed 20261014; injection/learned_direction: margin effect +0.069 [-0.295, +0.478]; n=24.
- Qwen/Qwen2.5-3B-Instruct; seed 20261014; injection/norm_matched_random: margin effect +0.079 [-0.299, +0.496]; n=24.
- Qwen/Qwen2.5-3B-Instruct; seed 20261014; misleading/learned_direction: margin effect +0.633 [+0.244, +1.115]; n=24.
- Qwen/Qwen2.5-3B-Instruct; seed 20261014; misleading/norm_matched_random: margin effect +0.703 [+0.333, +1.143]; n=24.
- Qwen/Qwen2.5-3B-Instruct; seed 20261014; trusted_misleading/learned_direction: margin effect +0.627 [+0.253, +1.081]; n=24.
- Qwen/Qwen2.5-3B-Instruct; seed 20261014; trusted_misleading/norm_matched_random: margin effect +0.653 [+0.285, +1.108]; n=24.

## Leave-one-task-out robustness

- HuggingFaceTB/SmolLM2-1.7B-Instruct; seed 20261012; test_id; risk_internal: AUROC=0.769, n=480, errors=240.
- HuggingFaceTB/SmolLM2-1.7B-Instruct; seed 20261012; test_id; risk_text_output: AUROC=0.798, n=480, errors=240.
- HuggingFaceTB/SmolLM2-1.7B-Instruct; seed 20261012; test_id; risk_confidence: AUROC=0.503, n=480, errors=240.
- HuggingFaceTB/SmolLM2-1.7B-Instruct; seed 20261012; test_ood; risk_internal: AUROC=0.738, n=240, errors=119.
- HuggingFaceTB/SmolLM2-1.7B-Instruct; seed 20261012; test_ood; risk_text_output: AUROC=0.847, n=240, errors=119.
- HuggingFaceTB/SmolLM2-1.7B-Instruct; seed 20261012; test_ood; risk_confidence: AUROC=0.421, n=240, errors=119.
- HuggingFaceTB/SmolLM2-1.7B-Instruct; seed 20261013; test_id; risk_internal: AUROC=0.912, n=480, errors=240.
- HuggingFaceTB/SmolLM2-1.7B-Instruct; seed 20261013; test_id; risk_text_output: AUROC=0.761, n=480, errors=240.
- HuggingFaceTB/SmolLM2-1.7B-Instruct; seed 20261013; test_id; risk_confidence: AUROC=0.521, n=480, errors=240.
- HuggingFaceTB/SmolLM2-1.7B-Instruct; seed 20261013; test_ood; risk_internal: AUROC=0.772, n=240, errors=117.
- HuggingFaceTB/SmolLM2-1.7B-Instruct; seed 20261013; test_ood; risk_text_output: AUROC=0.761, n=240, errors=117.
- HuggingFaceTB/SmolLM2-1.7B-Instruct; seed 20261013; test_ood; risk_confidence: AUROC=0.442, n=240, errors=117.
- HuggingFaceTB/SmolLM2-1.7B-Instruct; seed 20261014; test_id; risk_internal: AUROC=0.789, n=480, errors=240.
- HuggingFaceTB/SmolLM2-1.7B-Instruct; seed 20261014; test_id; risk_text_output: AUROC=0.774, n=480, errors=240.
- HuggingFaceTB/SmolLM2-1.7B-Instruct; seed 20261014; test_id; risk_confidence: AUROC=0.503, n=480, errors=240.
- HuggingFaceTB/SmolLM2-1.7B-Instruct; seed 20261014; test_ood; risk_internal: AUROC=0.717, n=240, errors=119.
- HuggingFaceTB/SmolLM2-1.7B-Instruct; seed 20261014; test_ood; risk_text_output: AUROC=0.750, n=240, errors=119.
- HuggingFaceTB/SmolLM2-1.7B-Instruct; seed 20261014; test_ood; risk_confidence: AUROC=0.412, n=240, errors=119.
- Qwen/Qwen2.5-1.5B-Instruct; seed 20261012; test_id; risk_internal: AUROC=0.701, n=480, errors=122.
- Qwen/Qwen2.5-1.5B-Instruct; seed 20261012; test_id; risk_text_output: AUROC=0.753, n=480, errors=122.
- Qwen/Qwen2.5-1.5B-Instruct; seed 20261012; test_id; risk_confidence: AUROC=0.699, n=480, errors=122.
- Qwen/Qwen2.5-1.5B-Instruct; seed 20261012; test_ood; risk_internal: AUROC=0.647, n=240, errors=99.
- Qwen/Qwen2.5-1.5B-Instruct; seed 20261012; test_ood; risk_text_output: AUROC=0.726, n=240, errors=99.
- Qwen/Qwen2.5-1.5B-Instruct; seed 20261012; test_ood; risk_confidence: AUROC=0.587, n=240, errors=99.
- Qwen/Qwen2.5-1.5B-Instruct; seed 20261013; test_id; risk_internal: AUROC=0.763, n=480, errors=130.
- Qwen/Qwen2.5-1.5B-Instruct; seed 20261013; test_id; risk_text_output: AUROC=0.753, n=480, errors=130.
- Qwen/Qwen2.5-1.5B-Instruct; seed 20261013; test_id; risk_confidence: AUROC=0.714, n=480, errors=130.
- Qwen/Qwen2.5-1.5B-Instruct; seed 20261013; test_ood; risk_internal: AUROC=0.693, n=240, errors=89.
- Qwen/Qwen2.5-1.5B-Instruct; seed 20261013; test_ood; risk_text_output: AUROC=0.654, n=240, errors=89.
- Qwen/Qwen2.5-1.5B-Instruct; seed 20261013; test_ood; risk_confidence: AUROC=0.611, n=240, errors=89.
- Qwen/Qwen2.5-1.5B-Instruct; seed 20261014; test_id; risk_internal: AUROC=0.718, n=480, errors=128.
- Qwen/Qwen2.5-1.5B-Instruct; seed 20261014; test_id; risk_text_output: AUROC=0.718, n=480, errors=128.
- Qwen/Qwen2.5-1.5B-Instruct; seed 20261014; test_id; risk_confidence: AUROC=0.669, n=480, errors=128.
- Qwen/Qwen2.5-1.5B-Instruct; seed 20261014; test_ood; risk_internal: AUROC=0.752, n=240, errors=89.
- Qwen/Qwen2.5-1.5B-Instruct; seed 20261014; test_ood; risk_text_output: AUROC=0.720, n=240, errors=89.
- Qwen/Qwen2.5-1.5B-Instruct; seed 20261014; test_ood; risk_confidence: AUROC=0.517, n=240, errors=89.
- Qwen/Qwen2.5-3B-Instruct; seed 20261012; test_id; risk_internal: AUROC=0.914, n=480, errors=124.
- Qwen/Qwen2.5-3B-Instruct; seed 20261012; test_id; risk_text_output: AUROC=0.789, n=480, errors=124.
- Qwen/Qwen2.5-3B-Instruct; seed 20261012; test_id; risk_confidence: AUROC=0.790, n=480, errors=124.
- Qwen/Qwen2.5-3B-Instruct; seed 20261012; test_ood; risk_internal: AUROC=0.932, n=240, errors=78.
- Qwen/Qwen2.5-3B-Instruct; seed 20261012; test_ood; risk_text_output: AUROC=0.767, n=240, errors=78.
- Qwen/Qwen2.5-3B-Instruct; seed 20261012; test_ood; risk_confidence: AUROC=0.777, n=240, errors=78.
- Qwen/Qwen2.5-3B-Instruct; seed 20261013; test_id; risk_internal: AUROC=0.922, n=480, errors=125.
- Qwen/Qwen2.5-3B-Instruct; seed 20261013; test_id; risk_text_output: AUROC=0.784, n=480, errors=125.
- Qwen/Qwen2.5-3B-Instruct; seed 20261013; test_id; risk_confidence: AUROC=0.789, n=480, errors=125.
- Qwen/Qwen2.5-3B-Instruct; seed 20261013; test_ood; risk_internal: AUROC=0.906, n=240, errors=72.
- Qwen/Qwen2.5-3B-Instruct; seed 20261013; test_ood; risk_text_output: AUROC=0.833, n=240, errors=72.
- Qwen/Qwen2.5-3B-Instruct; seed 20261013; test_ood; risk_confidence: AUROC=0.845, n=240, errors=72.
- Qwen/Qwen2.5-3B-Instruct; seed 20261014; test_id; risk_internal: AUROC=0.909, n=480, errors=124.
- Qwen/Qwen2.5-3B-Instruct; seed 20261014; test_id; risk_text_output: AUROC=0.809, n=480, errors=124.
- Qwen/Qwen2.5-3B-Instruct; seed 20261014; test_id; risk_confidence: AUROC=0.812, n=480, errors=124.
- Qwen/Qwen2.5-3B-Instruct; seed 20261014; test_ood; risk_internal: AUROC=0.932, n=240, errors=85.
- Qwen/Qwen2.5-3B-Instruct; seed 20261014; test_ood; risk_text_output: AUROC=0.766, n=240, errors=85.
- Qwen/Qwen2.5-3B-Instruct; seed 20261014; test_ood; risk_confidence: AUROC=0.787, n=240, errors=85.

## SAE (exploratory)

- frequency_matched_control: mean held-out delta-correct-margin +0.023, n=48 cases (not a mechanistic validation).
- selected_feature: mean held-out delta-correct-margin +0.023, n=48 cases (not a mechanistic validation).

## Real-data stress test (optional)

SEC XBRL tests: 14 company-year examples, with verifiable source metadata. This is numeric extracted-data evaluation, NOT direct financial-document reading.

## Submission-critical limitations and checks
1. A/B forced-choice next-token measurement is not free-form evidence citation accuracy.
2. Baselines trained on prompt text must be discussed even if the internal probe wins against confidence.
3. The deterministic numeric verifier solves the synthetic target by construction; interpretability does not beat it.
4. The experiment manipulates claimed textual authority, not objective reliability of audited financial filings.
5. Compare matched donor patching, self-patches, unchanged-token controls, across-model replication, and null interventions.
6. Source-token alignment failures and SAE failures are recorded, not quietly dropped.
7. Check qualitative errors, content leakage, prompt truncation (disallowed), model revisions, ablation specificity and multiplicity.
8. Cluster bootstrap intervals condition on the synthetic data generator; they are not broad market-world guarantees.
9. Before a substantive deployment claim, test held-out real filing passages, audited provenance and independent factual annotations.
10. Acceptance is determined by workshop reviewers; no amount of code makes it obvious or guaranteed.
