import streamlit as st
import pandas as pd

# Excel file where orders are saved
EXCEL_FILE = "restaurant_orders.xlsx"

# Admin Login
st.title("🔒 Admin Login")
password = st.text_input("Enter Admin Password", type="password")

if password == "admin123":  # Change this to a secure password
    st.title("📋 Restaurant Orders")
    
    try:
        df_orders = pd.read_excel(EXCEL_FILE)
        st.dataframe(df_orders)  # Show orders in a table
    except FileNotFoundError:
        st.warning("⚠️ No orders found.")
else:
    st.warning("🔐 Enter the correct password to access orders.")
