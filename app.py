import streamlit as st
from modules.refrigeration import refrigeration_tab
from modules.boilers import boilers_tab
from modules.cip import cip_tab
from modules.air_compressors import air_compressors_tab
from modules.lighting_hvac import lighting_hvac_tab
from modules.advanced_analytics import advanced_analytics_tab
from utils.alerts import show_alerts
from utils.ai_recommendations import show_ai_recommendations
from utils.style import set_custom_style

st.set_page_config(page_title="Dairy Digital Twin", layout="wide")
set_custom_style()

st.title("🧑‍🔬 Dairy Plant Energy Digital Twin")
st.sidebar.image("https://heritagefoods.in/img/logo.png", width=180)
st.sidebar.markdown("## Navigation")
tab_names = [
    "Refrigeration & Chilling",
    "Pasteurization/Boilers",
    "Water Heating & CIP",
    "Air Compressors",
    "Lighting & HVAC",
    "Advanced Analytics",
    "Alerts",
    "AI Recommendations"
]
tabs = st.tabs(tab_names)

with tabs[0]:
    refrigeration_tab()
with tabs[1]:
    boilers_tab()
with tabs[2]:
    cip_tab()
with tabs[3]:
    air_compressors_tab()
with tabs[4]:
    lighting_hvac_tab()
with tabs[5]:
    advanced_analytics_tab()
with tabs[6]:
    show_alerts()
with tabs[7]:
    show_ai_recommendations()
