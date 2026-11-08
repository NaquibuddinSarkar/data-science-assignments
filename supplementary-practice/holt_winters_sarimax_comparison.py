"""
Holt-Winters vs SARIMAX on a reproducible synthetic monthly series.

Supplementary self-authored practice example. The series is synthetic;
metrics are a coding demonstration, not evidence of real-world performance.
"""
from __future__ import annotations

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.metrics import mean_absolute_error, mean_squared_error
from statsmodels.tsa.holtwinters import ExponentialSmoothing
from statsmodels.tsa.statespace.sarimax import SARIMAX


def make_monthly_series(seed: int = 29, periods: int = 120) -> pd.Series:
    rng = np.random.default_rng(seed)
    dates = pd.date_range("2015-01-01", periods=periods, freq="MS")
    t = np.arange(periods)
    trend = 0.35 * t
    seasonal = 12 * np.sin(2 * np.pi * t / 12) + 4 * np.cos(2 * np.pi * t / 12)
    noise = rng.normal(0, 2.5, periods)
    return pd.Series(80 + trend + seasonal + noise, index=dates, name="synthetic_value")


def evaluate(actual: pd.Series, predicted: pd.Series, model_name: str) -> dict:
    aligned = pd.concat([actual.rename("actual"), predicted.rename("predicted")], axis=1).dropna()
    return {
        "Model": model_name,
        "MAE": mean_absolute_error(aligned["actual"], aligned["predicted"]),
        "RMSE": np.sqrt(mean_squared_error(aligned["actual"], aligned["predicted"])),
    }


def main() -> None:
    series = make_monthly_series()
    horizon = 12
    train, test = series.iloc[:-horizon], series.iloc[-horizon:]

    hw = ExponentialSmoothing(
        train, trend="add", seasonal="add", seasonal_periods=12,
        initialization_method="estimated",
    ).fit(optimized=True)
    hw_forecast = hw.forecast(horizon)
    hw_forecast.index = test.index

    sarimax = SARIMAX(
        train,
        order=(1, 1, 1),
        seasonal_order=(1, 1, 1, 12),
        enforce_stationarity=False,
        enforce_invertibility=False,
    ).fit(disp=False)
    sx_forecast = sarimax.get_forecast(steps=horizon).predicted_mean
    sx_forecast.index = test.index

    results = pd.DataFrame([
        evaluate(test, hw_forecast, "Holt-Winters additive"),
        evaluate(test, sx_forecast, "SARIMAX (1,1,1)x(1,1,1,12)"),
    ]).sort_values("RMSE")
    print(results.to_string(index=False, float_format=lambda x: f"{x:.3f}"))

    plt.figure(figsize=(11, 5))
    plt.plot(train.index, train, label="Training observations")
    plt.plot(test.index, test, label="Actual holdout", linewidth=2)
    plt.plot(hw_forecast.index, hw_forecast, label="Holt-Winters forecast")
    plt.plot(sx_forecast.index, sx_forecast, label="SARIMAX forecast")
    plt.title("Monthly synthetic series: 12-month holdout comparison")
    plt.xlabel("Month")
    plt.ylabel("Synthetic value")
    plt.legend()
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()
