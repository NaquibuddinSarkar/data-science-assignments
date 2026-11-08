# Supplementary Practice

This folder contains original practice material added separately from the uploaded course bundle. It is not represented as a set of completed course submissions. The notebooks use synthetic data unless explicitly stated otherwise.

## Notebooks

| File | Focus |
|---|---|
| 01_customer_eda_and_kpis.ipynb | EDA, customer segmentation and business KPIs |
| 02_visualization_storytelling.ipynb | Distributions, category comparisons and relationships |
| 03_ab_testing_and_hypothesis_testing.ipynb | Proportion tests, confidence intervals and Welch's test |
| 04_machine_learning_regression_pipeline.ipynb | Preprocessing, Random Forest, cross-validation and permutation importance |
| 05_prophet_time_series_forecasting.ipynb | Prophet, seasonal-naive benchmark and chronological holdout |
| 06_energy_demand_analytics.ipynb | Synthetic half-hourly meter profiles and load prediction |
| 07_python_foundations.ipynb | Python data types, functions, control flow and validation |
| 08_pandas_data_cleaning.ipynb | Missing data, duplicates, joins, grouping and pivots |
| 09_classification_model_evaluation.ipynb | Logistic regression, Random Forest, ROC-AUC and threshold metrics |
| 10_customer_segmentation_clustering.ipynb | Scaling, K-Means, silhouette score and PCA |
| 11_sarimax_forecasting_comparison.ipynb | SARIMAX and seasonal-naive benchmark |
| 12_advanced_statistics_practical.ipynb | Welch t-test, ANOVA, correlation, chi-square, regression and Bayes |
| 13_advanced_ml_model_selection_ensembles.ipynb | Ridge/Lasso, cross-validation, bagging, boosting, voting and stacking |
| 14_big_data_pyspark_workflow.ipynb | Spark DataFrames, lazy evaluation, joins, windows and Parquet |
| 15_attention_mechanism_for_time_series.ipynb | Query-Key-Value attention and weighted context |
| 16_production_monitoring_and_safe_rollout.ipynb | Data drift, freshness, calibration, monitoring layers and safe rollout |
| 17_factor_analysis_and_multiple_regression.ipynb | Factor analysis, multiple regression, VIF and residual diagnostics |
| 18_pv_degradation_and_waste_forecasting.ipynb | Weibull lifetime modelling, degradation, cohorts and synthetic waste projections |

## General installation

From the repository root:

```bash
python -m venv .venv
# Windows: .venv\\Scripts\\activate
# macOS/Linux: source .venv/bin/activate
pip install -r supplementary-practice/requirements.txt
```

Open a notebook in JupyterLab, VS Code or Google Colab and run cells from top to bottom. Prophet may require platform-specific dependencies.

## Optional PySpark dependencies

For the big-data notebook, install:

```bash
pip install -r supplementary-practice/requirements-big-data.txt
```

PySpark may also require a compatible Java runtime. Google Colab images generally include common system tooling, but verify the current runtime before running Spark.

## API and deployment

The separate [deployment example](deployment/README.md) contains FastAPI source code, a model-training script, automated endpoint tests, a Dockerfile and instructions. The repository workflow at .github/workflows/deployment-demo-ci.yml runs its tests on pushes to main, pull requests and manual dispatch.

## Reproducibility and limitations

- Random seeds are set where sampling or simulation is used.
- The datasets are synthetic. They do not represent real customers, employees, companies, utilities or BUET thesis measurements.
- Forecasting and model scores on synthetic data are not evidence of real-world performance.
- Notebook files have been checked for valid Jupyter JSON structure. They have not all been executed end-to-end in a clean environment.
- The FastAPI deployment tests have been run successfully through GitHub Actions on Python 3.12.
- For applied work, document data source and licence, define targets, prevent leakage, compare with simple baselines and report uncertainty.
- Do not publish course-provided or third-party material unless redistribution is permitted.
