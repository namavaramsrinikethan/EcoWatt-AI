from src.data_loader import load_dataset
from src.preprocessing import (
    convert_numeric,
    create_datetime,
    remove_missing_values,
    aggregate_daily_data,
    calculate_daily_energy
)

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

print()

print("First Date :", daily_df.index.min())

print("Last Date :", daily_df.index.max())

print("Total Days :", len(daily_df))

print(daily_df.head())

print()

print("Shape:", daily_df.shape)