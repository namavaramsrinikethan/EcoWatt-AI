"""
pipeline.py

Main orchestration module for EcoWatt AI.

Runs the complete pipeline.
"""

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

from src.analytics import (
    energy_health_score
)

from src.bill_estimator import (
    bill_summary
)

from src.recommendation import (
    generate_recommendations
)

from src.advisor import generate_advisor_report
def run_pipeline(
    dataset_path,
    model_path,
    tariff_rate=8.5
):
    df = load_dataset(dataset_path)

    df = convert_numeric(df)

    df = create_datetime(df)

    df = remove_missing_values(df)

    daily_df = aggregate_daily_data(df)

    daily_df = calculate_daily_energy(daily_df)

    model = load_model(model_path)

    future = create_future_dataframe(model)

    forecast = predict_energy(model, future)

    health = energy_health_score(
        daily_df,
        forecast
    )

    bill = bill_summary(
        health["predicted_average"],
        tariff_rate
    )

    advisor = generate_advisor_report(
        health,
        bill
    )

    recommendations = generate_recommendations(
        health,
        bill
    )

    print("✅ Pipeline Complete")

    return {
        "daily_data": daily_df,
        "forecast": forecast,
        "health": health,
        "bill": bill,
        "advisor": advisor,
        "recommendations": recommendations,
    }
    