# Assignment 1 — Energy Demand Forecasting

**Level:** Intermediate. **Course alignment:** Time-Series Forecasting. **Domain link:** Electrical engineering, energy planning and operational analytics.

## Business scenario
An electricity distribution team needs a short-term demand forecast to plan staffing and operational reserves. You have historical daily demand observations and may have calendar and weather variables. Build and compare forecasting methods and explain their practical implications.

Use a permitted dataset with a clear unit and time frequency. If no suitable data are available, use a synthetic series and label it explicitly as synthetic.

## Tasks

### Part A — Data audit and exploration
1. Confirm timestamp frequency, duplicates, missing dates and missing values.
2. Plot the full time series and rolling mean.
3. Describe trend, seasonality, unusual events and possible structural breaks.
4. Examine autocorrelation and partial autocorrelation.
5. State whether daily, weekly or annual seasonality is plausible.

### Part B — Baselines and candidate models
Build at least four forecasts: (1) naive or seasonal-naive baseline; (2) exponential smoothing/Holt-Winters where appropriate; (3) Prophet with suitable seasonality; (4) SARIMAX, with stationarity and ACF/PACF diagnostics guiding a reasonable model.

Optional: include an external regressor such as temperature or holiday indicator. Only use regressors that would be known or forecasted at the time of the prediction.

### Part C — Validation
1. Use chronological train/validation/test data.
2. Do not randomly shuffle time-series observations.
3. Report MAE and RMSE; include MAPE only where actual values are non-zero and suitable.
4. Add rolling-origin evaluation where possible.
5. Inspect residual autocorrelation and prediction intervals.
6. Compare all candidates on the same forecast horizon.

### Part D — Operational interpretation
Translate forecasts into a planning recommendation. State how forecast error could affect reserve capacity, staffing, maintenance windows or procurement. Explain why the lowest historical RMSE is not automatically the best operational choice.

## Deliverables
- energy_forecasting.ipynb
- README describing the dataset and methods
- forecast_comparison.csv
- At least two figures
- 300–500 word management note
- Limitations section

## Assessment rubric (100 points)
| Area | Points |
|---|---:|
| Data audit and visual analysis | 15 |
| Baseline and candidate model implementation | 25 |
| Chronological validation and fair comparison | 25 |
| Residuals, uncertainty and diagnostics | 15 |
| Operational interpretation and limitations | 15 |
| Reproducibility and code quality | 5 |

Document the dataset source and licence. Keep synthetic and real data clearly distinguished. Do not invent forecast results or imply that model estimates are actual grid measurements.
