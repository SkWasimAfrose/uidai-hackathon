import streamlit as st

st.set_page_config(
    page_title="UIDAI Aadhaar Insights Dashboard",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.title("📊 UIDAI Aadhaar Insights Dashboard")

st.markdown("""
This dashboard analyzes Aadhaar **Enrollment**, **Demographic Updates**,  
and **Biometric Updates** to uncover societal trends and anomalies.
""")

st.info("Use the sidebar to navigate between analysis pages.")
