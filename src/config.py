"""
config.py

Central configuration file for EcoWatt AI.

Modify values here instead of
hardcoding them throughout the project.
"""

# ==========================
# Application
# ==========================

APP_NAME = "EcoWatt AI"

APP_VERSION = "1.0"

# ==========================
# Forecast
# ==========================

FORECAST_DAYS = 7

# ==========================
# Electricity
# ==========================

DEFAULT_TARIFF = 8.5

DEFAULT_CURRENCY = "₹"

# ==========================
# Model
# ==========================

MODEL_PATH = "models/prophet_model.pkl"

# ==========================
# Dataset
# ==========================

DATASET_PATH = "datasets/household_power_consumption.txt"