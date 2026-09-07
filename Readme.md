# AI-Based Heart Disease Prediction System Using Machine Learning

## 📌 Project Overview

The AI-Based Heart Disease Prediction System is a Machine Learning-based web application that predicts the likelihood of heart disease based on patient medical parameters.

The system uses a Random Forest Classifier trained on a heart disease dataset. Users can enter medical information through an interactive Streamlit interface and receive a prediction along with the estimated probability of heart disease.

## 🚀 Features

* Interactive and user-friendly web interface
* Heart disease risk prediction
* Probability-based prediction
* Random Forest Machine Learning model
* Input based on 13 medical parameters
* Real-time prediction using Streamlit

## 🛠️ Technologies Used

* Python
* Pandas
* Scikit-learn
* Streamlit
* Pickle

## 🤖 Machine Learning Algorithm

Random Forest Classifier

## 📊 Project Workflow

Patient Medical Data → Data Preprocessing → Train-Test Split → Random Forest Model → Model Training → Prediction → Streamlit Interface

## 📁 Project Structure

```text
medical-disease-prediction/
│
├── heart.csv
├── train_model.py
├── heart_model.pkl
├── app.py
└── README.md
```

## ⚙️ Installation

Install the required libraries:

```bash
pip install pandas numpy scikit-learn streamlit
```

## ▶️ Run the Project

First, train the model:

```bash
python train_model.py
```

Then run the Streamlit application:

```bash
streamlit run app.py
```

## ⚠️ Disclaimer

This project is developed for educational and research purposes only. It should not be considered a replacement for professional medical diagnosis.
