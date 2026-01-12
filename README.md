# UIDAI Aadhaar Insights Dashboard

## Overview

This project is developed as part of the **UIDAI Data Hackathon 2026**.  
It transforms Aadhaar enrollment and update datasets into an interactive analytics dashboard to uncover societal trends, age-based behavior, and operational anomalies.

The dashboard is designed to support **data-driven decision-making** by presenting clear insights through visual analytics.

---

## Features

- State-wise and district-wise Aadhaar enrollment analysis
- Age-group enrollment trends (0–5, 5–17, 18+)
- Statistical anomaly detection in enrollment activity
- Demographic update trend analysis (age-based)
- Biometric update analysis highlighting life-stage patterns
- KPI metrics for quick executive-level understanding
- Clean, light-themed, professional dashboard UI

---

## Datasets Used

- Aadhaar Enrollment Dataset
- Aadhaar Demographic Update Dataset
- Aadhaar Biometric Update Dataset

_(Datasets are provided by UIDAI for hackathon use and are not included in this repository.)_

---

## Tech Stack

- Python
- Pandas
- Streamlit
- Plotly

---

## Project Structure

uidai-hackathon/
│
├── app.py
├── pages/
│ ├── 1_Enrollment_Analysis.py
│ ├── 2_Demographic_Updates.py
│ └── 3_Biometric_Updates.py
│
├── utils/
│ └── data_loader.py
│
├── data/
│ ├── enrolment/
│ ├── demographic/
│ └── biometric/
│
└── README.md

---

## How to Run Locally

1. Clone the repository
2. Create and activate a virtual environment
3. Install dependencies: pip install streamlit pandas plotly numpy
4. Run the app: streamlit run app.py

---

## Purpose

This project demonstrates how large-scale public datasets can be converted into actionable insights for governance, policy planning, and operational monitoring.

---

## Author

**SK Wasim Afrose**  
BCA – 3rd Year  
Solo Participant
