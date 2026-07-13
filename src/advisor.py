"""
advisor.py

AI Energy Advisor

Transforms energy analytics into
actionable intelligence.
"""


def calculate_trend(increase_percentage):
    """
    Determine energy trend.
    """

    if increase_percentage > 15:
        return "Increasing"

    elif increase_percentage < -10:
        return "Decreasing"

    return "Stable"


def calculate_risk(increase_percentage):

    if increase_percentage >= 25:
        return "High"

    elif increase_percentage >= 10:
        return "Medium"

    return "Low"


def calculate_efficiency(score):
    """
    Convert health score into
    user-friendly efficiency rating.
    """

    if score >= 90:
        return "★★★★★ Excellent"

    elif score >= 80:
        return "★★★★☆ Very Good"

    elif score >= 70:
        return "★★★☆☆ Good"

    elif score >= 60:
        return "★★☆☆☆ Fair"

    return "★☆☆☆☆ Poor"


def calculate_financial_impact(
    difference,
    tariff
):
    """
    Calculate additional monthly cost.
    """

    return round(
        difference * 30 * tariff,
        2
    )


def generate_summary(
    historical,
    predicted,
    increase,
    bill,
    score
):
    """
    Generate executive summary.
    """

    return (
        f"Your household is forecast to consume "
        f"{predicted:.2f} kWh/day over the next week. "
        f"This is {increase:.2f}% higher than your "
        f"historical average of {historical:.2f} kWh/day. "
        f"The estimated monthly electricity bill is "
        f"₹{bill:.2f}. "
        f"Your Energy Health Score is {score:.2f}/100."
    )


def generate_advisor_report(
    health,
    bill
):
    """
    Build AI Energy Advisor report.
    """

    historical = health["historical_average"]

    predicted = health["predicted_average"]

    score = health["score"]

    difference = round(
        predicted - historical,
        2
    )

    increase = round(
        (difference / historical) * 100,
        2
    )

    trend = calculate_trend(
        increase
    )

    risk = calculate_risk(
        increase
    )

    efficiency = calculate_efficiency(
        score
    )

    additional_cost = calculate_financial_impact(
        difference,
        bill["tariff_rate"]
    )

    potential_savings = round(
        3 * 30 * bill["tariff_rate"],
        2
    )

    report = {

        "executive_summary":
            generate_summary(
                historical,
                predicted,
                increase,
                bill["monthly_cost"],
                score
            ),

        "consumption_analysis": {

            "historical_average": historical,

            "forecast_average": predicted,

            "difference": difference,

            "increase_percentage": increase

        },

        "financial_impact": {

            "monthly_bill":
                bill["monthly_cost"],

            "additional_cost":
                additional_cost

        },

        "risk_level":
            risk,

        "efficiency_rating":
            efficiency,

        "trend":
            trend,

        "suggested_actions": [

            "Reduce air-conditioner usage during peak hours.",

            "Operate heavy appliances during off-peak periods.",

            "Turn off appliances on standby.",

            "Monitor water heater usage."

        ],

        "potential_savings":
            potential_savings,

        "future_outlook":
            "If this trend continues, electricity costs are expected to remain above your historical average."

    }

    return report