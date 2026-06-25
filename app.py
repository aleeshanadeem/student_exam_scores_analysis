if st.button("Predict Score"):
    features = np.array([[hours_studied, sleep_hours, attendance_percent, previous_scores]])

    prediction = model.predict(features)

    percentage = (prediction[0] / 51.3) * 100

    st.success(
        f"Predicted Exam Score: {prediction[0]:.2f} / 51.3 ({percentage:.1f}%)"
    )
