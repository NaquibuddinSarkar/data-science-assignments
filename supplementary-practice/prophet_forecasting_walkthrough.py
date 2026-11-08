"""
Prophet forecasting walkthrough using reproducible synthetic daily data.

This is a supplementary, self-authored learning example. It is not a real
energy-demand study and makes no claim about real-world forecast accuracy.
Install dependencies from this folder's requirements.txt before running.
"""
from __future__ import annotations

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from prophet import Prophet
from sklearn.metrics import mean_absolute_error, mean_squared_error


def make_daily_series(seed: int = 17, periods: int = 900) -> pd.DataFrame:
    """Create a synthetic daily series with trend, weekly/yearly seasonality and noise."""
    rng = np.random.default_rng(seed)
    dates = pd.date_range("2022-01-01", periods=periods, freq="D")
    t = np.arange(periods)
    trend = 0.025 * t
    weekly = 7.0 * np.sin(2 * np.pi * t / 7)
    yearly = 18.0 * np.sin(2 * np.pi * t / 365.25)
    noise = rng.normal(0, 4.0, periods)
    values = 120 + trend + weekly + yearly + noise
    return pd.DataFrame({"ds": dates, "y": values})


def main() -> None:
    data = make_daily_series()
    holdout_days = 90
    train = data.iloc[:-holdout_days].copy()
    test = data.iloc[-holdout_days:].copy()

    model = Prophet(
        weekly_seasonality=True,
        yearly_seasonality=True,
        daily_seasonality=False,
        changepoint_prior_scale=0.05,
    )
    model.fit(train)

    forecast = model.predict(test[["ds"]])
    comparison = test.merge(forecast[["ds", "yhat", "yhat_lower", "yhat_upper"]], on="ds")

    mae = mean_absolute_error(comparison["y"], comparison["yhat"])
    rmse = np.sqrt(mean_squared_error(comparison["y"], comparison["yhat"]))
    print(f"Holdout MAE:  {mae:.3f}")
    print(f"Holdout RMSE: {rmse:.3f}")
    print("\nFirst five holdout predictions:")
    print(comparison.head().to_string(index=False))

    plt.figure(figsize=(12, 5))
    plt.plot(train["ds"], train["y"], label="Training observations", linewidth=1)
    plt.plot(test["ds"], test["y"], label="Actual holdout", linewidth=1.5)
    plt.plot(comparison["ds"], comparison["yhat"], label="Prophet forecast", linewidth=1.5)
    plt.fill_between(
        comparison["ds"],
        comparison["yhat_lower"],
        comparison["yhat_upper"],
        alpha=0.2,
        label="Prophet uncertainty interval",
    )
    plt.title("Prophet: synthetic daily-series holdout forecast")
    plt.xlabel("Date")
    plt.ylabel("Synthetic value")
    plt.legend()
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()
