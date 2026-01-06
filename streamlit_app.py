import streamlit as st
import pandas as pd

from src.data_loader import load_use_case_data
from src.baseline import compute_baseline
from src.pipeline import run_pipeline

st.set_page_config(
    page_title="Agentic Loyalty Intelligence",
    layout="wide"
)

st.title("🧠 Agentic Loyalty Intelligence POC")
st.caption("Antavo-compatible | Supermarket & Fuel Loyalty")

# -------------------------------
# Sidebar
# -------------------------------
st.sidebar.header("Configuration")

use_case = st.sidebar.selectbox(
    "Select Use Case",
    ["supermarket", "fuel"]
)

customers, events, campaigns, sentiment = load_use_case_data(use_case)

customer_id = st.sidebar.selectbox(
    "Select Customer",
    customers["customer_id"].unique()
)

run_btn = st.sidebar.button("Run Loyalty Analysis")

# -------------------------------
# Main Logic
# -------------------------------
if run_btn:
    baseline = compute_baseline(events)

    is_high_value = customers.loc[
        customers["customer_id"] == customer_id,
        "is_high_value"
    ].iloc[0]

    result = run_pipeline(
        customer_id,
        use_case,
        events,
        sentiment,
        baseline,
        is_high_value
    )

    st.success("Analysis completed")

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("📊 Behavior Analysis")
        st.json(result["behavior"].dict())

        st.subheader("💬 Sentiment & Friction")
        st.json(result["sentiment"].dict())

    with col2:
        st.subheader("🧩 Root Cause Explanation")
        st.write(result["root_cause"].primary_cause)

        st.markdown("**Contributing Factors**")
        for f in result["root_cause"].contributing_factors:
            st.write("- ", f)

        st.markdown("**Evidence**")
        for e in result["root_cause"].evidence:
            st.write("- ", e)

        st.subheader("🎯 Recommended Action")
        st.json(result["recommendation"].dict())

else:
    st.info("Select a use case and customer, then click **Run Loyalty Analysis**")
