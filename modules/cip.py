import streamlit as st
from utils.data_loader import load_csv

def cip_tab():
    st.header("Water Heating & CIP")
    uploaded_file = st.file_uploader("Upload CIP Data (.csv)", type="csv")
    if uploaded_file:
        df = load_csv(uploaded_file)
    else:
        df = load_csv("data/sample/cip_sample.csv")
    st.subheader("Raw Data")
    st.dataframe(df)
    st.metric("Total Water Used (L)", df["Water_L"].sum())
    st.metric("Total Energy Used (kWh)", df["Energy_kWh"].sum())
    st.bar_chart(df[["Timestamp", "Energy_kWh"]].set_index("Timestamp"))
    st.subheader("What-if: Insulation Upgrade")
    insulation = st.selectbox("Insulation Quality", ["Standard", "Upgraded"])
    if insulation == "Upgraded":
        savings = df["Energy_kWh"].sum() * 0.10
        st.success(f"Estimated energy savings: **{savings:.2f} kWh**")
