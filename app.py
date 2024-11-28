import streamlit as st
import pandas as pd
import altair as alt

# Page Configuration
st.set_page_config(page_title="Water Management Dashboard", layout="wide")

# Title
st.title("Water Management Dashboard")

# Create two columns
col1, col2 = st.columns([1, 2])  # Adjust column width ratio as [1, 2]

# --- Column 1: Chat with Chatbot ---
with col1:
    st.subheader("Chat with your Assistant")
    # Create a text input box for chat
    user_input = st.text_input("Ask...", key="chat_input")
    if user_input:
        st.write("You asked:", user_input)
        st.write("Bot's response: This is where the chatbot's answer will appear.")

# --- Column 2: Current Thresholds and Water Consumption ---
with col2:
    # Row 1: Current Month Thresholds
    st.subheader("January")
    # Replace with dynamic values if needed
    st.info("City Threshold: 10m³/p\n\nCurrent Threshold: 12m³")

    # Row 2: Previous Water Consumption Plot
    st.subheader("Water Consumption")
    # Example data for the chart
    data = pd.DataFrame({
        "Month": ["October", "November", "December"],
        "City Threshold": [10, 10, 10],
        "Your Threshold": [5, 12, 18],
    })
    # Create a bar chart
    chart = alt.Chart(data).transform_fold(
        fold=["City Threshold", "Your Threshold"],  # Columns to show
        as_=["Threshold Type", "Value"]            # Rename for display
    ).mark_bar().encode(
        x=alt.X("Month:N", title="Month"),
        y=alt.Y("Value:Q", title="Water Consumption (m³)"),
        # Explicitly define the data type for "Threshold Type"
        color=alt.Color("Threshold Type:N", title="Type"),
        # Explicitly define data types in the tooltip
        tooltip=["Month", "Threshold Type:N", "Value:Q"]
    ).properties(
        width="container",
        height=300
    )
    st.altair_chart(chart, use_container_width=True)
