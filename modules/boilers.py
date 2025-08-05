import streamlit as st
from utils.data_loader import load_csv

def boilers_tab():
    st.header("Pasteurization / Boilers")
    uploaded_file = st.file_uploader("Upload Boiler Data (.csv)", type="csv")
    if uploaded_file:
        df = load_csv(uploaded_file)
    else:
        df = load_csv("data/sample/boilers_sample.csv")
    st.subheader("Raw Data")
    st.dataframe(df)
    st.metric("Total Steam Generated (kg)", df["Steam_kg"].sum())
    st.metric("Boiler Efficiency (%)", round(df["Efficiency"].mean(),2))
    st.area_chart(df[["Timestamp", "Fuel_Consumed"]].set_index("Timestamp"))
    st.subheader("Efficiency Calculator")
    fuel = st.number_input("Fuel Used (kg)", value=100)
    steam = st.number_input("Steam Generated (kg)", value=150)
    efficiency = steam / fuel * 100
    st.write(f"Calculated Efficiency: **{efficiency:.2f}%**")
