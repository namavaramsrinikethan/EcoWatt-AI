import streamlit as st

from src.config import APP_NAME

st.set_page_config(
    page_title=APP_NAME,
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.title("⚡ EcoWatt AI")

st.markdown("---")

st.write(
    """
Welcome to **EcoWatt AI**.

An intelligent energy consumption forecasting
system powered by Machine Learning.

This application can:

- 📈 Predict household energy usage
- 💰 Estimate electricity bills
- ❤️ Calculate Energy Health Score
- 💡 Generate intelligent recommendations
"""
)

st.success("Backend Connected Successfully ✅")