# Assignment 4 — Model Selection, Regularisation and Ensembles

**Level:** Intermediate to advanced. **Course alignment:** Advanced Machine Learning.

## Scenario
An operations team wants to predict a continuous KPI for weekly planning. The current linear baseline is stable but misses nonlinear patterns. The team proposes replacing it with a complex ensemble. Test whether complexity actually improves generalisation.

## Required modelling approaches
1. Linear regression baseline.
2. Ridge regression with cross-validated alpha.
3. Lasso regression with cross-validated alpha.
4. Random Forest or another bagging model.
5. Gradient boosting model.
6. Voting or stacking ensemble.

## Requirements
- Split data into train, validation and final test sets.
- Put preprocessing inside pipelines to prevent leakage.
- Use cross-validation on training data for model selection.
- Engineer at least two defensible features and explain them.
- Report MAE, RMSE and R-squared on the same held-out test set.
- Compare training and validation performance for underfitting/overfitting.
- Examine residuals and permutation importance.
- Explain bagging, boosting, voting and stacking.
- Explain why an ensemble can perform worse than its strongest base learner.

## Deliverables
- ensemble_benchmarking.ipynb
- Model comparison table
- At least two diagnostic figures
- Short model-card summary: intended use, data, metrics, limitations and risks

## Assessment rubric (100 points)
| Area | Points |
|---|---:|
| Experimental design and leakage prevention | 20 |
| Regularised linear models | 15 |
| Tree ensembles and ensemble strategy | 25 |
| Evaluation and residual analysis | 20 |
| Interpretation and model documentation | 20 |

Do not select a model solely on one favourable metric. Discuss operational cost, interpretability and maintenance as well as predictive performance.
