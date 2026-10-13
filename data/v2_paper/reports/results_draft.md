# FinCausalAudit v2 — automatically computed findings draft

> **Preliminary and synthetic-primary results.** Verify every number and graph against the raw CSVs before submission.

Run profile: `paper`; completed model/seed jobs: **6 of 6**.
All independent synthetic benchmark cases across seeds: **400**.
Main benchmark source authority is *synthetically assigned*, not authenticated.
On the synthetically numeric rule-based task a regex-based verifier achieves 100% task-score accuracy by construction.

## Primary: internal versus observable-signal error detection (held-out cases)
### `HuggingFaceTB/SmolLM2-1.7B-Instruct` — seed `20261012`, `test_id`
- risk_internal: AUROC 0.901 (n=240, errors=120; undefined metrics shown as `nan`).
- risk_confidence: AUROC 0.526 (n=240, errors=120; undefined metrics shown as `nan`).
- risk_metadata: AUROC 0.547 (n=240, errors=120; undefined metrics shown as `nan`).
- risk_text_output: AUROC 0.845 (n=240, errors=120; undefined metrics shown as `nan`).
- risk_perm_control: AUROC 0.380 (n=240, errors=120; undefined metrics shown as `nan`).
- risk_rule_verifier: AUROC 1.000 (n=240, errors=120; undefined metrics shown as `nan`).
- DIFF_internal_minus_risk_confidence: AUROC difference 0.375 (case-bootstrap 95% CI 0.265 to 0.481).
- DIFF_internal_minus_risk_metadata: AUROC difference 0.354 (case-bootstrap 95% CI 0.231 to 0.476).
- DIFF_internal_minus_risk_text_output: AUROC difference 0.056 (case-bootstrap 95% CI -0.005 to 0.111).
### `HuggingFaceTB/SmolLM2-1.7B-Instruct` — seed `20261012`, `test_ood`
- risk_internal: AUROC 0.830 (n=120, errors=61; undefined metrics shown as `nan`).
- risk_confidence: AUROC 0.493 (n=120, errors=61; undefined metrics shown as `nan`).
- risk_metadata: AUROC 0.486 (n=120, errors=61; undefined metrics shown as `nan`).
- risk_text_output: AUROC 0.862 (n=120, errors=61; undefined metrics shown as `nan`).
- risk_perm_control: AUROC 0.446 (n=120, errors=61; undefined metrics shown as `nan`).
- risk_rule_verifier: AUROC 1.000 (n=120, errors=61; undefined metrics shown as `nan`).
- DIFF_internal_minus_risk_confidence: AUROC difference 0.336 (case-bootstrap 95% CI 0.195 to 0.452).
- DIFF_internal_minus_risk_metadata: AUROC difference 0.343 (case-bootstrap 95% CI 0.189 to 0.496).
- DIFF_internal_minus_risk_text_output: AUROC difference -0.032 (case-bootstrap 95% CI -0.082 to 0.018).
### `HuggingFaceTB/SmolLM2-1.7B-Instruct` — seed `20261013`, `test_id`
- risk_internal: AUROC 0.874 (n=240, errors=120; undefined metrics shown as `nan`).
- risk_confidence: AUROC 0.466 (n=240, errors=120; undefined metrics shown as `nan`).
- risk_metadata: AUROC 0.481 (n=240, errors=120; undefined metrics shown as `nan`).
- risk_text_output: AUROC 0.794 (n=240, errors=120; undefined metrics shown as `nan`).
- risk_perm_control: AUROC 0.449 (n=240, errors=120; undefined metrics shown as `nan`).
- risk_rule_verifier: AUROC 1.000 (n=240, errors=120; undefined metrics shown as `nan`).
- DIFF_internal_minus_risk_confidence: AUROC difference 0.408 (case-bootstrap 95% CI 0.317 to 0.491).
- DIFF_internal_minus_risk_metadata: AUROC difference 0.393 (case-bootstrap 95% CI 0.299 to 0.482).
- DIFF_internal_minus_risk_text_output: AUROC difference 0.080 (case-bootstrap 95% CI 0.045 to 0.119).
### `HuggingFaceTB/SmolLM2-1.7B-Instruct` — seed `20261013`, `test_ood`
- risk_internal: AUROC 0.824 (n=120, errors=59; undefined metrics shown as `nan`).
- risk_confidence: AUROC 0.430 (n=120, errors=59; undefined metrics shown as `nan`).
- risk_metadata: AUROC 0.445 (n=120, errors=59; undefined metrics shown as `nan`).
- risk_text_output: AUROC 0.788 (n=120, errors=59; undefined metrics shown as `nan`).
- risk_perm_control: AUROC 0.407 (n=120, errors=59; undefined metrics shown as `nan`).
- risk_rule_verifier: AUROC 1.000 (n=120, errors=59; undefined metrics shown as `nan`).
- DIFF_internal_minus_risk_confidence: AUROC difference 0.394 (case-bootstrap 95% CI 0.250 to 0.501).
- DIFF_internal_minus_risk_metadata: AUROC difference 0.380 (case-bootstrap 95% CI 0.238 to 0.488).
- DIFF_internal_minus_risk_text_output: AUROC difference 0.037 (case-bootstrap 95% CI -0.067 to 0.132).
### `Qwen/Qwen2.5-1.5B-Instruct` — seed `20261012`, `test_id`
- risk_internal: AUROC 0.902 (n=240, errors=69; undefined metrics shown as `nan`).
- risk_confidence: AUROC 0.698 (n=240, errors=69; undefined metrics shown as `nan`).
- risk_metadata: AUROC 0.745 (n=240, errors=69; undefined metrics shown as `nan`).
- risk_text_output: AUROC 0.773 (n=240, errors=69; undefined metrics shown as `nan`).
- risk_perm_control: AUROC 0.500 (n=240, errors=69; undefined metrics shown as `nan`).
- risk_rule_verifier: AUROC 1.000 (n=240, errors=69; undefined metrics shown as `nan`).
- DIFF_internal_minus_risk_confidence: AUROC difference 0.204 (case-bootstrap 95% CI 0.090 to 0.331).
- DIFF_internal_minus_risk_metadata: AUROC difference 0.157 (case-bootstrap 95% CI 0.057 to 0.258).
- DIFF_internal_minus_risk_text_output: AUROC difference 0.129 (case-bootstrap 95% CI 0.042 to 0.230).
### `Qwen/Qwen2.5-1.5B-Instruct` — seed `20261012`, `test_ood`
- risk_internal: AUROC 0.875 (n=120, errors=48; undefined metrics shown as `nan`).
- risk_confidence: AUROC 0.608 (n=120, errors=48; undefined metrics shown as `nan`).
- risk_metadata: AUROC 0.811 (n=120, errors=48; undefined metrics shown as `nan`).
- risk_text_output: AUROC 0.764 (n=120, errors=48; undefined metrics shown as `nan`).
- risk_perm_control: AUROC 0.519 (n=120, errors=48; undefined metrics shown as `nan`).
- risk_rule_verifier: AUROC 1.000 (n=120, errors=48; undefined metrics shown as `nan`).
- DIFF_internal_minus_risk_confidence: AUROC difference 0.267 (case-bootstrap 95% CI 0.119 to 0.420).
- DIFF_internal_minus_risk_metadata: AUROC difference 0.064 (case-bootstrap 95% CI -0.037 to 0.177).
- DIFF_internal_minus_risk_text_output: AUROC difference 0.111 (case-bootstrap 95% CI 0.004 to 0.235).
### `Qwen/Qwen2.5-1.5B-Instruct` — seed `20261013`, `test_id`
- risk_internal: AUROC 0.953 (n=240, errors=62; undefined metrics shown as `nan`).
- risk_confidence: AUROC 0.587 (n=240, errors=62; undefined metrics shown as `nan`).
- risk_metadata: AUROC 0.732 (n=240, errors=62; undefined metrics shown as `nan`).
- risk_text_output: AUROC 0.727 (n=240, errors=62; undefined metrics shown as `nan`).
- risk_perm_control: AUROC 0.591 (n=240, errors=62; undefined metrics shown as `nan`).
- risk_rule_verifier: AUROC 1.000 (n=240, errors=62; undefined metrics shown as `nan`).
- DIFF_internal_minus_risk_confidence: AUROC difference 0.366 (case-bootstrap 95% CI 0.243 to 0.484).
- DIFF_internal_minus_risk_metadata: AUROC difference 0.221 (case-bootstrap 95% CI 0.134 to 0.304).
- DIFF_internal_minus_risk_text_output: AUROC difference 0.226 (case-bootstrap 95% CI 0.147 to 0.307).
### `Qwen/Qwen2.5-1.5B-Instruct` — seed `20261013`, `test_ood`
- risk_internal: AUROC 0.810 (n=120, errors=46; undefined metrics shown as `nan`).
- risk_confidence: AUROC 0.546 (n=120, errors=46; undefined metrics shown as `nan`).
- risk_metadata: AUROC 0.630 (n=120, errors=46; undefined metrics shown as `nan`).
- risk_text_output: AUROC 0.639 (n=120, errors=46; undefined metrics shown as `nan`).
- risk_perm_control: AUROC 0.618 (n=120, errors=46; undefined metrics shown as `nan`).
- risk_rule_verifier: AUROC 1.000 (n=120, errors=46; undefined metrics shown as `nan`).
- DIFF_internal_minus_risk_confidence: AUROC difference 0.275 (case-bootstrap 95% CI 0.104 to 0.426).
- DIFF_internal_minus_risk_metadata: AUROC difference 0.191 (case-bootstrap 95% CI 0.045 to 0.333).
- DIFF_internal_minus_risk_text_output: AUROC difference 0.183 (case-bootstrap 95% CI 0.045 to 0.318).
### `Qwen/Qwen2.5-3B-Instruct` — seed `20261012`, `test_id`
- risk_internal: AUROC 0.989 (n=240, errors=65; undefined metrics shown as `nan`).
- risk_confidence: AUROC 0.803 (n=240, errors=65; undefined metrics shown as `nan`).
- risk_metadata: AUROC 0.878 (n=240, errors=65; undefined metrics shown as `nan`).
- risk_text_output: AUROC 0.858 (n=240, errors=65; undefined metrics shown as `nan`).
- risk_perm_control: AUROC 0.550 (n=240, errors=65; undefined metrics shown as `nan`).
- risk_rule_verifier: AUROC 1.000 (n=240, errors=65; undefined metrics shown as `nan`).
- DIFF_internal_minus_risk_confidence: AUROC difference 0.172 (case-bootstrap 95% CI 0.110 to 0.236).
- DIFF_internal_minus_risk_metadata: AUROC difference 0.111 (case-bootstrap 95% CI 0.041 to 0.205).
- DIFF_internal_minus_risk_text_output: AUROC difference 0.131 (case-bootstrap 95% CI 0.056 to 0.237).
### `Qwen/Qwen2.5-3B-Instruct` — seed `20261012`, `test_ood`
- risk_internal: AUROC 0.970 (n=120, errors=45; undefined metrics shown as `nan`).
- risk_confidence: AUROC 0.815 (n=120, errors=45; undefined metrics shown as `nan`).
- risk_metadata: AUROC 0.802 (n=120, errors=45; undefined metrics shown as `nan`).
- risk_text_output: AUROC 0.804 (n=120, errors=45; undefined metrics shown as `nan`).
- risk_perm_control: AUROC 0.566 (n=120, errors=45; undefined metrics shown as `nan`).
- risk_rule_verifier: AUROC 1.000 (n=120, errors=45; undefined metrics shown as `nan`).
- DIFF_internal_minus_risk_confidence: AUROC difference 0.155 (case-bootstrap 95% CI 0.055 to 0.280).
- DIFF_internal_minus_risk_metadata: AUROC difference 0.168 (case-bootstrap 95% CI 0.053 to 0.317).
- DIFF_internal_minus_risk_text_output: AUROC difference 0.166 (case-bootstrap 95% CI 0.047 to 0.319).
### `Qwen/Qwen2.5-3B-Instruct` — seed `20261013`, `test_id`
- risk_internal: AUROC 0.990 (n=240, errors=60; undefined metrics shown as `nan`).
- risk_confidence: AUROC 0.752 (n=240, errors=60; undefined metrics shown as `nan`).
- risk_metadata: AUROC 0.824 (n=240, errors=60; undefined metrics shown as `nan`).
- risk_text_output: AUROC 0.833 (n=240, errors=60; undefined metrics shown as `nan`).
- risk_perm_control: AUROC 0.500 (n=240, errors=60; undefined metrics shown as `nan`).
- risk_rule_verifier: AUROC 1.000 (n=240, errors=60; undefined metrics shown as `nan`).
- DIFF_internal_minus_risk_confidence: AUROC difference 0.228 (case-bootstrap 95% CI 0.152 to 0.314).
- DIFF_internal_minus_risk_metadata: AUROC difference 0.166 (case-bootstrap 95% CI 0.103 to 0.243).
- DIFF_internal_minus_risk_text_output: AUROC difference 0.158 (case-bootstrap 95% CI 0.097 to 0.236).
### `Qwen/Qwen2.5-3B-Instruct` — seed `20261013`, `test_ood`
- risk_internal: AUROC 0.928 (n=120, errors=33; undefined metrics shown as `nan`).
- risk_confidence: AUROC 0.793 (n=120, errors=33; undefined metrics shown as `nan`).
- risk_metadata: AUROC 0.836 (n=120, errors=33; undefined metrics shown as `nan`).
- risk_text_output: AUROC 0.829 (n=120, errors=33; undefined metrics shown as `nan`).
- risk_perm_control: AUROC 0.416 (n=120, errors=33; undefined metrics shown as `nan`).
- risk_rule_verifier: AUROC 1.000 (n=120, errors=33; undefined metrics shown as `nan`).
- DIFF_internal_minus_risk_confidence: AUROC difference 0.135 (case-bootstrap 95% CI 0.024 to 0.245).
- DIFF_internal_minus_risk_metadata: AUROC difference 0.092 (case-bootstrap 95% CI -0.004 to 0.182).
- DIFF_internal_minus_risk_text_output: AUROC difference 0.099 (case-bootstrap 95% CI -0.005 to 0.214).

