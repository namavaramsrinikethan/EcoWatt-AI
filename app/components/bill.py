import streamlit as st


def bill_breakdown(bill):
    """
    Display electricity bill summary.
    """

    st.subheader("💰 Electricity Bill Breakdown")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "Daily",
            f"₹{bill['daily_cost']:.2f}"
        )

    with col2:
        st.metric(
            "Weekly",
            f"₹{bill['weekly_cost']:.2f}"
        )

    with col3:
        st.metric(
            "Monthly",
            f"₹{bill['monthly_cost']:.2f}"
        )