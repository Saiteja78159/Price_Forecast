# import os
# import joblib
# import pandas as pd
# from django.http import JsonResponse

# BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# MODEL_PATH = os.path.join(BASE_DIR, "price_forecast_model.pkl")
# CSV_PATH = os.path.join(BASE_DIR, "price_data.csv")

# # Load model once when server starts
# model = joblib.load(MODEL_PATH)

# def predict_price(request):
#     # Load historical data
#     df = pd.read_csv(CSV_PATH)

#     df['date'] = pd.to_datetime(df['date'])
#     df.set_index('date', inplace=True)
#     df = df.asfreq('MS')

#     # Forecast next 12 months
#     forecast = model.get_forecast(steps=12)
#     predicted_prices = forecast.predicted_mean

#     response = {
#         "forecast": [
#             {"date": str(date.date()), "predicted_price": float(price)}
#             for date, price in predicted_prices.items()
#         ]
#     }

#     return JsonResponse(response)

import os
import joblib
import pandas as pd
from django.http import JsonResponse
from django.shortcuts import render

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

MODEL_PATH = os.path.join(BASE_DIR, "price_forecast_model.pkl")
CSV_PATH = os.path.join(BASE_DIR, "price_data.csv")

model = joblib.load(MODEL_PATH)

def predict_price(request):
    df = pd.read_csv(CSV_PATH)
    df['date'] = pd.to_datetime(df['date'])
    df.set_index('date', inplace=True)
    df = df.asfreq('MS')

    forecast = model.get_forecast(steps=12)
    predicted = forecast.predicted_mean

    data = [
        {"date": date.strftime("%Y-%m"), "price": round(price, 2)}
        for date, price in predicted.items()
    ]

    return JsonResponse({"forecast": data})


def home(request):
    df = pd.read_csv(CSV_PATH)
    df['date'] = pd.to_datetime(df['date'])
    df.set_index('date', inplace=True)
    df = df.asfreq('MS')

    forecast = model.get_forecast(steps=12)
    predicted = forecast.predicted_mean

    data = [
        {"date": date.strftime("%Y-%m"), "price": round(price, 2)}
        for date, price in predicted.items()
    ]

    return render(request, "forecast/home.html", {"forecast": data})
