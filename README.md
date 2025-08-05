# Dairy Plant Energy Digital Twin

This Streamlit app enables digital-led and engineering-led energy analysis for dairy processing plants. It models energy-consuming processes and provides AI-driven recommendations and alerts.

## Features

- Tab-based analysis for each key process:
  - Refrigeration & Chilling
  - Pasteurization/Boilers
  - Water Heating & CIP
  - Air Compressors
  - Lighting & HVAC
- Upload CSV data or use provided sample datasets
- Performance dashboards and engineering calculators
- What-if analysis for process optimization
- Automated alerting for anomalies
- AI-driven recommendations using simple ML models
- Professional color palette (orange, grey, white)

## Setup

1. Install requirements:
   ```
   pip install streamlit pandas scikit-learn
   ```
2. Run the app:
   ```
   streamlit run app.py
   ```
3. Optionally, replace sample CSVs in `data/sample/` with your own data.

## Extend

- Add more sophisticated AI models in `utils/ai_recommendations.py`
- Customize visuals in `style.py`
- Add more engineering calculators in module files

---

For any queries, contact [Heritage Foods](https://heritagefoods.in) or your energy optimization consultant.
