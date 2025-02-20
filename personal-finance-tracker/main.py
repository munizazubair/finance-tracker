import streamlit as st
import plotly.express as px
from io import BytesIO

st.title("📊 Personal Finance Tracker")

income = st.number_input("Enter your Monthly Income:", min_value=0.0)
expense = st.number_input("Enter your Monthly Expense:", min_value=0.0)

if st.button("Calculate Savings"):
    savings = income - expense
    st.write(f"💰 Your Monthly Savings: **{savings}**")

    # Create bar chart using Plotly
    fig = px.bar(
        x=["Income", "Expense", "Savings"],
        y=[income, expense, savings],
        labels={"x": "Category", "y": "Amount"},
        title="Income vs Expense vs Savings"
    )
    st.plotly_chart(fig)

    # Save the chart as an interactive HTML file (alternative method)
    img_bytes = BytesIO()
    img_bytes.write(fig.to_html().encode("utf-8"))
    img_bytes.seek(0)

    # Add a download button for the HTML file
    st.download_button(
        label="📥 Download Graph",
        data=img_bytes,
        file_name="finance_chart.html",
        mime="text/html"
    )
