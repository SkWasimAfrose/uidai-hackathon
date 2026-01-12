import streamlit as st
from utils.data_loader import load_multiple_csv
import pandas as pd

st.title("📌 Aadhaar Enrollment Analysis")

df = load_multiple_csv("data/enrolment")

# Convert date
df["date"] = pd.to_datetime(df["date"], format="mixed", dayfirst=True)

# Create total enrollment column
df["total_enrollment"] = (
    df["age_0_5"] + df["age_5_17"] + df["age_18_greater"]
)

st.success("Enrollment data loaded successfully")

st.markdown("### Key Enrollment Metrics")

col1, col2, col3, col4 = st.columns(4)

col1.metric(
    label="Total Enrollments",
    value=f"{df['total_enrollment'].sum():,}"
)

col2.metric(
    label="States Covered",
    value=df["state"].nunique()
)

col3.metric(
    label="Districts Covered",
    value=df["district"].nunique()
)

peak_date = (
    df.groupby("date")["total_enrollment"]
    .sum()
    .idxmax()
)

col4.metric(
    label="Peak Enrollment Date",
    value=peak_date.strftime("%d %b %Y")
)


st.divider()

st.markdown("#### State-wise Enrollment Distribution")
st.caption("Aggregated Aadhaar enrollments across states highlight regional coverage disparities.")

state_data = (
    df.groupby("state")["total_enrollment"]
    .sum()
    .sort_values(ascending=False)
    .reset_index()
)

st.bar_chart(state_data.set_index("state"))



st.divider()

st.markdown("#### 📈 Age-group Trend Analysis")
st.caption("Longitudinal tracking of enrollment figures across demographic age brackets.")

trend_df = (
    df.groupby("date")[["age_0_5", "age_5_17", "age_18_greater"]]
    .sum()
    .reset_index()
    .sort_values("date")
)

st.line_chart(
    trend_df.set_index("date")
)




st.divider()

st.markdown("#### 🚨 Enrollment Anomaly Detection")
st.caption("Statistical identification of daily enrollment outliers using standard deviation thresholds.")

daily_enrollment = (
    df.groupby("date")["total_enrollment"]
    .sum()
    .reset_index()
    .sort_values("date")
)

mean_val = daily_enrollment["total_enrollment"].mean()
std_val = daily_enrollment["total_enrollment"].std()

daily_enrollment["anomaly"] = (
    (daily_enrollment["total_enrollment"] > mean_val + 2 * std_val) |
    (daily_enrollment["total_enrollment"] < mean_val - 2 * std_val)
)

anomalies = daily_enrollment[daily_enrollment["anomaly"]]

st.line_chart(
    daily_enrollment.set_index("date")["total_enrollment"]
)


st.write("🔴 Detected Anomalies")
st.dataframe(
    anomalies,
    use_container_width=True,
    hide_index=True
)



st.divider()

st.markdown("#### 📍 District-level High Volume Areas")
st.caption("Listing top-performing districts based on cumulative enrollment data.")

district_data = (
    df.groupby(["state", "district"])["total_enrollment"]
    .sum()
    .reset_index()
    .sort_values("total_enrollment", ascending=False)
)

st.dataframe(
    district_data.head(20),
    use_container_width=True,
    hide_index=True
)


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
