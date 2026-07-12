from src.data_loader import load_dataset, display_dataset_info

# Load dataset
df = load_dataset("datasets/household_power_consumption.txt")

# Display information
info = display_dataset_info(df)

print(info)