## Source-specific and holistic causal edits

A higher correct-choice margin after an edit does not, by itself, imply that source trustworthiness is localized in the modified residual component.
- authority_token / status_high_to_low / delta_minus_identity_control: mean over reported per-model/seed/layer tests = -0.128 (descriptive; consult disaggregated CIs and FDR in causal_summary_all.csv).
- authority_token / status_high_to_low / raw_delta_margin: mean over reported per-model/seed/layer tests = +0.004 (descriptive; consult disaggregated CIs and FDR in causal_summary_all.csv).
- authority_token / status_low_to_high / delta_minus_identity_control: mean over reported per-model/seed/layer tests = +0.162 (descriptive; consult disaggregated CIs and FDR in causal_summary_all.csv).
- authority_token / status_low_to_high / raw_delta_margin: mean over reported per-model/seed/layer tests = +0.294 (descriptive; consult disaggregated CIs and FDR in causal_summary_all.csv).
- authority_token / status_self_control / raw_delta_margin: mean over reported per-model/seed/layer tests = +0.132 (descriptive; consult disaggregated CIs and FDR in causal_summary_all.csv).
- authority_token / unchanged_earlier_token / delta_minus_identity_control: mean over reported per-model/seed/layer tests = +0.000 (descriptive; consult disaggregated CIs and FDR in causal_summary_all.csv).
- authority_token / unchanged_earlier_token / raw_delta_margin: mean over reported per-model/seed/layer tests = +0.132 (descriptive; consult disaggregated CIs and FDR in causal_summary_all.csv).
- whole_final_token / different_case_clean_matched / raw_delta_margin: mean over reported per-model/seed/layer tests = +0.076 (descriptive; consult disaggregated CIs and FDR in causal_summary_all.csv).
- whole_final_token / same_case_clean / raw_delta_margin: mean over reported per-model/seed/layer tests = +0.216 (descriptive; consult disaggregated CIs and FDR in causal_summary_all.csv).
- whole_final_token / same_case_evidence_flip / raw_delta_margin: mean over reported per-model/seed/layer tests = -1.020 (descriptive; consult disaggregated CIs and FDR in causal_summary_all.csv).
- whole_final_token / self_injection / raw_delta_margin: mean over reported per-model/seed/layer tests = +0.080 (descriptive; consult disaggregated CIs and FDR in causal_summary_all.csv).

