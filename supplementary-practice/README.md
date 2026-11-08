# Supplementary Practice (Original Additions)

This folder contains additional, self-authored practice examples prepared to extend the coursework collection. These files are **not represented as submitted course assignments** or as work completed for an employer/client.

## Included examples

- `prophet_forecasting_walkthrough.py`: end-to-end daily forecasting using a reproducible synthetic dataset, chronological holdout, Prophet, and MAE/RMSE evaluation.
- `holt_winters_sarimax_comparison.py`: monthly synthetic series and a chronological comparison of Holt-Winters and SARIMAX.

## Run

Create a virtual environment, then install the relevant packages:

```bash
python -m venv .venv
# Windows: .venv\Scripts\activate
# macOS/Linux: source .venv/bin/activate
pip install -r requirements.txt
python prophet_forecasting_walkthrough.py
python holt_winters_sarimax_comparison.py
```

The examples generate their own synthetic data. They do not require private, proprietary, or third-party datasets.

## Interpretation

Synthetic data is useful for demonstrating workflow and code structure, but it does not establish real-world forecasting accuracy. For an empirical study, replace the synthetic series with a documented dataset, preserve chronological splits, compare against suitable baselines, and report uncertainty and limitations.
