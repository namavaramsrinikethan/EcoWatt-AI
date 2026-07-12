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

from src.analytics import energy_health_score

from src.bill_estimator import bill_summary

from src.recommendation import generate_recommendations

# Load dataset
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

future = create_future_dataframe(model)

forecast = predict_energy(
    model,
    future
)

# Analytics
health = energy_health_score(
    daily_df,
    forecast
)

# Bill
bill = bill_summary(
    health["predicted_average"],
    8.5
)

# Recommendations
cards = generate_recommendations(
    health,
    bill
)

print()

print("Recommendation Cards\n")

for card in cards:

    print("=" * 50)

    for key, value in card.items():

        print(f"{key}: {value}")

    print()