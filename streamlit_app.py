import streamlit as st
import pandas as pd
import pickle
import os

# Load the model and preprocessor
model_path = os.path.join("artifacts", "model.pkl")
preprocessor_path = os.path.join("artifacts", "preprocessor.pkl")

with open(model_path, 'rb') as model_file:
    model = pickle.load(model_file)

with open(preprocessor_path, 'rb') as preprocessor_file:
    preprocessor = pickle.load(preprocessor_file)

# Streamlit app
st.title("Sales Prediction App")

# Input fields
st.sidebar.header("User Input Features")

Outlet_Size = st.sidebar.selectbox("Outlet Size", ["High", "Medium", "Small"])
Outlet_Identifier = st.sidebar.selectbox("Outlet Identifier",["OUT049",
"OUT018",
"OUT010",
"OUT013",
"OUT027",
"OUT045",
"OUT017",
"OUT046",
"OUT035",
"OUT019"])
Item_Type = st.sidebar.selectbox("Item Type", ["Dairy", "Soft Drinks", "Meat", "Fruits and Vegetables", "Household", "Baking Goods", "Snack Foods", "Frozen Foods", "Breakfast", "Health and Hygiene", "Hard Drinks", "Canned", "Breads", "Starchy Foods", "Others"])
Item_Fat_Content = st.sidebar.selectbox("Item Fat Content", ["Low Fat", "Regular"])
Outlet_Location_Type = st.sidebar.selectbox("Outlet Location Type", ["Tier 1", "Tier 2", "Tier 3"])
Outlet_Type = st.sidebar.selectbox("Outlet Type", ["Grocery Store", "Supermarket Type1", "Supermarket Type2", "Supermarket Type3"])
Item_Weight = st.sidebar.number_input("Item Weight", min_value=0.0)
Item_Visibility = st.sidebar.number_input("Item Visibility", min_value=0.0, max_value=1.0)
Item_MRP = st.sidebar.number_input("Item MRP", min_value=0.0)

# Create a DataFrame from the inputs
input_data = pd.DataFrame({
    "Outlet_Size": [Outlet_Size],
    "Outlet_Identifier": [Outlet_Identifier],
    "Item_Type": [Item_Type],
    "Item_Fat_Content": [Item_Fat_Content],
    "Outlet_Location_Type": [Outlet_Location_Type],
    "Outlet_Type": [Outlet_Type],
    "Item_Weight": [Item_Weight],
    "Item_Visibility": [Item_Visibility],
    "Item_MRP": [Item_MRP]
})

# Display the input data
st.write("### Input Data")
st.write(input_data)

# Preprocess the input data
input_data_preprocessed = preprocessor.transform(input_data)

# Make prediction
if st.button("Predict"):
    prediction = model.predict(input_data_preprocessed)
    st.write(f"### Predicted Sales: {prediction[0]:.2f}")