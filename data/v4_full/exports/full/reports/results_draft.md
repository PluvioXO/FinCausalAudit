# FinCausalAudit v4 — measured results (NOT a paper claim generator)

- Profile: `full`; protocol `FinCausalAudit-v4.0.0-hardtasks-causal-identity`
- Completed jobs: 18 / 18
- Failures: 0
- Models: Qwen/Qwen2.5-1.5B-Instruct, Qwen/Qwen2.5-3B-Instruct, Qwen/Qwen3-4B-Instruct-2507, microsoft/Phi-4-mini-instruct, ibm-granite/granite-3.3-2b-instruct, allenai/OLMo-2-0425-1B-Instruct
- All accuracy and AUROC scores below are from the newly generated multi-step synthetic scenarios.
- Prior v3 activations and scores are not mixed with the new experiment.
- Zero-error models are marked unestimable for error AUROC.
- Causal results are NEVER interpreted if their identity/null controls fail.

## Error detection
- Qwen/Qwen2.5-1.5B-Instruct / test_id / confidence_risk: mean AUROC 0.3630 across 3 seeds.
- Qwen/Qwen2.5-1.5B-Instruct / test_id / internal_risk: mean AUROC 0.8878 across 3 seeds.
- Qwen/Qwen2.5-1.5B-Instruct / test_id / text_output_risk: mean AUROC 0.7052 across 3 seeds.
- Qwen/Qwen2.5-1.5B-Instruct / test_ood / confidence_risk: mean AUROC 0.3104 across 3 seeds.
- Qwen/Qwen2.5-1.5B-Instruct / test_ood / internal_risk: mean AUROC 0.7180 across 3 seeds.
- Qwen/Qwen2.5-1.5B-Instruct / test_ood / text_output_risk: mean AUROC 0.7268 across 3 seeds.
- Qwen/Qwen2.5-3B-Instruct / test_id / confidence_risk: mean AUROC 0.4102 across 3 seeds.
- Qwen/Qwen2.5-3B-Instruct / test_id / internal_risk: mean AUROC 0.9861 across 3 seeds.
- Qwen/Qwen2.5-3B-Instruct / test_id / text_output_risk: mean AUROC 0.8356 across 3 seeds.
- Qwen/Qwen2.5-3B-Instruct / test_ood / confidence_risk: mean AUROC 0.3930 across 3 seeds.
- Qwen/Qwen2.5-3B-Instruct / test_ood / internal_risk: mean AUROC 0.9088 across 3 seeds.
- Qwen/Qwen2.5-3B-Instruct / test_ood / text_output_risk: mean AUROC 0.8022 across 3 seeds.
- Qwen/Qwen3-4B-Instruct-2507 / test_id / confidence_risk: mean AUROC 0.4423 across 3 seeds.
- Qwen/Qwen3-4B-Instruct-2507 / test_id / internal_risk: mean AUROC 0.9513 across 3 seeds.
- Qwen/Qwen3-4B-Instruct-2507 / test_id / text_output_risk: mean AUROC 0.6527 across 3 seeds.
- Qwen/Qwen3-4B-Instruct-2507 / test_ood / confidence_risk: mean AUROC 0.5323 across 3 seeds.
- Qwen/Qwen3-4B-Instruct-2507 / test_ood / internal_risk: mean AUROC 0.7975 across 3 seeds.
- Qwen/Qwen3-4B-Instruct-2507 / test_ood / text_output_risk: mean AUROC 0.4829 across 3 seeds.
- allenai/OLMo-2-0425-1B-Instruct / test_id / confidence_risk: mean AUROC 0.4056 across 3 seeds.
- allenai/OLMo-2-0425-1B-Instruct / test_id / internal_risk: mean AUROC 0.8735 across 3 seeds.
- allenai/OLMo-2-0425-1B-Instruct / test_id / text_output_risk: mean AUROC 0.8379 across 3 seeds.
- allenai/OLMo-2-0425-1B-Instruct / test_ood / confidence_risk: mean AUROC 0.3968 across 3 seeds.
- allenai/OLMo-2-0425-1B-Instruct / test_ood / internal_risk: mean AUROC 0.6151 across 3 seeds.
- allenai/OLMo-2-0425-1B-Instruct / test_ood / text_output_risk: mean AUROC 0.6082 across 3 seeds.
- ibm-granite/granite-3.3-2b-instruct / test_id / confidence_risk: mean AUROC 0.2577 across 3 seeds.
- ibm-granite/granite-3.3-2b-instruct / test_id / internal_risk: mean AUROC 0.9251 across 3 seeds.
- ibm-granite/granite-3.3-2b-instruct / test_id / text_output_risk: mean AUROC 0.7960 across 3 seeds.
- ibm-granite/granite-3.3-2b-instruct / test_ood / confidence_risk: mean AUROC 0.2741 across 3 seeds.
- ibm-granite/granite-3.3-2b-instruct / test_ood / internal_risk: mean AUROC 0.7925 across 3 seeds.
- ibm-granite/granite-3.3-2b-instruct / test_ood / text_output_risk: mean AUROC 0.6824 across 3 seeds.
- microsoft/Phi-4-mini-instruct / test_id / confidence_risk: mean AUROC 0.3482 across 3 seeds.
- microsoft/Phi-4-mini-instruct / test_id / internal_risk: mean AUROC 0.9435 across 3 seeds.
- microsoft/Phi-4-mini-instruct / test_id / text_output_risk: mean AUROC 0.7645 across 3 seeds.
- microsoft/Phi-4-mini-instruct / test_ood / confidence_risk: mean AUROC 0.4925 across 3 seeds.
- microsoft/Phi-4-mini-instruct / test_ood / internal_risk: mean AUROC 0.6187 across 3 seeds.
- microsoft/Phi-4-mini-instruct / test_ood / text_output_risk: mean AUROC 0.5468 across 3 seeds.

