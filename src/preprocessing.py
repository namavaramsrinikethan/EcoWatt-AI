"""
preprocessing.py

This module performs all preprocessing operations
required before forecasting.

Functions:
- Convert numeric columns
- Create Datetime column
- Remove missing values
- Aggregate daily data
- Calculate Daily Energy
"""

import pandas as pd


def convert_numeric(df):
    """
    Convert numeric columns to float.

    Parameters:
        df (DataFrame)

    Returns:
        DataFrame
    """

    numeric_columns = [
        "Global_active_power",
        "Global_reactive_power",
        "Voltage",
        "Global_intensity",
        "Sub_metering_1",
        "Sub_metering_2",
        "Sub_metering_3"
    ]

    for column in numeric_columns:
        df[column] = pd.to_numeric(
            df[column],
            errors="coerce"
        )

    return df


def create_datetime(df):
    """
    Create Datetime column.

    Parameters:
        df (DataFrame)

    Returns:
        DataFrame
    """

    df["Datetime"] = pd.to_datetime(
        df["Date"] + " " + df["Time"],
        dayfirst=True
    )

    return df


def remove_missing_values(df):
    """
    Remove rows containing missing values.

    Parameters:
        df (DataFrame)

    Returns:
        DataFrame
    """

    df = df.dropna()

    return df


def aggregate_daily_data(df):
    """
    Aggregate minute-level data into daily data.

    Parameters:
        df (DataFrame)

    Returns:
        DataFrame
    """

    daily_df = df.groupby(
        df["Datetime"].dt.date
    ).agg({
        "Global_active_power": "sum",
        "Global_reactive_power": "sum",
        "Voltage": "mean",
        "Global_intensity": "mean",
        "Sub_metering_1": "sum",
        "Sub_metering_2": "sum",
        "Sub_metering_3": "sum"
    })

    daily_df.index = pd.to_datetime(daily_df.index)

    daily_df.index.name = "Datetime"

    return daily_df


def calculate_daily_energy(daily_df):
    """
    Calculate Daily Energy Consumption.

    Parameters:
        daily_df (DataFrame)

    Returns:
        DataFrame
    """

    daily_df["Daily_Energy_kWh"] = (
        daily_df["Global_active_power"] / 60
    )

    return daily_df