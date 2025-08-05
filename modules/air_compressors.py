import streamlit as st
import pandas as pd
from utils.data_loader import load_csv

def air_compressors_tab():
    st.header("Air Compressors")
    uploaded_file = st.file_uploader("Upload Air Compressor Data (.csv)", type="csv")
    if uploaded_file:
        df = load_csv(uploaded_file)
    else:
        df = load_csv("data/sample/air_compressors_sample.csv")
    
    st.subheader("Raw Data")
    st.dataframe(df)
    st.metric("Total Air Generated (m3)", df["Air_m3"].sum())
    st.metric("Average Load (%)", round(df["Load_%"].mean(),2))
    st.line_chart(df[["Timestamp", "Energy_kWh"]].set_index("Timestamp"))
    
    st.subheader("Leak Detection")
    leaks = df[df["Load_%"] > 95]
    st.write(f"Possible leak events: {len(leaks)}")
