# Supplementary Practice

This folder contains **original practice material added separately from the uploaded course bundle**. It is not presented as a set of completed course submissions. Synthetic data are generated in the notebooks, and all analyses are instructional examples.

## Notebooks

| File | Focus |
|---|---|
| `07_python_foundations.ipynb` | Core Python, functions, validation and iteration |
| `08_pandas_data_cleaning.ipynb` | Cleaning, missing values, joins, groupby and pivot |
| `01_customer_eda_and_kpis.ipynb` | EDA, customer segmentation and business KPIs |
| `02_visualization_storytelling.ipynb` | Visualisation choices and interpretation |
| `03_ab_testing_and_hypothesis_testing.ipynb` | Proportion tests, confidence intervals and Welch's test |
| `04_machine_learning_regression_pipeline.ipynb` | Preprocessing, regression, cross-validation and permutation importance |
| `09_classification_model_evaluation.ipynb` | Logistic regression, Random Forest, ROC-AUC and threshold metrics |
| `10_customer_segmentation_clustering.ipynb` | Scaling, K-Means, silhouette score and PCA |
| `05_prophet_time_series_forecasting.ipynb` | Prophet, seasonal-naive benchmark and chronological holdout |
| `11_sarimax_forecasting_comparison.ipynb` | SARIMAX and seasonal-naive model comparison |
| `06_energy_demand_analytics.ipynb` | Synthetic half-hourly meter profiles and load prediction |

## Install and run

From the repository root:

```bash
python -m venv .venv
# Windows: .venv\\Scripts\\activate
# macOS/Linux: source .venv/bin/activate
pip install -r supplementary-practice/requirements.txt
```

Open any notebook in JupyterLab, VS Code or Google Colab. Run cells from top to bottom. Some package versions or operating systems may require installation adjustments; Prophet is the package most likely to require additional platform-specific dependencies.

The separate [deployment example](deployment/README.md) has its own requirements file and run instructions.

## Reproducibility and limitations

- Random seeds are set in the notebooks where sampling or simulation is used.
- The datasets are synthetic. They do not represent real customers, employees, companies, utilities or BUET thesis measurements.
- Forecasting and model scores on synthetic data are not evidence of real-world performance.
- The notebooks have been checked for valid Jupyter notebook JSON structure, but they have **not all been executed end-to-end in a clean environment**.
- For applied work, document the data source and licence, define the prediction target, prevent leakage, compare against simple baselines, and report uncertainty and limitations.
