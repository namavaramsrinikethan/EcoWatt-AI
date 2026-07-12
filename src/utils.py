"""
utils.py

Common helper functions used across
EcoWatt AI.
"""

from datetime import datetime


def format_currency(amount, currency="₹"):
    """
    Format currency value.
    """

    return f"{currency}{amount:,.2f}"


def format_energy(value):
    """
    Format energy value.
    """

    return f"{value:.2f} kWh"


def format_percentage(value):
    """
    Format percentage.
    """

    return f"{value:.2f}%"


def current_timestamp():
    """
    Return current date and time.
    """

    return datetime.now().strftime(
        "%d-%m-%Y %H:%M:%S"
    )


def health_icon(status):
    """
    Return an icon based on health status.
    """

    icons = {
        "Excellent": "🟢",
        "Good": "🟢",
        "Needs Attention": "🟠",
        "Poor": "🔴"
    }

    return icons.get(status, "⚪")