# Data Science Coursework and Practice Portfolio

This repository separates original course materials and assignments from supplementary practice examples added to extend the portfolio.

> **Coursework import status:** the uploaded course bundle was curated into a separate GitHub-ready package of 61 files (including 24 notebooks). Those exact original files have not yet been imported here. The material currently committed under supplementary-practice is newly authored practice, not represented as submitted course work.

## Original supplementary notebooks

The notebook collection is intended to work in JupyterLab, VS Code and Google Colab. Click any notebook below to preview it on GitHub; the COLAB_GUIDE.md explains how to open notebooks in Colab and how to share your own Colab work for review.

| Notebook | Course topic |
|---|---|
| [01 Customer EDA and KPIs](supplementary-practice/notebooks/01_customer_eda_and_kpis.ipynb) | EDA, segmentation and business metrics |
| [02 Visualisation storytelling](supplementary-practice/notebooks/02_visualization_storytelling.ipynb) | Distributions, comparisons and relationships |
| [03 A/B testing](supplementary-practice/notebooks/03_ab_testing_and_hypothesis_testing.ipynb) | Hypothesis tests, confidence intervals and effect size |
| [04 Regression pipeline](supplementary-practice/notebooks/04_machine_learning_regression_pipeline.ipynb) | Preprocessing, Random Forest and cross-validation |
| [05 Prophet forecasting](supplementary-practice/notebooks/05_prophet_time_series_forecasting.ipynb) | Seasonality and chronological holdout validation |
| [06 Energy demand analytics](supplementary-practice/notebooks/06_energy_demand_analytics.ipynb) | Synthetic meter data and load prediction |
| [07 Python foundations](supplementary-practice/notebooks/07_python_foundations.ipynb) | Python functions, control flow and validation |
| [08 Pandas data cleaning](supplementary-practice/notebooks/08_pandas_data_cleaning.ipynb) | Missing data, joins, grouping and pivots |
| [09 Classification evaluation](supplementary-practice/notebooks/09_classification_model_evaluation.ipynb) | Logistic regression, Random Forest and ROC-AUC |
| [10 Customer clustering](supplementary-practice/notebooks/10_customer_segmentation_clustering.ipynb) | K-Means, scaling, silhouette score and PCA |
| [11 SARIMAX forecasting](supplementary-practice/notebooks/11_sarimax_forecasting_comparison.ipynb) | Seasonal naive and SARIMAX benchmarking |
| [12 Advanced statistics](supplementary-practice/notebooks/12_advanced_statistics_practical.ipynb) | Welch t-test, ANOVA, correlations, chi-square, regression and Bayes |
| [13 Advanced ML and ensembles](supplementary-practice/notebooks/13_advanced_ml_model_selection_ensembles.ipynb) | Ridge/Lasso, cross-validation, bagging, boosting, voting and stacking |
| [14 PySpark workflow](supplementary-practice/notebooks/14_big_data_pyspark_workflow.ipynb) | Spark DataFrames, lazy evaluation, joins, windows and Parquet |
| [15 Attention for time series](supplementary-practice/notebooks/15_attention_mechanism_for_time_series.ipynb) | Query-Key-Value and scaled dot-product attention |
| [16 Production monitoring](supplementary-practice/notebooks/16_production_monitoring_and_safe_rollout.ipynb) | Drift, freshness, calibration, monitoring layers and safe rollout |

## Applied assignment briefs

New exercises based on the course content are available in [assignments/](assignments/README.md):

1. [Energy demand forecasting](assignments/assignment_01_energy_forecasting.md)
2. [Production monitoring and safe rollout](assignments/assignment_02_production_monitoring.md)
3. [Big-data transaction analytics with PySpark](assignments/assignment_03_pyspark_analytics.md)
4. [Model selection and ensemble benchmarking](assignments/assignment_04_ensemble_benchmarking.md)
5. [CI/CD, Docker and rollback](assignments/assignment_05_ci_cd_docker_and_rollback.md)

These are practice briefs, not answers to the course's graded assignments.

## Course alignment

See [COURSE_ALIGNMENT.md](COURSE_ALIGNMENT.md) for a topic-by-topic map from the uploaded course slides and assignments to the notebooks, practice briefs and deployment examples.

## Model deployment and CI/CD

The [FastAPI deployment example](supplementary-practice/deployment/) includes model training, a prediction API, endpoint tests and a Dockerfile. A GitHub Actions workflow at [.github/workflows/deployment-demo-ci.yml](.github/workflows/deployment-demo-ci.yml) runs on pushes to main, pull requests and manual dispatch. It uses Python 3.12, installs the deployment demo's requirements and runs pytest.

The Docker demonstration is local and educational. It does not deploy to AWS ECS/Fargate or Docker Hub automatically.

## Install

For the general notebooks:

```bash
python -m venv .venv
# Windows: .venv\\Scripts\\activate
# macOS/Linux: source .venv/bin/activate
pip install -r supplementary-practice/requirements.txt
```

For PySpark, install the optional dependencies:

```bash
pip install -r supplementary-practice/requirements-big-data.txt
```

For the FastAPI deployment demo, follow the folder-specific instructions in [its README](supplementary-practice/deployment/README.md).

## Colab and your existing notebooks

See [COLAB_GUIDE.md](COLAB_GUIDE.md). Example: [open the PV forecasting notebook in Google Colab](https://colab.research.google.com/github/NaquibuddinSarkar/data-science-assignments/blob/main/supplementary-practice/notebooks/18_pv_degradation_and_waste_forecasting.ipynb). I do not have a direct connection to your private Colab runtime or Drive, but can inspect and improve notebooks you upload as .ipynb files or share through an accessible link.

## Data, testing and interpretation

- Supplementary notebooks generate synthetic datasets. They do not represent real customers, employees, companies, utilities or BUET thesis observations.
- Notebook JSON structure has been checked; the notebooks have not all been executed end-to-end in a clean environment.
- Scores on synthetic data are not evidence of real-world performance.
- For applied work, document data source and licence, define prediction targets, prevent leakage, compare with simple baselines and report uncertainty and limitations.
- Do not publish third-party or course-provided datasets unless redistribution is permitted.
- Preserve course attribution and context when importing your original course exercises.

