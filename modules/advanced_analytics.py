import streamlit as st
import pandas as pd
from utils.data_loader import load_csv
from sklearn.ensemble import IsolationForest
from prophet import Prophet
import numpy as np
import os

def get_data(uploaded_file, sample_path):
    if uploaded_file is not None:
        return load_csv(uploaded_file)
    elif os.path.exists(sample_path):
        return load_csv(sample_path)
    else:
        return None

def advanced_analytics_tab():
    st.header("Advanced Analytics for Dairy Operations")

    # ---- Anomaly Detection ----
    st.subheader("Anomaly Detection (Isolation Forest)")
    uploaded_file = st.file_uploader(
        "Upload Energy Data for Anomaly Detection (.csv) or use sample data", type="csv", key="ad1"
    )
    df_anomaly = get_data(uploaded_file, "data/sample/advanced_anomaly.csv")
    if df_anomaly is not None and "Energy_kWh" in df_anomaly.columns:
        model = IsolationForest(contamination=0.1)
        df_anomaly['anomaly'] = model.fit_predict(df_anomaly[['Energy_kWh']])
        st.write(df_anomaly[["Timestamp", "Energy_kWh", "anomaly"]])
        st.write("Red rows indicate anomalies (-1).")
        st.dataframe(df_anomaly[df_anomaly['anomaly'] == -1], use_container_width=True)
    elif uploaded_file:
        st.warning("File must have 'Energy_kWh' column.")
    else:
        st.info("Using sample data. Upload your CSV to override.")

    # ---- Energy Forecasting ----
    st.subheader("Energy Forecasting (Prophet)")
    uploaded_file2 = st.file_uploader(
        "Upload Energy Data for Forecasting (.csv) or use sample data", type="csv", key="ad2"
    )
    df_forecast = get_data(uploaded_file2, "data/sample/advanced_forecast.csv")
    if df_forecast is not None and "Timestamp" in df_forecast.columns and "Energy_kWh" in df_forecast.columns:
        dfp = pd.DataFrame()
        dfp["ds"] = pd.to_datetime(df_forecast["Timestamp"])
        dfp["y"] = df_forecast["Energy_kWh"]
        m = Prophet()
        m.fit(dfp)
        future = m.make_future_dataframe(periods=24, freq='H')
        forecast = m.predict(future)
        st.line_chart(forecast.set_index("ds")["yhat"])
        st.write("Forecasted energy usage for next 24 hours.")
    elif uploaded_file2:
        st.warning("File must have 'Timestamp' and 'Energy_kWh' columns.")
    else:
        st.info("Using sample data. Upload your CSV to override.")

    # ---- Process Benchmarking ----
    st.subheader("Process Benchmarking")
    uploaded_file3 = st.file_uploader(
        "Upload Benchmark Data (.csv) or use sample data", type="csv", key="ad3"
    )
    df_bench = get_data(uploaded_file3, "data/sample/advanced_benchmark.csv")
    if df_bench is not None and "Energy_per_liter" in df_bench.columns and "Industry_Benchmark" in df_bench.columns:
        avg = df_bench["Energy_per_liter"].mean()
        bench = df_bench["Industry_Benchmark"].iloc[0]
        st.metric("Your avg energy/liter", avg)
        st.metric("Industry benchmark", bench)
        st.dataframe(df_bench)
        if avg > bench:
            st.warning("Your process is above industry benchmark. Opportunity for improvement!")
        else:
            st.success("Your process is efficient compared to benchmark.")
    elif uploaded_file3:
        st.warning("File must have 'Energy_per_liter' and 'Industry_Benchmark' columns.")
    else:
        st.info("Using sample data. Upload your CSV to override.")

    # ---- Carbon Footprint Estimation ----
    st.subheader("Carbon Footprint Estimation")
    uploaded_file4 = st.file_uploader(
        "Upload Energy Data for Carbon Footprint (.csv) or use sample data", type="csv", key="ad4"
    )
    df_carbon = get_data(uploaded_file4, "data/sample/advanced_carbon.csv")
    if df_carbon is not None and "Energy_kWh" in df_carbon.columns:
        total_energy = df_carbon["Energy_kWh"].sum()
        emissions = total_energy * 0.82
        st.metric("Estimated CO2 Emissions (kg)", emissions)
        st.write("Based on Indian grid average emission factor (source: CEA India).")
    elif uploaded_file4:
        st.warning("File must have 'Energy_kWh' column.")
    else:
        st.info("Using sample data. Upload your CSV to override.")

    # ---- Quality-Energy Correlation ----
    st.subheader("Quality-Energy Correlation")
    uploaded_file5 = st.file_uploader(
        "Upload Data for Quality-Energy Analysis (.csv) or use sample data", type="csv", key="ad5"
    )
    df_quality = get_data(uploaded_file5, "data/sample/advanced_quality.csv")
    if df_quality is not None and "Energy_kWh" in df_quality.columns and "Quality_Score" in df_quality.columns:
        corr = df_quality["Energy_kWh"].corr(df_quality["Quality_Score"])
        st.metric("Correlation (Energy vs. Quality)", corr)
        st.dataframe(df_quality)
        if abs(corr) > 0.5:
            st.warning("Strong correlation detected. Investigate for root cause.")
        else:
            st.success("No strong correlation. Process energy and quality are independent.")
    elif uploaded_file5:
        st.warning("File must have 'Energy_kWh' and 'Quality_Score' columns.")
    else:
        st.info("Using sample data. Upload your CSV to override.")
