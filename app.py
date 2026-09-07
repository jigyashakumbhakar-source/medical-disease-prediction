import streamlit as st
import pandas as pd
import pickle

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="AI Heart Disease Prediction",
    page_icon="❤️",
    layout="wide"
)

# ---------------- LOAD MODEL ----------------
with open("heart_model.pkl", "rb") as file:
    model = pickle.load(file)


# ---------------- CUSTOM CSS ----------------
st.markdown("""
<style>

.main {
    background-color: #f8fafc;
}

.main-title {
    text-align: center;
    font-size: 42px;
    font-weight: bold;
    color: #e63946;
}

.subtitle {
    text-align: center;
    font-size: 18px;
    color: #64748b;
    margin-bottom: 30px;
}

.result-box {
    padding: 20px;
    border-radius: 10px;
}

</style>
""", unsafe_allow_html=True)


# ---------------- SIDEBAR ----------------
with st.sidebar:

    st.title("🩺 Project Information")

    st.write("### AI-Based Medical Prediction")

    st.write("""
    **Algorithm:** Random Forest Classifier

    **Language:** Python

    **Framework:** Streamlit

    **Dataset:** Heart Disease Dataset

    **Input Features:** 13

    **Output:** Heart Disease Risk Prediction
    """)

    st.divider()

    st.info("""
    This system uses Machine Learning
    to analyze patient medical parameters
    and predict the likelihood of heart disease.
    """)


# ---------------- HEADER ----------------
st.markdown(
    '<p class="main-title">❤️ AI-Based Heart Disease Prediction System</p>',
    unsafe_allow_html=True
)

st.markdown(
    '<p class="subtitle">Machine Learning Powered Medical Risk Prediction</p>',
    unsafe_allow_html=True
)

st.divider()


# ---------------- PATIENT INPUT ----------------
st.subheader("🧑‍⚕️ Patient Medical Information")

col1, col2 = st.columns(2)


with col1:

    age = st.number_input(
        "Age",
        min_value=18,
        max_value=100,
        value=45
    )

    sex_label = st.selectbox(
        "Gender",
        ["Female", "Male"]
    )

    sex = 1 if sex_label == "Male" else 0


    cp_label = st.selectbox(
        "Chest Pain Type",
        [
            "Typical Angina",
            "Atypical Angina",
            "Non-anginal Pain",
            "Asymptomatic"
        ]
    )

    cp_mapping = {
        "Typical Angina": 0,
        "Atypical Angina": 1,
        "Non-anginal Pain": 2,
        "Asymptomatic": 3
    }

    cp = cp_mapping[cp_label]


    trestbps = st.number_input(
        "Resting Blood Pressure (mm Hg)",
        min_value=80,
        max_value=220,
        value=120
    )


    chol = st.number_input(
        "Cholesterol Level (mg/dl)",
        min_value=100,
        max_value=600,
        value=200
    )


    fbs_label = st.selectbox(
        "Fasting Blood Sugar > 120 mg/dl",
        ["No", "Yes"]
    )

    fbs = 1 if fbs_label == "Yes" else 0



with col2:

    restecg = st.selectbox(
        "Resting ECG Result",
        [0, 1, 2]
    )


    thalach = st.number_input(
        "Maximum Heart Rate",
        min_value=60,
        max_value=220,
        value=150
    )


    exang_label = st.selectbox(
        "Exercise Induced Angina",
        ["No", "Yes"]
    )

    exang = 1 if exang_label == "Yes" else 0


    oldpeak = st.number_input(
        "ST Depression (Oldpeak)",
        min_value=0.0,
        max_value=10.0,
        value=1.0,
        step=0.1
    )


    slope = st.selectbox(
        "Slope of Peak Exercise ST Segment",
        [0, 1, 2]
    )


    ca = st.selectbox(
        "Number of Major Vessels",
        [0, 1, 2, 3, 4]
    )


    thal = st.selectbox(
        "Thalassemia",
        [0, 1, 2, 3]
    )


# ---------------- PREDICTION ----------------
st.divider()

if st.button("🔍 Predict Heart Disease Risk", use_container_width=True):

    patient_data = pd.DataFrame(
        [[
            age,
            sex,
            cp,
            trestbps,
            chol,
            fbs,
            restecg,
            thalach,
            exang,
            oldpeak,
            slope,
            ca,
            thal
        ]],

        columns=[
            "age",
            "sex",
            "cp",
            "trestbps",
            "chol",
            "fbs",
            "restecg",
            "thalach",
            "exang",
            "oldpeak",
            "slope",
            "ca",
            "thal"
        ]
    )


    prediction = model.predict(patient_data)[0]
    probability = model.predict_proba(patient_data)[0]


    st.divider()

    st.subheader("📊 Prediction Result")


    col_result1, col_result2 = st.columns(2)


    with col_result1:

        if prediction == 1:

            st.error(
                "⚠️ Higher likelihood of Heart Disease detected."
            )

        else:

            st.success(
                "✅ Lower likelihood of Heart Disease detected."
            )


    with col_result2:

        st.metric(
            "Heart Disease Risk Probability",
            f"{probability[1] * 100:.2f}%"
        )


# ---------------- FOOTER ----------------
st.divider()

st.warning(
    "⚠️ Disclaimer: This application is developed for educational "
    "and research purposes only. It should not be considered a "
    "replacement for professional medical diagnosis."
)