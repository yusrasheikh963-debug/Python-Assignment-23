import streamlit as st
import pandas as pd
import joblib

# Page Config
st.set_page_config(
    page_title="Machine Learning Prediction System",
    layout="wide"
)

st.title("Machine Learning Prediction System")
st.write("Prediction using Multiple Machine Learning Models")

# Load Models
logistic_model = joblib.load("Logistic_model.pkl")
knn_model = joblib.load("knn_model.pkl")
naive_model = joblib.load("Naive_bayes_model.pkl")
price_model = joblib.load("Price_model.pkl")

# Load Scalers
heart_scaler = joblib.load("scaler.pkl")
heart_columns = joblib.load("columns.pkl")

price_scaler = joblib.load("Price_scaler.pkl")
price_columns = joblib.load("Price_columns.pkl")

# Sidebar
problem = st.sidebar.selectbox(
    "Select Model",
    [
        "Car Price Prediction",
        "Logistic Regression",
        "KNN",
        "Naive Bayes"
    ]
)

#CAR PRICE PREDICTION

if problem == "Car Price Prediction":

    st.header("Ford Car Price Prediction")

    model_name = st.text_input("Car Model")
    year = st.number_input("Year", 1990, 2026, 2018)

    transmission = st.selectbox(
        "Transmission",
        ["Manual", "Automatic", "Semi-Auto"]
    )

    mileage = st.number_input(
        "Mileage",
        min_value=0,
        value=20000
    )

    fuelType = st.selectbox(
        "Fuel Type",
        ["Petrol", "Diesel", "Hybrid", "Electric"]
    )

    tax = st.number_input(
        "Tax",
        min_value=0,
        value=150
    )

    mpg = st.number_input(
        "MPG",
        min_value=0.0,
        value=50.0
    )

    engineSize = st.number_input(
        "Engine Size",
        min_value=0.0,
        value=1.5
    )

    if st.button("Predict Price"):

        input_df = pd.DataFrame({
            "model": [model_name],
            "year": [year],
            "transmission": [transmission],
            "mileage": [mileage],
            "fuelType": [fuelType],
            "tax": [tax],
            "mpg": [mpg],
            "engineSize": [engineSize]
        })

        input_df = pd.get_dummies(input_df)

        input_df = input_df.reindex(columns=price_columns, fill_value=0)

        try:
            input_scaled = price_scaler.transform(input_df)
            prediction = price_model.predict(input_scaled)
        except:
            prediction = price_model.predict(input_df)

        st.success(f"💰 Predicted Car Price: ₹ {prediction[0]:,.2f}")

# HEART INPUT FUNCTION
def heart_inputs():

    age = st.number_input("Age", 1, 120, 45)
    sex = st.selectbox("Sex", ["M", "F"])
    chest = st.selectbox("ChestPainType", ["ATA", "NAP", "ASY", "TA"])
    restingBP = st.number_input("RestingBP", 50, 250, 120)
    cholesterol = st.number_input("Cholesterol", 0, 700, 200)
    fastingBS = st.selectbox("FastingBS", [0, 1])
    restingECG = st.selectbox("RestingECG", ["Normal", "ST", "LVH"])
    maxHR = st.number_input("MaxHR", 50, 250, 150)
    exerciseAngina = st.selectbox("ExerciseAngina", ["N", "Y"])
    oldpeak = st.number_input("Oldpeak", 0.0, 10.0, 1.0)
    stSlope = st.selectbox("ST_Slope", ["Up", "Flat", "Down"])

    df = pd.DataFrame({
        "Age":[age],
        "Sex":[sex],
        "ChestPainType":[chest],
        "RestingBP":[restingBP],
        "Cholesterol":[cholesterol],
        "FastingBS":[fastingBS],
        "RestingECG":[restingECG],
        "MaxHR":[maxHR],
        "ExerciseAngina":[exerciseAngina],
        "Oldpeak":[oldpeak],
        "ST_Slope":[stSlope]
    })

    df = pd.get_dummies(df)
    df = df.reindex(columns=heart_columns, fill_value=0)
    df = heart_scaler.transform(df)

    return df

# HEART DISEASE PREDICTION

if problem == "Logistic Regression":

    st.header("Heart Disease Prediction (Logistic Regression)")

    data = heart_inputs()

    if st.button("Predict"):

        pred = logistic_model.predict(data)

        if pred[0] == 1:
            st.error("⚠️ Heart Disease Detected")
        else:
            st.success("✅ No Heart Disease")


#KNN

if problem == "KNN":

    st.header("Heart Disease Prediction (KNN)")

    data = heart_inputs()

    if st.button("Predict"):

        pred = knn_model.predict(data)

        if pred[0] == 1:
            st.error("⚠️ Heart Disease Detected")
        else:
            st.success("✅ No Heart Disease")


#NAIVE BAYES

if problem == "Naive Bayes":

    st.header("Heart Disease Prediction (Naive Bayes)")

    data = heart_inputs()

    if st.button("Predict"):

        pred = naive_model.predict(data)

        if pred[0] == 1:
            st.error("⚠️ Heart Disease Detected")
        else:
            st.success("✅ No Heart Disease")