import streamlit as st
import pandas as pd
from utils.data_loader import load_csv

def lighting_hvac_tab():
    st.header("Lighting & HVAC")
    uploaded_file = st.file_uploader("Upload Lighting & HVAC Data (.csv)", type="csv")
    if uploaded_file:
        df = load_csv(uploaded_file)
    else:
        df = load_csv("data/sample/lighting_hvac_sample.csv")
    
    st.subheader("Raw Data")
    st.dataframe(df)
    st.metric("Total Lighting Energy (kWh)", df["Lighting_kWh"].sum())
    st.metric("Total HVAC Energy (kWh)", df["HVAC_kWh"].sum())
    st.line_chart(df[["Timestamp", "Lighting_kWh", "HVAC_kWh"]].set_index("Timestamp"))
    
    st.subheader("What-if: LED Retrofit")
    led_adoption = st.slider("LED Adoption (%)", min_value=0, max_value=100, value=50)
    potential_savings = df["Lighting_kWh"].sum()*(led_adoption/100)*0.4
    st.write(f"Potential lighting energy savings: **{potential_savings:.2f} kWh**")
