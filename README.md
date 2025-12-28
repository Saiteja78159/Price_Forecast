# 📈 Monthly Price Forecasting – Django Application

## 📝 Project Overview
This project forecasts **average monthly prices for the next 12 months** using historical price data.  
The application is built with a **SARIMA time-series model** for forecasting and deployed using **Django**. Users can access predictions via a **REST API** and a **web interface**.

---

## 📊 Dataset
- The dataset is provided as a CSV file: `price_data.csv`
- Contains historical monthly prices with the following columns:
  - `date` – Month of the record (`YYYY-MM-DD`)
  - `avg_monthly_price` – Average price for that month
- Example data:

| date       | avg_monthly_price |
|------------|-----------------|
| 2024-01-01 | 12000           |
| 2024-02-01 | 12350           |
| …          | …               |

---

## 🧠 Model Details
- **Model Type:** SARIMA (Seasonal ARIMA)
- **Reason for Choice:**
  - Handles trend and seasonality in time series
  - Works well with limited historical data
  - Statistically interpretable
- **Evaluation Metrics on Test Set:**
  - MAE, RMSE, MAPE
  - The model provides accurate forecasts for the next 12 months

---

## 🖥 Web Interface

The Django app provides a **simple UI** displaying the 12-month forecast.

### Example Output
<img width="1304" height="856" alt="image" src="https://github.com/user-attachments/assets/c1e272de-bbda-44a3-a8fb-05d12594dce0" />


- **Columns:**  
  - Month  
  - Predicted Price  
- Footer: SARIMA-based Price Forecasting Model

---

## 🔗 REST API Endpoint

**GET** `/predict/`

Returns the forecasted prices in JSON format:

```json
{
  "forecast": [
    {"date": "2025-10", "predicted_price": 15359.72},
    {"date": "2025-11", "predicted_price": 15541.64},
    {"date": "2025-12", "predicted_price": 16167.75},
    ...
  ]
}
