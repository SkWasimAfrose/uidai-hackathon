import streamlit as st
from utils.data_loader import load_multiple_csv
import pandas as pd

st.title("🧾 Aadhaar Demographic Update Analysis")

df = load_multiple_csv("data/demographic")

df["date"] = pd.to_datetime(df["date"], format="mixed", dayfirst=True)

st.success("Demographic update data loaded")

st.markdown("### Key Demographic Update Metrics")

col1, col2, col3 = st.columns(3)

total_updates = (df["demo_age_5_17"] + df["demo_age_17_"]).sum()

col1.metric(
    label="Total Demographic Updates",
    value=f"{total_updates:,}"
)

col2.metric(
    label="States Covered",
    value=df["state"].nunique()
)

peak_date = (
    df.assign(total_demo=df["demo_age_5_17"] + df["demo_age_17_"])
      .groupby("date")["total_demo"]
      .sum()
      .idxmax()
)

col3.metric(
    label="Peak Update Date",
    value=peak_date.strftime("%d %b %Y")
)

st.divider()

st.subheader("Available Demographic Update Types")

update_cols = [col for col in df.columns if col not in ["date", "state", "district", "pincode"]]
st.caption("Available columns used for analysis.")

st.subheader("Total Demographic Updates Over Time")

df["total_demo_updates"] = df["demo_age_5_17"] + df["demo_age_17_"]

trend = (
    df.groupby("date")["total_demo_updates"]
    .sum()
    .reset_index()
    .sort_values("date")
)

st.line_chart(trend.set_index("date"))
st.caption("This chart shows the trend of total demographic updates over time.")


st.subheader("Age-wise Demographic Update Comparison")

age_data = (
    df[["demo_age_5_17", "demo_age_17_"]]
    .sum()
    .reset_index()
)

age_data.columns = ["Age Group", "Total Updates"]

st.bar_chart(age_data.set_index("Age Group"))
st.caption("Comparison of update volumes between different age demographics.")
