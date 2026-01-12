import streamlit as st
from utils.data_loader import load_multiple_csv
import pandas as pd

st.title("🧬 Aadhaar Biometric Update Analysis")

df = load_multiple_csv("data/biometric")

df["date"] = pd.to_datetime(df["date"], format="mixed", dayfirst=True)

st.success("Biometric update data loaded")

st.markdown("### Key Biometric Update Metrics")

col1, col2, col3 = st.columns(3)

total_bio = (df["bio_age_5_17"] + df["bio_age_17_"]).sum()

col1.metric(
    label="Total Biometric Updates",
    value=f"{total_bio:,}"
)

col2.metric(
    label="States Covered",
    value=df["state"].nunique()
)

peak_date = (
    df.assign(total_bio=df["bio_age_5_17"] + df["bio_age_17_"])
      .groupby("date")["total_bio"]
      .sum()
      .idxmax()
)

col3.metric(
    label="Peak Update Date",
    value=peak_date.strftime("%d %b %Y")
)

st.divider()

st.subheader("Available Biometric Update Columns")

bio_cols = [col for col in df.columns if col not in ["date", "state", "district", "pincode"]]
st.caption("Available columns used for biometric analysis.")


st.subheader("Total Biometric Updates Over Time")

df["total_bio_updates"] = df["bio_age_5_17"] + df["bio_age_17_"]

trend = (
    df.groupby("date")["total_bio_updates"]
    .sum()
    .reset_index()
    .sort_values("date")
)

st.line_chart(trend.set_index("date"))
st.caption("This chart tracks the timeline of biometric updates.")


st.subheader("Age-wise Biometric Update Comparison")

age_bio = (
    df[["bio_age_5_17", "bio_age_17_"]]
    .sum()
    .reset_index()
)

age_bio.columns = ["Age Group", "Total Updates"]

st.bar_chart(age_bio.set_index("Age Group"))
st.caption("Comparison of biometric update counts across age groups.")


st.markdown(
    """
    <hr style="margin-top: 50px;">
    <div style="text-align: center; font-size: 12px; color: #6c757d;">
        Built by <a href="https://whoiswasim.vercel.app/" target="_blank"
        style="text-decoration: none; color: #0d6efd;">
        SK Wasim Afrose</a>
    </div>
    """,
    unsafe_allow_html=True
)
