"""
forecasting.py

This module performs forecasting using the
trained Prophet model.

Functions:
- Load saved model
- Generate future dates
- Predict future energy consumption
"""

import os
import joblib


def load_model(model_path):
    """
    Load the trained Prophet model.

    Parameters:
        model_path (str)

    Returns:
        Prophet Model
    """

    if not os.path.exists(model_path):
        raise FileNotFoundError(
            f"Model not found: {model_path}"
        )

    model = joblib.load(model_path)

    return model


def create_future_dataframe(
    model,
    periods=7
):
    """
    Create future dates.

    Parameters:
        model
        periods

    Returns:
        DataFrame
    """

    future = model.make_future_dataframe(
        periods=periods,
        freq="D"
    )

    return future


def predict_energy(
    model,
    future
):
    """
    Generate energy forecast.

    Parameters:
        model
        future dataframe

    Returns:
        forecast dataframe
    """

    forecast = model.predict(
        future
    )

    return forecast