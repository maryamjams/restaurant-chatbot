import streamlit as st
import pandas as pd
import base64
from datetime import datetime

# Set background image function
def set_background(image_file):
    with open(image_file, "rb") as file:
        bg_image = file.read()
    bg_style = f"""
    <style>
    .stApp {{
        background: url("data:image/jpg;base64,{base64.b64encode(bg_image).decode()}");
        background-size: cover;
        background-position: center;
    }}
    </style>
    """
    st.markdown(bg_style, unsafe_allow_html=True)

# Set background image (make sure the image file is in the same folder)
set_background("background.png")  # Change this to your image file

# Excel file to store orders
EXCEL_FILE = "restaurant_orders.xlsx"

# Restaurant menu
MENU = {
    "Burgers": ["Cheese Burger", "Chicken Burger", "Veggie Burger"],
    "Pizza": ["Pepperoni Pizza", "Margherita Pizza", "BBQ Chicken Pizza"],
    "Drinks": ["Coke", "Orange Juice", "Lemonade"]
}

# Function to save order to Excel
def save_order_to_excel(order_details):
    try:
        # Load existing data or create a new DataFrame
        try:
            df = pd.read_excel(EXCEL_FILE)
        except FileNotFoundError:
            df = pd.DataFrame(columns=["Name", "Phone", "Order", "Total Items", "Time"])

        # Append new order
        new_order = pd.DataFrame([order_details])
        df = pd.concat([df, new_order], ignore_index=True)

        # Save to Excel
        df.to_excel(EXCEL_FILE, index=False, engine="openpyxl")

        st.success("✅ Order placed successfully!")
    except Exception as e:
        st.error(f"⚠️ Error saving order: {e}")

# Streamlit App UI
st.title("🍔 Welcome To Aisol Restaurant!")

st.subheader("📝 Place Order Here")
name = st.text_input("Your Name")
phone = st.text_input("Your Phone Number")
address = st.text_input("Your Address")

# Display Menu
st.subheader("📜 Menu")
selected_category = st.selectbox("Choose a category", list(MENU.keys()))
selected_item = st.selectbox("Choose an item", MENU[selected_category])
quantity = st.number_input("Quantity", min_value=1, step=1)

# Place Order Button
if st.button("🛒 Place Order"):
    if name and phone and selected_item:
        order_details = {
            "Name": name,
            "Phone": phone,
            "Address": address, 
            "Order": selected_item,
            "Total Items": quantity,
            "Time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        save_order_to_excel(order_details)
    else:
        st.warning("⚠️ Please fill in all details before placing an order.")
