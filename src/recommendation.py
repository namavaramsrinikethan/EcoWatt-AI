"""
recommendation.py

Generate intelligent energy-saving
recommendations based on analytics
and bill estimation.

Functions:
- Generate recommendation cards
"""
def generate_recommendations(
    health_report,
    bill_summary
):
    """
    Generate recommendation cards.

    Returns:
        list of dictionaries
    """

    recommendations = []

    score = health_report["score"]

    bill = bill_summary["monthly_cost"]

    difference = health_report["difference"]

    if score < 75:

        recommendations.append({

            "priority": "High",

            "category": "Energy Health",

            "title": "Higher than Normal Consumption",

            "description":
                health_report["message"],

            "action":
                "Monitor high-power appliances and reduce unnecessary usage."

        })

    if bill > 8000:

        recommendations.append({

            "priority": "High",

            "category": "Electricity Bill",

            "title": "High Monthly Bill Expected",

            "description":
                f"Estimated monthly bill is ₹{bill:.2f}.",

            "action":
                "Review appliance usage to reduce monthly expenses."

        })

    if difference > 2:

        recommendations.append({

            "priority": "Medium",

            "category": "Forecast",

            "title": "Increasing Energy Trend",

            "description":
                "Predicted energy usage is higher than your historical average.",

            "action":
                "Reduce usage during peak hours whenever possible."

        })

    if score >= 90:

        recommendations.append({

            "priority": "Low",

            "category": "Performance",

            "title": "Excellent Energy Management",

            "description":
                "Your predicted energy usage is close to your normal pattern.",

            "action":
                "Maintain your current energy-saving habits."

        })
    return recommendations