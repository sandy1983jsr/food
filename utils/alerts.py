import streamlit as st
import pandas as pd
import glob

def show_alerts():
    st.header("🔔 Alerts & Notifications")
    st.write("Detection of abnormal energy consumption and operational anomalies.")
    alert_msgs = []
    for fname in glob.glob("data/sample/*.csv"):
        df = pd.read_csv(fname)
        if "Energy_kWh" in df.columns and df["Energy_kWh"].max() > 1000:
            alert_msgs.append(f"High energy usage detected in {fname.split('/')[-1]}")
        if "Load_%" in df.columns and (df["Load_%"] > 95).sum() > 0:
            alert_msgs.append(f"Possible air compressor overload in {fname.split('/')[-1]}")
    if alert_msgs:
        for msg in alert_msgs:
            st.error(msg)
    else:
        st.success("No critical alerts detected in recent data.")
