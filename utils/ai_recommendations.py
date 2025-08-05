import streamlit as st
import pandas as pd
import glob
from sklearn.linear_model import LinearRegression
import numpy as np

def show_ai_recommendations():
    st.header("🤖 AI Recommendations")
    st.write("AI-driven suggestions for energy savings and operational improvements.")
    # Example: Linear regression to predict energy use and recommend actions
    for fname in glob.glob("data/sample/*.csv"):
        df = pd.read_csv(fname)
        if "Energy_kWh" in df.columns and "Timestamp" in df.columns:
            X = np.arange(len(df)).reshape(-1,1)
            y = df["Energy_kWh"].values
            model = LinearRegression()
            model.fit(X, y)
            trend = model.coef_[0]
            if trend > 0.5:
                st.warning(f"Energy trend increasing in {fname.split('/')[-1]} — Check equipment for inefficiency or consider process optimization.")
            else:
                st.success(f"Stable energy trend in {fname.split('/')[-1]}. Keep monitoring.")
        if "COP" in df.columns and df["COP"].mean() < 2.5:
            st.info(f"Low COP detected in {fname.split('/')[-1]} — Consider maintenance or upgrading refrigeration equipment.")
