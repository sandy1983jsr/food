import streamlit as st
import pandas as pd
from utils.data_loader import load_csv
from sklearn.ensemble import IsolationForest
from prophet import Prophet
import numpy as np

def advanced_analytics_tab():
    st.header("Advanced Analytics for Dairy Operations")

    st.subheader("Anomaly Detection (Isolation Forest)")
    uploaded_file = st.file_uploader("Upload Energy Data for Anomaly Detection (.csv)", type="csv", key="ad1")
    if uploaded_file:
        df = load_csv(uploaded_file)
        if "Energy_kWh" in df.columns:
            model = IsolationForest(contamination=0.1)
            df['anomaly'] = model.fit_predict(df[['Energy_kWh']])
            st.write(df[["Timestamp", "Energy_kWh", "anomaly"]])
            st.write("Red rows indicate anomalies (-1).")
            st.dataframe(df[df['anomaly'] == -1], use_container_width=True)
        else:
            st.warning("Please upload a file with Energy_kWh column.")

    st.subheader("Energy Forecasting (Prophet)")
    uploaded_file2 = st.file_uploader("Upload Energy Data for Forecasting (.csv)", type="csv", key="ad2")
    if uploaded_file2:
        df = load_csv(uploaded_file2)
        if "Timestamp" in df.columns and "Energy_kWh" in df.columns:
            dfp = pd.DataFrame()
            dfp["ds"] = pd.to_datetime(df["Timestamp"])
            dfp["y"] = df["Energy_kWh"]
            m = Prophet()
            m.fit(dfp)
            future = m.make_future_dataframe(periods=24, freq='H')
            forecast = m.predict(future)
            st.line_chart(forecast.set_index("ds")["yhat"])
            st.write("Forecasted energy usage for next 24 hours.")
        else:
            st.warning("Please upload a file with Timestamp and Energy_kWh columns.")

    st.subheader("Process Benchmarking")
    uploaded_file3 = st.file_uploader("Upload Benchmark Data (.csv)", type="csv", key="ad3")
    if uploaded_file3:
        df = load_csv(uploaded_file3)
        st.write(df)
        # Assume you have column 'Energy_per_liter' and 'Industry_Benchmark'
        if "Energy_per_liter" in df.columns and "Industry_Benchmark" in df.columns:
            avg = df["Energy_per_liter"].mean()
            bench = df["Industry_Benchmark"].iloc[0]
            st.metric("Your avg energy/liter", avg)
            st.metric("Industry benchmark", bench)
            if avg > bench:
                st.warning("Your process is above industry benchmark. Opportunity for improvement!")
            else:
                st.success("Your process is efficient compared to benchmark.")

    st.subheader("Carbon Footprint Estimation")
    uploaded_file4 = st.file_uploader("Upload Energy Data for Carbon Footprint (.csv)", type="csv", key="ad4")
    if uploaded_file4:
        df = load_csv(uploaded_file4)
        # Assume grid emissions factor is 0.82 kgCO2/kWh
        if "Energy_kWh" in df.columns:
            total_energy = df["Energy_kWh"].sum()
            emissions = total_energy * 0.82
            st.metric("Estimated CO2 Emissions (kg)", emissions)
            st.write("Based on Indian grid average emission factor (source: CEA India).")
        else:
            st.warning("Please upload a file with Energy_kWh column.")

    st.subheader("Quality-Energy Correlation")
    uploaded_file5 = st.file_uploader("Upload Data for Quality-Energy Analysis (.csv)", type="csv", key="ad5")
    if uploaded_file5:
        df = load_csv(uploaded_file5)
        if "Energy_kWh" in df.columns and "Quality_Score" in df.columns:
            corr = df["Energy_kWh"].corr(df["Quality_Score"])
            st.metric("Correlation (Energy vs. Quality)", corr)
            if abs(corr) > 0.5:
                st.warning("Strong correlation detected. Investigate for root cause.")
            else:
                st.success("No strong correlation. Process energy and quality are independent.")
        else:
            st.warning("Please upload a file with Energy_kWh and Quality_Score columns.")
