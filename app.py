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
