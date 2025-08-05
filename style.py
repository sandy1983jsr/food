import streamlit as st

def set_custom_style():
    st.markdown("""
        <style>
        .stTabs [data-baseweb="tab"] {
            background-color: #fff;
            color: #f26a21;
        }
        .stTabs [aria-selected="true"] {
            background-color: #f26a21 !important;
            color: #fff !important;
        }
        .stApp {
            background-color: #f7f7f9;
        }
        .css-1d391kg {
            background-color: #eeeeee !important;
        }
        .stButton>button {
            background-color: #f26a21;
            color: white;
        }
        </style>
    """, unsafe_allow_html=True)
