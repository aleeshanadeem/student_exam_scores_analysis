import streamlit as st
import joblib
import numpy as np

# Load Model
model = joblib.load("student_exam_model.pkl")

# Title
st.title("🎓 Student Exam Score Predictor")

st.write("Enter student information to predict exam score.")

hours_studied = st.number_input("Hours Studied", min_value=0.0)
sleep_hours = st.number_input("Sleep Hours", min_value=0.0)
attendance_percent = st.number_input("Attendance Percentage", min_value=0.0, max_value=100.0)
previous_scores = st.number_input("Previous Scores", min_value=0.0)

if st.button("Predict Score"):
    features = np.array([[hours_studied, sleep_hours, attendance_percent, previous_scores]])

    prediction = model.predict(features)

    percentage = (prediction[0] / 51.3) * 100

    st.success(
        f"Predicted Exam Score: {prediction[0]:.2f} / 51.3 ({percentage:.1f}%)"
    )
