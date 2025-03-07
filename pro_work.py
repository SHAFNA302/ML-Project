import streamlit as st
import joblib
import os
from PIL import Image

# Load the model
model_path = (r"C:\Users\dell\OneDrive\Desktop\project\project work")  # Update with the correct file name
if os.path.exists(model_path):
    model = joblib.load(model_path)
else:
    st.error("Model file not found. Please check the file path.")
    st.stop()

# App title
st.title("Sales and Revenue Analysis: Economic Insights from Transaction Data")
st.write("Leveraging Data for Predicting Revenue and Understanding Sales Trends")

# Load and display image
img_path = (r"C:\Users\dell\OneDrive\Documents\project.jpg")  # Update with the correct file path
if os.path.exists(img_path):
    img = Image.open(img_path)
    st.image(img, width=800)
else:
    st.warning("Image not found. Please check the file path.")

# Input grid
col1, col2, col3 = st.columns(3)

with col1:
    index = st.number_input('Enter the Index:', min_value=0.0, step=0.1)
    customer_gender = st.number_input('Enter the Customer Gender (0 for Male, 1 for Female):', min_value=0, max_value=1, step=1)
    product_category = st.number_input('Enter the Product Category ID:', min_value=0.0, max_value=100.0, step=0.1)

with col2:
    quantity = st.number_input('Enter the Quantity:', min_value=0.0, step=0.1)
    unit_cost = st.number_input('Enter the Unit Cost:', min_value=0.0, step=0.1)

with col3:
    unit_price = st.number_input('Enter the Unit Price:', min_value=0.0, step=0.1)
    cost = st.number_input('Enter the Cost:', min_value=0.0, step=0.1)

# Predict button
if st.button('Check Prediction'):
    try:
        # Ensure the input is a 2D array
        input_data = [[
            index,
            customer_gender,
            product_category,
            quantity,
            unit_cost,
            unit_price,
            cost
        ]]
        predicted = model.predict(input_data)
        st.success(f"The predicted revenue is: ${predicted[0]:.2f}")
    except Exception as e:
        st.error(f"An error occurred during prediction: {e}")