## Activation steering with held-out controls

- Qwen/Qwen2.5-1.5B-Instruct; seed 20261012; clean/learned_direction: margin effect +0.062 [-0.038, +0.162]; n=10.
- Qwen/Qwen2.5-1.5B-Instruct; seed 20261012; clean/norm_matched_random: margin effect -0.100 [-0.187, -0.012]; n=10.
- Qwen/Qwen2.5-1.5B-Instruct; seed 20261012; injection/learned_direction: margin effect +0.075 [-0.050, +0.187]; n=10.
- Qwen/Qwen2.5-1.5B-Instruct; seed 20261012; injection/norm_matched_random: margin effect -0.025 [-0.225, +0.162]; n=10.
- Qwen/Qwen2.5-1.5B-Instruct; seed 20261012; misleading/learned_direction: margin effect +0.225 [+0.137, +0.300]; n=10.
- Qwen/Qwen2.5-1.5B-Instruct; seed 20261012; misleading/norm_matched_random: margin effect +0.025 [-0.062, +0.112]; n=10.
- Qwen/Qwen2.5-1.5B-Instruct; seed 20261012; trusted_misleading/learned_direction: margin effect +0.050 [-0.050, +0.150]; n=10.
- Qwen/Qwen2.5-1.5B-Instruct; seed 20261012; trusted_misleading/norm_matched_random: margin effect -0.088 [-0.212, +0.013]; n=10.
- Qwen/Qwen2.5-1.5B-Instruct; seed 20261013; clean/learned_direction: margin effect +0.038 [-0.038, +0.113]; n=10.
- Qwen/Qwen2.5-1.5B-Instruct; seed 20261013; clean/norm_matched_random: margin effect +0.013 [-0.100, +0.113]; n=10.
- Qwen/Qwen2.5-1.5B-Instruct; seed 20261013; injection/learned_direction: margin effect +0.050 [-0.075, +0.175]; n=10.
- Qwen/Qwen2.5-1.5B-Instruct; seed 20261013; injection/norm_matched_random: margin effect -0.062 [-0.175, +0.063]; n=10.
- Qwen/Qwen2.5-1.5B-Instruct; seed 20261013; misleading/learned_direction: margin effect +0.038 [-0.025, +0.113]; n=10.
- Qwen/Qwen2.5-1.5B-Instruct; seed 20261013; misleading/norm_matched_random: margin effect -0.025 [-0.100, +0.038]; n=10.
- Qwen/Qwen2.5-1.5B-Instruct; seed 20261013; trusted_misleading/learned_direction: margin effect +0.050 [-0.075, +0.163]; n=10.
- Qwen/Qwen2.5-1.5B-Instruct; seed 20261013; trusted_misleading/norm_matched_random: margin effect +0.075 [-0.075, +0.200]; n=10.
- HuggingFaceTB/SmolLM2-1.7B-Instruct; seed 20261012; clean/learned_direction: margin effect -0.000 [-0.062, +0.062]; n=10.
- HuggingFaceTB/SmolLM2-1.7B-Instruct; seed 20261012; clean/norm_matched_random: margin effect -0.025 [-0.075, +0.025]; n=10.
- HuggingFaceTB/SmolLM2-1.7B-Instruct; seed 20261012; injection/learned_direction: margin effect +0.000 [-0.037, +0.037]; n=10.
- HuggingFaceTB/SmolLM2-1.7B-Instruct; seed 20261012; injection/norm_matched_random: margin effect -0.012 [-0.037, +0.000]; n=10.
- HuggingFaceTB/SmolLM2-1.7B-Instruct; seed 20261012; misleading/learned_direction: margin effect -0.037 [-0.075, -0.000]; n=10.
- HuggingFaceTB/SmolLM2-1.7B-Instruct; seed 20261012; misleading/norm_matched_random: margin effect -0.000 [-0.050, +0.050]; n=10.
- HuggingFaceTB/SmolLM2-1.7B-Instruct; seed 20261012; trusted_misleading/learned_direction: margin effect +0.037 [+0.000, +0.075]; n=10.
- HuggingFaceTB/SmolLM2-1.7B-Instruct; seed 20261012; trusted_misleading/norm_matched_random: margin effect +0.025 [-0.025, +0.075]; n=10.
- HuggingFaceTB/SmolLM2-1.7B-Instruct; seed 20261013; clean/learned_direction: margin effect +0.025 [+0.000, +0.062]; n=10.
- HuggingFaceTB/SmolLM2-1.7B-Instruct; seed 20261013; clean/norm_matched_random: margin effect +0.025 [+0.000, +0.062]; n=10.
- HuggingFaceTB/SmolLM2-1.7B-Instruct; seed 20261013; injection/learned_direction: margin effect +0.050 [-0.000, +0.100]; n=10.
- HuggingFaceTB/SmolLM2-1.7B-Instruct; seed 20261013; injection/norm_matched_random: margin effect +0.000 [-0.050, +0.050]; n=10.
- HuggingFaceTB/SmolLM2-1.7B-Instruct; seed 20261013; misleading/learned_direction: margin effect +0.012 [-0.025, +0.050]; n=10.
- HuggingFaceTB/SmolLM2-1.7B-Instruct; seed 20261013; misleading/norm_matched_random: margin effect +0.012 [-0.025, +0.050]; n=10.
- HuggingFaceTB/SmolLM2-1.7B-Instruct; seed 20261013; trusted_misleading/learned_direction: margin effect -0.012 [-0.062, +0.025]; n=10.
- HuggingFaceTB/SmolLM2-1.7B-Instruct; seed 20261013; trusted_misleading/norm_matched_random: margin effect -0.025 [-0.062, +0.000]; n=10.
- Qwen/Qwen2.5-3B-Instruct; seed 20261012; clean/learned_direction: margin effect +0.284 [-0.327, +1.029]; n=10.
- Qwen/Qwen2.5-3B-Instruct; seed 20261012; clean/norm_matched_random: margin effect +0.363 [-0.223, +1.092]; n=10.
- Qwen/Qwen2.5-3B-Instruct; seed 20261012; injection/learned_direction: margin effect -0.046 [-0.254, +0.137]; n=10.
- Qwen/Qwen2.5-3B-Instruct; seed 20261012; injection/norm_matched_random: margin effect -0.025 [-0.201, +0.150]; n=10.
- Qwen/Qwen2.5-3B-Instruct; seed 20261012; misleading/learned_direction: margin effect +0.482 [-0.263, +1.398]; n=10.
- Qwen/Qwen2.5-3B-Instruct; seed 20261012; misleading/norm_matched_random: margin effect +0.114 [-0.355, +0.646]; n=10.
- Qwen/Qwen2.5-3B-Instruct; seed 20261012; trusted_misleading/learned_direction: margin effect +0.745 [+0.122, +1.453]; n=10.
- Qwen/Qwen2.5-3B-Instruct; seed 20261012; trusted_misleading/norm_matched_random: margin effect +0.820 [+0.260, +1.534]; n=10.
- Qwen/Qwen2.5-3B-Instruct; seed 20261013; clean/learned_direction: margin effect +0.162 [-0.469, +0.913]; n=10.
- Qwen/Qwen2.5-3B-Instruct; seed 20261013; clean/norm_matched_random: margin effect +0.307 [-0.422, +1.142]; n=10.
- Qwen/Qwen2.5-3B-Instruct; seed 20261013; injection/learned_direction: margin effect +0.267 [-0.215, +0.769]; n=10.
- Qwen/Qwen2.5-3B-Instruct; seed 20261013; injection/norm_matched_random: margin effect +0.204 [-0.316, +0.747]; n=10.
- Qwen/Qwen2.5-3B-Instruct; seed 20261013; misleading/learned_direction: margin effect +0.586 [+0.134, +1.080]; n=10.
- Qwen/Qwen2.5-3B-Instruct; seed 20261013; misleading/norm_matched_random: margin effect +0.661 [+0.217, +1.160]; n=10.
- Qwen/Qwen2.5-3B-Instruct; seed 20261013; trusted_misleading/learned_direction: margin effect +0.461 [+0.143, +0.786]; n=10.
- Qwen/Qwen2.5-3B-Instruct; seed 20261013; trusted_misleading/norm_matched_random: margin effect +0.461 [+0.136, +0.786]; n=10.

