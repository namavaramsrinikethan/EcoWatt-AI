from src.bill_estimator import *

predicted_average = 32.86

tariff_rate = 8.5

summary = bill_summary(
    predicted_average,
    tariff_rate
)

print()

print("Electricity Bill Summary\n")

for key, value in summary.items():
    print(f"{key}: {value}")