import streamlit as st
import plotly.express as px


def historical_chart(daily_df):
    """
    Display historical daily energy consumption.
    """

    fig = px.line(
        daily_df,
        x=daily_df.index,
        y="Daily_Energy_kWh",
        title="Historical Daily Energy Consumption"
    )

    fig.update_layout(
        xaxis_title="Date",
        yaxis_title="Energy (kWh)",
        template="plotly_white"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )


def forecast_chart(forecast):
    """
    Display 7-day forecast.
    """

    future = forecast.tail(7)

    fig = px.line(
        future,
        x="ds",
        y="yhat",
        markers=True,
        title="7-Day Energy Consumption Forecast"
    )

    fig.update_layout(
        xaxis_title="Date",
        yaxis_title="Predicted Energy (kWh)",
        template="plotly_white"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )