from src.forecasting import (
    load_model,
    create_future_dataframe,
    predict_energy
)

# Load model
model = load_model(
    "models/prophet_model.pkl"
)

# Create future dates
future = create_future_dataframe(
    model,
    periods=7
)

# Forecast
forecast = predict_energy(
    model,
    future
)

print(
    forecast[
        ["ds","yhat","yhat_lower","yhat_upper"]
    ].tail(7)
)