"""
analytics.py

This module performs analytical calculations
for the EcoWatt AI dashboard.

Functions:
- Average daily usage
- Highest usage
- Lowest usage
- Weekly average
- Monthly average
- Forecast summary
- Energy Health Score
"""
import pandas as pd

def calculate_average_usage(daily_df):
    """
    Calculate average daily energy usage.
    """

    return daily_df["Daily_Energy_kWh"].mean()


def highest_usage_day(daily_df):
    """
    Find the day with the highest energy usage.
    """

    idx = daily_df["Daily_Energy_kWh"].idxmax()

    return (
        idx,
        daily_df.loc[idx, "Daily_Energy_kWh"]
    )


def lowest_usage_day(daily_df):
    """
    Find the day with the lowest energy usage.
    """

    idx = daily_df["Daily_Energy_kWh"].idxmin()

    return (
        idx,
        daily_df.loc[idx, "Daily_Energy_kWh"]
    )


def weekly_average(daily_df):
    """
    Calculate weekly average energy usage.
    """

    weekly = (
        daily_df["Daily_Energy_kWh"]
        .resample("W")
        .mean()
    )

    return weekly


def monthly_average(daily_df):
    """
    Calculate monthly average energy usage.
    """

    monthly = (
        daily_df["Daily_Energy_kWh"]
        .resample("M")
        .mean()
    )

    return monthly


def forecast_average(forecast):
    """
    Calculate average predicted energy.
    """

    return forecast.tail(7)["yhat"].mean()


def energy_health_score(daily_df, forecast):
    """
    Calculate personalized Energy Health Score.

    Returns:
        dict
    """

    historical_avg = daily_df["Daily_Energy_kWh"].mean()

    predicted_avg = forecast.tail(7)["yhat"].mean()

    difference = predicted_avg - historical_avg

    percentage = abs(difference) / historical_avg * 100

    score = max(0, min(100, 100 - percentage))

    # Health Status
    if score >= 90:
        status = "Excellent"
        color = "Green"

    elif score >= 75:
        status = "Good"
        color = "Light Green"

    elif score >= 60:
        status = "Needs Attention"
        color = "Orange"

    else:
        status = "Poor"
        color = "Red"

    # Personalized Message
    if difference < -2:
        message = (
            "Predicted consumption is lower than your historical average."
        )

    elif difference > 2:
        message = (
            "Predicted consumption is higher than your historical average."
        )

    else:
        message = (
            "Predicted consumption is close to your normal usage."
        )

    return {
        "score": round(score, 2),
        "status": status,
        "color": color,
        "historical_average": round(historical_avg, 2),
        "predicted_average": round(predicted_avg, 2),
        "difference": round(difference, 2),
        "message": message
    }