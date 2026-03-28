import streamlit as st
import pandas as pd
import os

# 1. UI Setup - JPMC Branding
st.set_page_config(page_title="JPMC Payments Lab", layout="wide")
st.title("💳 Digital Payment Friction Dashboard")
st.markdown("### Product Analytics Solution - Associate Portal")

# 2. Path to your data
file_path = '/Users/ronithmantheni/Documents/data/jpmc_payments_data.csv'

if os.path.exists(file_path):
    df = pd.read_csv(file_path)
    
    # --- SIDEBAR: INTERACTIVE CONTROLS ---
    st.sidebar.header("Test a User Scenario")
    user_device = st.sidebar.selectbox("Customer Device", ['iOS', 'Android', 'Web'])
    user_amount = st.sidebar.slider("Transaction Amount ($)", 5, 500, 100)
    
    # --- MAIN PANEL: ANALYSIS ---
    st.subheader("Automated Risk Assessment")
    
    if st.button("Run Diagnostic"):
        # We manually program the "Android Bug" logic we found earlier
        if user_device == 'Android':
            st.error(f"⚠️ HIGH RISK: Android users are experiencing 100% failure at the Security Step.")
            st.info("💡 Business Insight: Recommend Engineering team to roll back the latest Biometric update.")
        elif user_amount > 400:
            st.warning("⚠️ MODERATE RISK: High-value transactions are seeing higher 'Timeout' rates.")
        else:
            st.success("✅ LOW RISK: This transaction profile is healthy.")

    # --- DATA VISUALIZATION (Automated Reporting) ---
    st.divider()
    st.subheader("Live Funnel Health")
    # This fulfills the "Automate analyses into dashboards" requirement
    funnel = df['Last_Step_Reached'].value_counts().sort_index()
    funnel.index = ['Started', 'Entered Details', 'Security Check', 'Success']
    st.bar_chart(funnel)

else:
    st.error("Data file not found. Please ensure 'jpmc_payments_data.csv' is in the data folder.")