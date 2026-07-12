from src.data_loader import load_dataset

from src.preprocessing import (
    convert_numeric,
    create_datetime,
    remove_missing_values,
    aggregate_daily_data,
    calculate_daily_energy
)

from src.forecasting import (
    load_model,
    create_future_dataframe,
    predict_energy
)

from src.analytics import *

# Load data
df = load_dataset(
    "datasets/household_power_consumption.txt"
)

# Preprocessing
df = convert_numeric(df)

df = create_datetime(df)

df = remove_missing_values(df)

daily_df = aggregate_daily_data(df)

daily_df = calculate_daily_energy(daily_df)

# Forecast
model = load_model(
    "models/prophet_model.pkl"
)

future = create_future_dataframe(
    model
)

forecast = predict_energy(
    model,
    future
)

print("Average Daily Usage")

print(calculate_average_usage(daily_df))

print()

print("Highest Usage")

print(highest_usage_day(daily_df))

print()

print("Lowest Usage")

print(lowest_usage_day(daily_df))

print()

print("Forecast Average")

print(forecast_average(forecast))

print()

print("Energy Health Score")

health = energy_health_score(
    daily_df,
    forecast
)

print("\nEnergy Health Report\n")

for key, value in health.items():
    print(f"{key}: {value}")