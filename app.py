import streamlit as st
import joblib
import numpy as np

# Load Model
model = joblib.load("student_exam_model.pkl")

# Title
st.title("🎓 Student Exam Score Predictor")

st.write("Enter student information to predict exam score.")

# Inputs
hours_studied = st.number_input("Hours Studied", min_value=0.0)
sleep_hours = st.number_input("Sleep Hours", min_value=0.0)
attendance_percent = st.number_input("Attendance Percentage", min_value=0.0, max_value=100.0)
previous_scores = st.number_input("Previous Scores", min_value=0.0)

# Prediction
if st.button("Predict Score"):
    features = np.array([[hours_studied, sleep_hours, attendance_percent, previous_scores]])

    prediction = model.predict(features)

    st.success(f"Predicted Exam Score: {prediction[0]:.2f}")
