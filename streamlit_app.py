import streamlit as st
from app.components.advisor import advisor_dashboard
from src.config import (
    APP_NAME,
    DATASET_PATH,
    MODEL_PATH,
    DEFAULT_TARIFF
)

from src.pipeline import run_pipeline

from app.components.cards import dashboard_cards
from app.components.bill import bill_breakdown
from app.components.charts import (
    historical_chart,
    forecast_chart
)

# =====================================================
# PAGE CONFIG
# =====================================================

st.set_page_config(
    page_title=APP_NAME,
    page_icon="⚡",
    layout="wide"
)

# =====================================================
# HEADER
# =====================================================

st.title("⚡ EcoWatt AI")

st.write("""
Welcome to **EcoWatt AI**.

An AI-powered platform that predicts household energy
consumption, estimates electricity bills, analyzes usage
patterns, and provides intelligent energy insights.
""")

st.success("Backend Ready ✅")

# =====================================================
# RUN ANALYSIS
# =====================================================

if st.button("🚀 Run Analysis", use_container_width=True):

    with st.spinner("Analyzing household energy consumption..."):

        results = run_pipeline(
            DATASET_PATH,
            MODEL_PATH,
            DEFAULT_TARIFF
        )

    st.success("Analysis Completed Successfully!")

    health = results["health"]
    bill = results["bill"]

    # =====================================================
    # KEY METRICS
    # =====================================================

    st.markdown("---")
    st.header("📊 Key Metrics")

    dashboard_cards(
        health,
        bill
    )

    # =====================================================
    # HISTORICAL CONSUMPTION
    # =====================================================

    st.markdown("---")
    st.subheader("📈 Historical Energy Consumption")

    historical_chart(
        results["daily_data"]
    )

    # =====================================================
    # FORECAST
    # =====================================================

    st.markdown("---")
    st.subheader("🔮 7-Day Forecast")

    forecast_chart(
        results["forecast"]
    )

    # =====================================================
    # BILL BREAKDOWN
    # =====================================================

    st.markdown("---")

    bill_breakdown(
        bill
    )

    # =====================================================
    # ENERGY STATUS
    # =====================================================

    st.markdown("---")

    st.subheader("📋 Energy Status")

    st.info(
        f"""
**Status:** {health['status']}

**Analysis:** {health['message']}
"""
    )

    # =====================================================
    # AI ENERGY ADVISOR (TEMPORARY)
    # =====================================================

    st.markdown("---")

    advisor_dashboard(
        results["advisor"]
    )