## Causal identity-control audit
- Qwen/Qwen2.5-1.5B-Instruct / 20261031: valid=True, reason=passed.
- Qwen/Qwen2.5-1.5B-Instruct / 20261101: valid=True, reason=passed.
- Qwen/Qwen2.5-1.5B-Instruct / 20261102: valid=True, reason=passed.
- Qwen/Qwen2.5-3B-Instruct / 20261031: valid=True, reason=passed.
- Qwen/Qwen2.5-3B-Instruct / 20261101: valid=True, reason=passed.
- Qwen/Qwen2.5-3B-Instruct / 20261102: valid=True, reason=passed.
- Qwen/Qwen3-4B-Instruct-2507 / 20261031: valid=True, reason=passed.
- Qwen/Qwen3-4B-Instruct-2507 / 20261101: valid=True, reason=passed.
- Qwen/Qwen3-4B-Instruct-2507 / 20261102: valid=True, reason=passed.
- allenai/OLMo-2-0425-1B-Instruct / 20261031: valid=True, reason=passed.
- allenai/OLMo-2-0425-1B-Instruct / 20261101: valid=True, reason=passed.
- allenai/OLMo-2-0425-1B-Instruct / 20261102: valid=True, reason=passed.
- ibm-granite/granite-3.3-2b-instruct / 20261031: valid=True, reason=passed.
- ibm-granite/granite-3.3-2b-instruct / 20261101: valid=True, reason=passed.
- ibm-granite/granite-3.3-2b-instruct / 20261102: valid=True, reason=passed.
- microsoft/Phi-4-mini-instruct / 20261031: valid=True, reason=passed.
- microsoft/Phi-4-mini-instruct / 20261101: valid=True, reason=passed.
- microsoft/Phi-4-mini-instruct / 20261102: valid=True, reason=passed.

## Evidence quality and reporting rules
1. The tasks use deterministic synthetic numerical rules; an independent rule-verifier is an oracle for these cases.
2. A/B next-token probabilities are not unconstrained generated recommendations.
3. Text-only/output-aware classifiers are valid comparators; confidence alone is weak.
4. Case-disjoint tests and unseen templates are different generalisation claims.
5. Do not treat repeated model seeds as independent real financial cases.
6. Actual SEC facts are extracted structured data, not prose filings; count company-years rather than prompt repeats.
7. Before alleging a discovered causal source-trust circuit, validate identity, null, and direction-specific controls.
8. Retain negative and unestimable findings; no selectively dropping failed models.
9. Report changes to protocol and model revisions transparently.
10. This export does not guarantee conference acceptance.
