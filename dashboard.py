import streamlit as st
import pickle
import pandas as pd
import sqlite3

# Load model
model = pickle.load(open("models/student_model.pkl", "rb"))

st.title("🎓 Student Performance Prediction")

# Load dataset
conn = sqlite3.connect("database/students.db")
df = pd.read_sql("SELECT * FROM students", conn)

st.subheader("Dataset Overview")

st.write("Average Scores")
st.write(df[["math score","reading score","writing score"]].mean())

st.write("Enter student scores to predict performance.")

# User Inputs
math_score = st.slider("Math Score", 0, 100, 50)
reading_score = st.slider("Reading Score", 0, 100, 50)
writing_score = st.slider("Writing Score", 0, 100, 50)

# Prediction button
if st.button("Predict Performance"):

    data = pd.DataFrame([[math_score, reading_score, writing_score]],
                        columns=["math score", "reading score", "writing score"])

    prediction = model.predict(data)[0]

    if prediction == 1:
        st.success("✅ Predicted: Good Performance")
    else:
        st.error("⚠️ Predicted: Poor Performance")