## Leave-one-task-out robustness

- HuggingFaceTB/SmolLM2-1.7B-Instruct; seed 20261012; test_id; risk_internal: AUROC=0.755, n=240, errors=120.
- HuggingFaceTB/SmolLM2-1.7B-Instruct; seed 20261012; test_id; risk_text_output: AUROC=0.742, n=240, errors=120.
- HuggingFaceTB/SmolLM2-1.7B-Instruct; seed 20261012; test_id; risk_confidence: AUROC=0.526, n=240, errors=120.
- HuggingFaceTB/SmolLM2-1.7B-Instruct; seed 20261012; test_ood; risk_internal: AUROC=0.795, n=120, errors=61.
- HuggingFaceTB/SmolLM2-1.7B-Instruct; seed 20261012; test_ood; risk_text_output: AUROC=0.804, n=120, errors=61.
- HuggingFaceTB/SmolLM2-1.7B-Instruct; seed 20261012; test_ood; risk_confidence: AUROC=0.493, n=120, errors=61.
- HuggingFaceTB/SmolLM2-1.7B-Instruct; seed 20261013; test_id; risk_internal: AUROC=0.673, n=240, errors=120.
- HuggingFaceTB/SmolLM2-1.7B-Instruct; seed 20261013; test_id; risk_text_output: AUROC=0.704, n=240, errors=120.
- HuggingFaceTB/SmolLM2-1.7B-Instruct; seed 20261013; test_id; risk_confidence: AUROC=0.466, n=240, errors=120.
- HuggingFaceTB/SmolLM2-1.7B-Instruct; seed 20261013; test_ood; risk_internal: AUROC=0.605, n=120, errors=59.
- HuggingFaceTB/SmolLM2-1.7B-Instruct; seed 20261013; test_ood; risk_text_output: AUROC=0.678, n=120, errors=59.
- HuggingFaceTB/SmolLM2-1.7B-Instruct; seed 20261013; test_ood; risk_confidence: AUROC=0.430, n=120, errors=59.
- Qwen/Qwen2.5-1.5B-Instruct; seed 20261012; test_id; risk_internal: AUROC=0.652, n=240, errors=69.
- Qwen/Qwen2.5-1.5B-Instruct; seed 20261012; test_id; risk_text_output: AUROC=0.727, n=240, errors=69.
- Qwen/Qwen2.5-1.5B-Instruct; seed 20261012; test_id; risk_confidence: AUROC=0.698, n=240, errors=69.
- Qwen/Qwen2.5-1.5B-Instruct; seed 20261012; test_ood; risk_internal: AUROC=0.639, n=120, errors=48.
- Qwen/Qwen2.5-1.5B-Instruct; seed 20261012; test_ood; risk_text_output: AUROC=0.721, n=120, errors=48.
- Qwen/Qwen2.5-1.5B-Instruct; seed 20261012; test_ood; risk_confidence: AUROC=0.608, n=120, errors=48.
- Qwen/Qwen2.5-1.5B-Instruct; seed 20261013; test_id; risk_internal: AUROC=0.804, n=240, errors=62.
- Qwen/Qwen2.5-1.5B-Instruct; seed 20261013; test_id; risk_text_output: AUROC=0.668, n=240, errors=62.
- Qwen/Qwen2.5-1.5B-Instruct; seed 20261013; test_id; risk_confidence: AUROC=0.587, n=240, errors=62.
- Qwen/Qwen2.5-1.5B-Instruct; seed 20261013; test_ood; risk_internal: AUROC=0.688, n=120, errors=46.
- Qwen/Qwen2.5-1.5B-Instruct; seed 20261013; test_ood; risk_text_output: AUROC=0.594, n=120, errors=46.
- Qwen/Qwen2.5-1.5B-Instruct; seed 20261013; test_ood; risk_confidence: AUROC=0.546, n=120, errors=46.
- Qwen/Qwen2.5-3B-Instruct; seed 20261012; test_id; risk_internal: AUROC=0.848, n=240, errors=65.
- Qwen/Qwen2.5-3B-Instruct; seed 20261012; test_id; risk_text_output: AUROC=0.724, n=240, errors=65.
- Qwen/Qwen2.5-3B-Instruct; seed 20261012; test_id; risk_confidence: AUROC=0.803, n=240, errors=65.
- Qwen/Qwen2.5-3B-Instruct; seed 20261012; test_ood; risk_internal: AUROC=0.862, n=120, errors=45.
- Qwen/Qwen2.5-3B-Instruct; seed 20261012; test_ood; risk_text_output: AUROC=0.752, n=120, errors=45.
- Qwen/Qwen2.5-3B-Instruct; seed 20261012; test_ood; risk_confidence: AUROC=0.815, n=120, errors=45.
- Qwen/Qwen2.5-3B-Instruct; seed 20261013; test_id; risk_internal: AUROC=0.908, n=240, errors=60.
- Qwen/Qwen2.5-3B-Instruct; seed 20261013; test_id; risk_text_output: AUROC=0.765, n=240, errors=60.
- Qwen/Qwen2.5-3B-Instruct; seed 20261013; test_id; risk_confidence: AUROC=0.752, n=240, errors=60.
- Qwen/Qwen2.5-3B-Instruct; seed 20261013; test_ood; risk_internal: AUROC=0.845, n=120, errors=33.
- Qwen/Qwen2.5-3B-Instruct; seed 20261013; test_ood; risk_text_output: AUROC=0.752, n=120, errors=33.
- Qwen/Qwen2.5-3B-Instruct; seed 20261013; test_ood; risk_confidence: AUROC=0.793, n=120, errors=33.

## SAE (exploratory)

- frequency_matched_control: mean held-out delta-correct-margin +0.012, n=20 cases (not a mechanistic validation).
- selected_feature: mean held-out delta-correct-margin -0.006, n=20 cases (not a mechanistic validation).

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
