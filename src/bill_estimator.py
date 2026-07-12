"""
bill_estimator.py

Estimate electricity bills
based on predicted energy
consumption.

Functions:
- Daily Cost
- Weekly Cost
- Monthly Cost
- Bill Summary
"""
import pandas as pd

def daily_cost(
    daily_energy,
    tariff_rate
):
    """
    Calculate daily electricity cost.
    """

    return round(
        daily_energy * tariff_rate,
        2
    )


def weekly_cost(
    predicted_average,
    tariff_rate
):
    """
    Calculate weekly electricity cost.
    """

    return round(
        predicted_average * 7 * tariff_rate,
        2
    )


def monthly_cost(
    predicted_average,
    tariff_rate
):
    """
    Calculate monthly electricity cost.
    """

    return round(
        predicted_average * 30 * tariff_rate,
        2
    )


def bill_summary(
    predicted_average,
    tariff_rate,
    currency="₹"
):
    """
    Return a complete bill summary.
    """

    daily = daily_cost(
        predicted_average,
        tariff_rate
    )

    weekly = weekly_cost(
        predicted_average,
        tariff_rate
    )

    monthly = monthly_cost(
        predicted_average,
        tariff_rate
    )

    return {
        "currency": currency,
        "daily_cost": daily,
        "weekly_cost": weekly,
        "monthly_cost": monthly,
        "tariff_rate": tariff_rate,
        "predicted_daily_energy": round(
            predicted_average,
            2
        )
    }