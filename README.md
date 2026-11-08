# Data Science Coursework and Practice Portfolio

This repository separates two kinds of material:

1. **Original course materials and assignments** — these should retain their course context, original filenames, datasets and attribution.
2. **Supplementary practice examples** — new, self-authored examples added to extend the portfolio and demonstrate reproducible analytical workflows.

> **Current status:** the original course ZIP was curated into a 61-file package (including 24 notebooks), but those original files have **not yet been copied into this GitHub repository**. The files currently committed here are the supplementary examples listed below. This distinction is intentional; supplementary examples are not being presented as submitted coursework.

## Supplementary practice currently in this repository

### Jupyter notebooks

| Notebook | Main topics |
|---|---|
| [01 Python foundations](supplementary-practice/notebooks/07_python_foundations.ipynb) | Python types, functions, control flow, exceptions |
| [02 Pandas data cleaning](supplementary-practice/notebooks/08_pandas_data_cleaning.ipynb) | Missing values, duplicates, joins, groupby, pivot |
| [03 Customer EDA and KPIs](supplementary-practice/notebooks/01_customer_eda_and_kpis.ipynb) | Data quality, segmentation, business metrics |
| [04 Visualisation storytelling](supplementary-practice/notebooks/02_visualization_storytelling.ipynb) | Distributions, category comparisons, relationships |
| [05 A/B testing](supplementary-practice/notebooks/03_ab_testing_and_hypothesis_testing.ipynb) | Two-proportion tests, confidence intervals, Welch test |
| [06 Regression pipeline](supplementary-practice/notebooks/04_machine_learning_regression_pipeline.ipynb) | Preprocessing, Random Forest, cross-validation, metrics |
| [07 Classification evaluation](supplementary-practice/notebooks/09_classification_model_evaluation.ipynb) | Logistic regression, Random Forest, ROC-AUC, precision/recall |
| [08 Customer clustering](supplementary-practice/notebooks/10_customer_segmentation_clustering.ipynb) | Scaling, K-Means, silhouette, PCA |
| [09 Prophet forecasting](supplementary-practice/notebooks/05_prophet_time_series_forecasting.ipynb) | Weekly/yearly seasonality, seasonal-naive baseline, MAE/RMSE |
| [10 SARIMAX forecasting](supplementary-practice/notebooks/11_sarimax_forecasting_comparison.ipynb) | Seasonal-naive benchmark, SARIMAX, holdout evaluation |
| [11 Energy demand analytics](supplementary-practice/notebooks/06_energy_demand_analytics.ipynb) | Synthetic meter data, load profile, Random Forest regression |

### API deployment example

The [FastAPI deployment example](supplementary-practice/deployment/) contains a training script, a prediction API, requirements and run instructions. It uses the sample Iris dataset and is an educational example, not a production service.

## Running the supplementary notebooks

Install the packages from the supplementary folder:

```bash
python -m venv .venv
# Windows: .venv\\Scripts\\activate
# macOS/Linux: source .venv/bin/activate
pip install -r supplementary-practice/requirements.txt
```

Open the notebooks in JupyterLab, VS Code or Google Colab. Prophet can require additional platform-specific dependencies; consult the Prophet installation guidance if installation fails.

For the API example, follow [its README](supplementary-practice/deployment/README.md) and install its separate requirements file.

## Data, testing and interpretation

- Supplementary notebooks generate synthetic datasets locally. These records are not actual customer, employee, utility or BUET research observations.
- The notebooks are instructional examples. They have not all been executed end-to-end in a clean environment.
- Forecasting and machine-learning results on synthetic data are not evidence of real-world model performance.
- For applied research, replace synthetic data with a documented, permitted dataset; preserve chronological splits for time series; compare against simple baselines; and report limitations.
- Do not publish course datasets or other third-party material unless redistribution is permitted.
- Preserve course instructions, source citations and attribution when adding the original coursework package.

## Prepared coursework package

A separate GitHub-ready archive was prepared from the uploaded course bundle. It contains 61 files, including 24 notebooks, datasets, scripts and documentation organised into seven topic folders. It is **not yet committed to this repository**. Once those original files are imported, they should remain clearly separated from `supplementary-practice/`.

