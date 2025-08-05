import streamlit as st
import pandas as pd
from utils.data_loader import load_csv

def refrigeration_tab():
    st.header("Refrigeration & Chilling")
    
    uploaded_file = st.file_uploader("Upload Refrigeration Data (.csv)", type="csv")
    if uploaded_file:
        df = load_csv(uploaded_file)
    else:
        df = load_csv("data/sample/refrigeration_sample.csv")
    
    st.subheader("Raw Data")
    st.dataframe(df)
    
    st.subheader("Energy Performance Dashboard")
    st.metric("Total Energy Used (kWh)", df["Energy_kWh"].sum())
    st.metric("Average COP", round(df["COP"].mean(),2))
    st.line_chart(df[["Timestamp", "Energy_kWh"]].set_index("Timestamp"))
    
    st.subheader("What-if Analysis")
    setpoint = st.slider("Temperature Setpoint (°C)", min_value=2, max_value=8, value=5)
    # Simple what-if: Assume every 1°C increase saves 2% energy
    potential_savings = (8-setpoint)*0.02*df["Energy_kWh"].sum()
    st.write(f"Potential energy savings if setpoint is increased to {setpoint}°C: **{potential_savings:.2f} kWh**")
