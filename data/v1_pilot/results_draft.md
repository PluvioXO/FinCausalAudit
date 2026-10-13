# FinCausalAudit: computed results draft

**DO NOT CITE THIS FILE AS VERIFIED RESULTS WITHOUT REVIEW AND REPLICATION.**

Model: `Qwen/Qwen2.5-1.5B-Instruct`; seed `20261012`; cases `128`; smoke test `False`; GPU `NVIDIA L4`.

## Synthetic held-out behavioural findings

- `misleading` vs clean: correct-letter margin Δ -1.184 (case-bootstrap 95% CI [-1.715, -0.695]); accuracy Δ -0.062 [-0.188, +0.062].
- `injection` vs clean: correct-letter margin Δ -2.941 (case-bootstrap 95% CI [-3.914, -2.070]); accuracy Δ -0.125 [-0.250, -0.031].
- `authority_swap` vs clean: correct-letter margin Δ -2.703 (case-bootstrap 95% CI [-3.739, -1.722]); accuracy Δ -0.156 [-0.345, +0.032].
- `evidence_flip` vs clean: correct-letter margin Δ +0.723 (case-bootstrap 95% CI [-1.164, +2.809]); accuracy Δ +0.000 [-0.250, +0.281].

Additional behavioural controls:
- fact_flip_changes_choice: 0.438, CI [0.281, 0.625] (n=32).
- source_label_swap_changes_choice: 0.219, CI [0.094, 0.344] (n=32).
- misleading_changes_choice: 0.125, CI [0.031, 0.250] (n=32).
- injection_changes_choice: 0.125, CI [0.031, 0.250] (n=32).
- Unconstrained exact-letter generation compliance: 1.000 (n=16); this is supplementary.

## Probe (error detection)

- output_baseline: n=96, errors=33, AUROC=0.661, AUPRC=0.465, Brier=0.238.
- selected_layer_24: n=96, errors=33, AUROC=0.985, AUPRC=0.975, Brier=0.066.
- A probe exceeding this baseline is only an **incremental prediction result**, not mechanistic attribution.


## Patching

- Last tested layer 27, clean_into_injection: Δ original-correct margin +2.458 [+1.323, +3.626], n=12.
- Last tested layer 27, counterfactual_into_injection: Δ original-correct margin -3.698 [-5.167, -2.208], n=12.
- Last tested layer 27, other_clean_matched: Δ original-correct margin +5.146 [+3.489, +6.698], n=12.
- Last tested layer 27, other_injected_matched: Δ original-correct margin +1.073 [-0.125, +2.198], n=12.
- A last-layer residual carries downstream answer information; this alone cannot establish provenance mechanisms.


## Steering

- Layer and strength selected on validation: layer 16, α=1.0.
- clean/random_direction: test Δ margin +0.027 [-0.059, +0.109], n=32.
- clean/trained_direction: test Δ margin -0.184 [-0.246, -0.121], n=32.
- injection/random_direction: test Δ margin -0.113 [-0.188, -0.035], n=32.
- injection/trained_direction: test Δ margin +0.059 [-0.051, +0.180], n=32.

## Sparse features

- SAE layer 16, holdout token reconstruction VE=0.982.
- chosen_feature, feature 2498: test Δ margin -0.043 [-0.164, +0.086].
- frequency_control, feature 2960: test Δ margin -0.016 [-0.047, +0.012].
- SAE features are not semantically labelled or validated; causal ablation results require further controls.

## Before submitting

- [ ] Run >=3 independent seeds, report across-seed variation.
- [ ] Add a second model and a genuinely out-of-distribution financial document task.
- [ ] Confirm source authenticity and licensing for external documents.
- [ ] Predeclare primary endpoint and negative controls to mitigate selection bias.
- [ ] Inspect raw prompts, tokenization, failure cases and calibration plots.
- [ ] Distinguish causal residual interventions from source-trust feature localization.
- [ ] Acknowledge failure modes, null findings, synthetic-only constraints, and confidence interval definitions.
