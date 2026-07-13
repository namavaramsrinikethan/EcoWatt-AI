import streamlit as st


def advisor_dashboard(advisor):
    """
    Display AI Energy Advisor.
    """

    st.header("🧠 AI Energy Advisor")

    # ------------------------------------

    st.subheader("📄 Executive Summary")

    st.write(
        advisor["executive_summary"]
    )

    # ------------------------------------

    st.subheader("📊 Consumption Analysis")

    analysis = advisor["consumption_analysis"]

    st.table({

        "Metric": [

            "Historical Average",

            "Forecast Average",

            "Difference",

            "Increase (%)"

        ],

        "Value": [

            f"{analysis['historical_average']:.2f} kWh",

            f"{analysis['forecast_average']:.2f} kWh",

            f"{analysis['difference']:.2f} kWh",

            f"{analysis['increase_percentage']:.2f}%"

        ]

    })

    # ------------------------------------

    st.subheader("💰 Financial Impact")

    finance = advisor["financial_impact"]

    col1, col2 = st.columns(2)

    with col1:

        st.metric(
            "Monthly Bill",
            f"₹{finance['monthly_bill']:.2f}"
        )

    with col2:

        st.metric(
            "Additional Cost",
            f"₹{finance['additional_cost']:.2f}"
        )

    # ------------------------------------

    st.subheader("⚠ Risk Assessment")

    st.warning(
        advisor["risk_level"]
    )

    # ------------------------------------

    st.subheader("⭐ Efficiency Rating")

    st.success(
        advisor["efficiency_rating"]
    )

    # ------------------------------------

    st.subheader("📈 Trend")

    st.info(
        advisor["trend"]
    )

    # ------------------------------------

    st.subheader("✅ Suggested Actions")

    for action in advisor["suggested_actions"]:

        st.write(f"• {action}")

    # ------------------------------------

    st.subheader("💵 Potential Savings")

    st.success(
        f"₹{advisor['potential_savings']:.2f} per month"
    )

    # ------------------------------------

    st.subheader("🔮 Future Outlook")

    st.write(
        advisor["future_outlook"]
    )