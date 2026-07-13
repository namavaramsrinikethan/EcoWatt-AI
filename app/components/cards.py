import streamlit as st


def dashboard_cards(health, bill):
    """
    Display dashboard KPI cards.
    """

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "❤️ Energy Health",
            f"{health['score']}/100"
        )

    with col2:
        st.metric(
            "💰 Monthly Bill",
            f"₹{bill['monthly_cost']:.2f}"
        )

    with col3:
        st.metric(
            "⚡ Daily Usage",
            f"{health['historical_average']:.2f} kWh"
        )