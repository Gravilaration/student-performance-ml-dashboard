import streamlit as st
import pickle
import pandas as pd
import sqlite3

# Load model
model = pickle.load(open("models/student_model.pkl", "rb"))

st.title("🎓 Student Performance Prediction")
conn = sqlite3.connect("database/students.db")
df = pd.read_sql("SELECT * FROM students", conn)

st.subheader("Dataset Overview")

st.write("Average Scores")
st.write(df[["math score","reading score","writing score"]].mean())

st.write("Enter student details to predict performance.")

# User Inputs
gender = st.selectbox("Gender", ["Male", "Female"])
lunch = st.selectbox("Lunch Type", ["Standard", "Free/Reduced"])
test_prep = st.selectbox("Test Preparation", ["None", "Completed"])

# Encoding (same as training)
gender_val = 1 if gender == "Male" else 0
lunch_val = 1 if lunch == "Standard" else 0
prep_val = 1 if test_prep == "Completed" else 0

# Prediction button
if st.button("Predict Performance"):

    data = pd.DataFrame([[gender_val, lunch_val, prep_val]],
                        columns=["gender", "lunch", "test preparation course"])

    prediction = model.predict(data)[0]

    if prediction == 1:
        st.success("✅ Predicted: Good Performance")
    else:
        st.error("⚠️ Predicted: Poor Performance")