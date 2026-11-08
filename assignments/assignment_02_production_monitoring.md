# Assignment 2 — Production Monitoring and Safe Model Rollout

**Level:** Intermediate to advanced. **Course alignment:** Data Science in Production, monitoring and cloud deployment.

## Scenario: SolarPulse Operations
A service operator uses an ML model to predict whether a rooftop solar installation will experience an inverter fault within 24 hours. The model was trained using validated maintenance records from two sites and is now being tested at three additional sites.

| Metric | Site A | Site B | Site C |
|---|---:|---:|---:|
| Offline ROC-AUC at launch | 0.91 | 0.91 | 0.91 |
| Recent labelled ROC-AUC | 0.89 | 0.86 | 0.63 |
| Feature missing rate | 0.5% | 1.2% | 18% |
| Median feature age | 4 min | 7 min | 46 min |
| P95 API latency | 140 ms | 155 ms | 170 ms |
| Alert acknowledgement rate | 91% | 86% | 48% |

Additional fictional facts: Site C uses different firmware and local-time timestamps; one feed changed temperature from degrees Celsius to tenths of a degree; maintenance labels arrive 2–5 days after faults; the proposed model scores 2% better on a random offline split.

## Questions

### Q1. Diagnose failures
Identify at least three plausible failure patterns. Cite evidence. Distinguish training-serving skew, data/schema pipeline problems, delayed labels and concept drift.

### Q2. Four-layer monitoring plan
Create a plan with at least two metrics per layer:
- System: P50/P95/P99 latency, throughput, error rate, queue depth, CPU/memory.
- Data: missing rate, schema/type/unit changes, distribution shift, category cardinality, feature freshness.
- Model: prediction distribution, confidence, calibration and rolling labelled performance.
- Business/operations: alert acknowledgement, confirmed fault capture, false dispatch rate and site-level outcomes.

For at least three metrics specify baseline, alert threshold, owner and response.

### Q3. Delayed labels and calibration
Explain why today's prediction metrics may be unavailable or misleading when labels arrive days later. Propose a monitoring design that joins predictions to eventual labels and reports performance by site and firmware.

### Q4. Safe rollout
Design offline validation, shadow deployment, a small canary, gradual promotion and rollback conditions. State the evidence required before each promotion step.

### Q5. Engineering remediation
Describe how to fix timestamp, temperature-unit and freshness problems and prevent recurrence.

## Deliverables
Monitoring metric table; data validation code or pseudocode; release/rollback decision diagram; 500–800 word incident analysis; README with assumptions.

## Assessment rubric (100 points)
| Area | Points |
|---|---:|
| Evidence-based failure diagnosis | 20 |
| Monitoring coverage and measurable thresholds | 25 |
| Delayed labels and calibration reasoning | 15 |
| Shadow/canary release plan | 25 |
| Engineering remediation and clarity | 15 |

This is an engineering exercise, not a diagnostic tool for actual solar equipment or a substitute for electrical safety procedures.
