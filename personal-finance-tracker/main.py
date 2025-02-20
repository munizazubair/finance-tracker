import streamlit as st
import matplotlib.pyplot as plt
from io import BytesIO

st.title("📊 Personal Finance Tracker")

# create input fields for monthly income and expense
income = st.number_input("Enter your Monthly Income:", min_value=0.0)
expense = st.number_input("Enter your Monthly Expense:", min_value=0.0)

if st.button("Calculate Savings"):
    # calculate savings directly
    savings = income - expense

    # display the calculated savings
    st.write(f"💰 Your Monthly Savings: **{savings}**")

    # create a bar chart to visualize income, expense, and savings
    fig, ax = plt.subplots()
    ax.bar(["Income", "Expense", "Savings"], [income, expense, savings], color=["green", "red", "blue"])
    ax.set_title("Income vs Expense vs Savings")
    st.pyplot(fig)

    # save the chart as a PNG image in memory
    img_bytes = BytesIO()
    fig.savefig(img_bytes, format="png")
    img_bytes.seek(0)

    # add a download button for the chart
    st.download_button(
        label="📥 Download Graph",
        data=img_bytes,
        file_name="finance_chart.png",
        mime="image/png"
    )
