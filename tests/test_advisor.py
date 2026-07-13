from src.analytics import energy_health_score
from src.bill_estimator import bill_summary
from src.advisor import generate_advisor_report

import pandas as pd


daily_df = pd.DataFrame({
    "Daily_Energy_kWh": [20, 25, 24, 28, 30, 29]
})

forecast = pd.DataFrame({
    "yhat": [32, 33, 34, 31, 35, 33, 32]
})

health = energy_health_score(
    daily_df,
    forecast
)

bill = bill_summary(
    health["predicted_average"],
    8.5
)

advisor = generate_advisor_report(
    health,
    bill
)

print("\nAI Energy Advisor Report\n")

for section, value in advisor.items():

    print("=" * 50)

    print(section)

    print(value)