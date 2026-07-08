# 🏦 Smart Lender — Loan Eligibility Prediction System

<div align="center">

### Machine Learning-Powered Loan Eligibility Analysis & Decision Support Platform

Smart Lender is an end-to-end machine learning web application that analyzes applicant profiles and predicts loan eligibility through a responsive, interactive decision-support interface.

<br>

![Python](https://img.shields.io/badge/Python-3.8%2B-blue?style=for-the-badge&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-Web%20Framework-black?style=for-the-badge&logo=flask&logoColor=white)
![Scikit Learn](https://img.shields.io/badge/Scikit--Learn-Machine%20Learning-orange?style=for-the-badge&logo=scikitlearn&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-150458?style=for-the-badge&logo=pandas&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-Numerical%20Computing-013243?style=for-the-badge&logo=numpy&logoColor=white)
![Jupyter](https://img.shields.io/badge/Jupyter-Model%20Development-F37626?style=for-the-badge&logo=jupyter&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-Interactive%20UI-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black)

<br>

### 🔗 Project Links

[![Live Demo](https://img.shields.io/badge/Live_Demo-View_Application-0F766E?style=for-the-badge)] https://smart-lender-credit-eligiblity-1.onrender.com

[![GitHub](https://img.shields.io/badge/GitHub-Repository-181717?style=for-the-badge&logo=github)] https://github.com/Pranavi7777/smart_lender_credit_eligiblity

[![Demo Video](https://img.shields.io/badge/Demo-Video-FF0000?style=for-the-badge&logo=youtube)]
https://drive.google.com/file/d/19RYqKajJ6J-OMd2v-9A15cyXmCfVBLjk/view

</div>

---

## 📌 Overview

**Smart Lender** is a machine learning-powered loan eligibility prediction platform designed to demonstrate how data-driven systems can support financial decision-making workflows.

The application accepts structured applicant information such as income, loan amount, credit history, education, employment status, dependents, and property area.

The submitted applicant profile is processed by a trained machine learning model through a Flask backend. The system then returns:

- Loan approval or rejection prediction
- Prediction confidence
- Approval probability
- Interactive decision analysis

The project integrates the complete machine learning lifecycle — from data preprocessing and exploratory analysis to model comparison, feature engineering, model deployment, and frontend integration.

> **Smart Lender is designed as a machine learning decision-support project and not as a replacement for real-world financial underwriting systems.**

---

## ✨ Key Features

| Feature | Description |
|---|---|
| 🤖 Machine Learning Prediction | Predicts applicant loan eligibility using a trained classification model |
| 📊 Model Comparison | Evaluates multiple machine learning classification algorithms |
| ⚙️ Automated Model Selection | Selects the best-performing candidate model based on evaluation performance |
| 🧠 Feature Engineering | Generates additional financial indicators from the original applicant data |
| ⚡ Real-Time Analysis | Sends applicant data to the Flask API and returns predictions instantly |
| 📈 Probability Insights | Displays approval probability and prediction confidence |
| 💻 Product-Style Interface | Responsive and interactive loan analysis workspace |
| 🔄 End-to-End ML Pipeline | Connects data preprocessing, training, model persistence, backend, and frontend |

---

## 🖥️ Application Preview

### 🏠 Smart Lender Home Page

<p align="center">
  <img src="assets/home.JPG" alt="Smart Lender Home Page" width="90%">
</p>

The landing interface introduces the Smart Lender platform, machine learning workflow, and application capabilities through a modern product-style experience.

---

### 💳 Loan Eligibility Analyzer

<p align="center">
  <img src="assets/loan_eligibility.JPG" alt="Loan Eligibility Analyzer" width="90%">
</p>

Applicants can enter 11 profile attributes and receive an instant machine learning prediction with confidence and approval probability.

---

### ⚙️ Machine Learning Workflow

<p align="center">
  <img src="assets/working_process.JPG" alt="Smart Lender Machine Learning Workflow" width="90%">
</p>

The project follows an end-to-end workflow from applicant data preprocessing and feature engineering to model evaluation, persistence, and Flask deployment.

---

## 🏗️ System Architecture

```text
                    ┌─────────────────────────┐
                    │   Loan Applicant Data   │
                    └────────────┬────────────┘
                                 │
                                 ▼
                    ┌─────────────────────────┐
                    │   Data Preprocessing    │
                    │                         │
                    │  • Missing Values       │
                    │  • Categorical Encoding │
                    │  • Data Transformation  │
                    └────────────┬────────────┘
                                 │
                                 ▼
                    ┌─────────────────────────┐
                    │    Feature Engineering  │
                    │                         │
                    │  • Total Income         │
                    │  • Income/Loan Ratio    │
                    │  • Loan Amount Log      │
                    │  • Total Income Log     │
                    └────────────┬────────────┘
                                 │
                                 ▼
              ┌──────────────────────────────────────┐
              │          Model Comparison            │
              │                                      │
              │  Decision Tree    Random Forest      │
              │  KNN              Gradient Boosting  │
              │  XGBoost                             │
              └──────────────────┬───────────────────┘
                                 │
                                 ▼
                    ┌─────────────────────────┐
                    │   Best Model Selection  │
                    │       F1 Score          │
                    └────────────┬────────────┘
                                 │
                                 ▼
                    ┌─────────────────────────┐
                    │     best_model.pkl      │
                    └────────────┬────────────┘
                                 │
                                 ▼
                    ┌─────────────────────────┐
                    │      Flask Backend      │
                    │                         │
                    │   /predict   /health    │
                    └────────────┬────────────┘
                                 │
                                 ▼
                    ┌─────────────────────────┐
                    │     Smart Lender UI     │
                    │                         │
                    │   HTML • CSS • JS       │
                    └─────────────────────────┘
```

---

## 🔄 Project Workflow

```text
Dataset
   ↓
Exploratory Data Analysis
   ↓
Data Preprocessing
   ↓
Categorical Encoding
   ↓
Missing Value Handling
   ↓
Feature Engineering
   ↓
Train-Test Split
   ↓
Train Multiple ML Models
   ↓
Model Evaluation
   ↓
Best Model Selection
   ↓
Model Serialization
   ↓
Flask API Integration
   ↓
Interactive Web Application
   ↓
Loan Eligibility Prediction
```

---

## 🧠 Machine Learning Pipeline

### 1️⃣ Data Preprocessing

The original dataset contains applicant demographic, financial, and credit-related attributes.

The preprocessing pipeline performs:

- Categorical feature encoding
- Missing value handling
- Dependent value transformation
- Numerical feature preparation
- Target variable encoding

---

### 2️⃣ Feature Engineering

The system generates additional features to improve the representation of applicant financial profiles.

#### Total Income

```text
TotalIncome = ApplicantIncome + CoapplicantIncome
```

#### Income-to-Loan Ratio

```text
IncomeToLoanRatio = TotalIncome / LoanAmount
```

#### Log-Transformed Loan Amount

```text
LoanAmountLog = log(1 + LoanAmount)
```

#### Log-Transformed Total Income

```text
TotalIncomeLog = log(1 + TotalIncome)
```

These engineered features help the models capture relationships between applicant income and requested loan amount.

---

### 3️⃣ Model Training and Comparison

Smart Lender compares five classification algorithms:

| Model | Purpose |
|---|---|
| Decision Tree | Tree-based classification baseline |
| Random Forest | Ensemble learning using multiple decision trees |
| K-Nearest Neighbors | Distance-based classification |
| Gradient Boosting | Sequential ensemble learning |
| XGBoost | Optimized gradient boosting classification |

Each candidate model is trained using the same training and testing data split.

The models are evaluated using classification metrics, including:

- Accuracy
- F1 Score
- Confusion Matrix
- Classification Report

---

### 4️⃣ Best Model Selection

The training pipeline compares candidate models and selects the model with the highest F1 score.

```text
Decision Tree ────────┐
                      │
Random Forest ────────┤
                      │
KNN ──────────────────┼──► Model Evaluation ──► Best Model
                      │
Gradient Boosting ────┤
                      │
XGBoost ──────────────┘
```

The selected model is serialized as:

```text
final model/best_model.pkl
```

The Flask application loads this artifact when the server starts.

---

## 📥 Model Inputs

The machine learning model evaluates 11 applicant inputs.

| Input Feature | Description |
|---|---|
| Gender | Applicant gender |
| Married | Marital status |
| Dependents | Number of dependents |
| Education | Graduate or non-graduate |
| Self Employed | Employment category |
| Applicant Income | Primary applicant income |
| Co-Applicant Income | Co-applicant income |
| Loan Amount | Requested loan amount |
| Loan Amount Term | Loan repayment period |
| Credit History | Applicant credit history |
| Property Area | Rural, semi-urban, or urban property location |

---

## 📤 Prediction Output

After analyzing the applicant profile, Smart Lender displays:

```text
Prediction Result
        │
        ├──► Approved / Rejected
        │
        ├──► Prediction Confidence
        │
        └──► Approval Probability
```

Example:

```text
Prediction Result: Approved

Prediction Confidence: 55.98%

Approval Probability: 55.98%
```

---

## 🛠️ Technology Stack

### Machine Learning & Data Science

<p>

![Python](https://img.shields.io/badge/Python-Programming-blue?style=flat-square&logo=python)
![Pandas](https://img.shields.io/badge/Pandas-Data_Processing-150458?style=flat-square&logo=pandas)
![NumPy](https://img.shields.io/badge/NumPy-Numerical_Computing-013243?style=flat-square&logo=numpy)
![Scikit Learn](https://img.shields.io/badge/Scikit--Learn-Machine_Learning-F7931E?style=flat-square&logo=scikitlearn)
![XGBoost](https://img.shields.io/badge/XGBoost-Classification-EC6B23?style=flat-square)

</p>

### Data Analysis & Visualization

<p>

![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-F37626?style=flat-square&logo=jupyter)
![Matplotlib](https://img.shields.io/badge/Matplotlib-Visualization-blue?style=flat-square)
![Seaborn](https://img.shields.io/badge/Seaborn-Statistical_Visualization-4C72B0?style=flat-square)

</p>

### Backend Development

<p>

![Flask](https://img.shields.io/badge/Flask-Backend-black?style=flat-square&logo=flask)
![Python](https://img.shields.io/badge/Python-API-blue?style=flat-square&logo=python)

</p>

### Frontend Development

<p>

![HTML5](https://img.shields.io/badge/HTML5-Structure-E34F26?style=flat-square&logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/CSS3-Styling-1572B6?style=flat-square&logo=css3&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-Interaction-F7DF1E?style=flat-square&logo=javascript&logoColor=black)

</p>

### Development Tools

<p>

![VS Code](https://img.shields.io/badge/VS_Code-Development-007ACC?style=flat-square&logo=visualstudiocode)
![Git](https://img.shields.io/badge/Git-Version_Control-F05032?style=flat-square&logo=git&logoColor=white)
![GitHub](https://img.shields.io/badge/GitHub-Repository-181717?style=flat-square&logo=github)

</p>

---

## 📂 Project Structure

```text
SMARTLENDER/
│
├── assets/
│   ├── home.JPG
│   ├── loan_eligibility.JPG
│   └── working_process.JPG
│
├── dataset/
│   └── loan_prediction.xlsx
│
├── final model/
│   └── best_model.pkl
│
├── static/
│   ├── script.js
│   └── style.css
│
├── templates/
│   └── index.html
│
├── training model/
│   └── training.ipynb
│
├── app.py
├── retrain_models.py
├── README.md
└── requirements.txt
```

---

## 🚀 Run the Project Locally

### 1️⃣ Clone the Repository

```bash
git clone ADD_GITHUB_REPOSITORY_LINK_HERE
```

### 2️⃣ Navigate to the Project Directory

```bash
cd smartlender
```

### 3️⃣ Create a Virtual Environment

```bash
python -m venv .venv
```

### 4️⃣ Activate the Virtual Environment

#### Windows

```powershell
.venv\Scripts\activate
```

#### Linux / macOS

```bash
source .venv/bin/activate
```

### 5️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 6️⃣ Retrain the Machine Learning Models

Run this step when the dataset, feature engineering, or model configuration changes.

```bash
python retrain_models.py
```

The best-performing model will be saved as:

```text
final model/best_model.pkl
```

### 7️⃣ Start the Flask Application

```bash
python app.py
```

### 8️⃣ Open the Application

Open the following address in your browser:

```text
http://127.0.0.1:5000
```

---

## 🔌 API Endpoints

| Endpoint | Method | Description |
|---|---|---|
| `/` | GET | Loads the Smart Lender application |
| `/predict` | POST | Processes applicant data and returns the ML prediction |
| `/health` | GET | Checks backend and model availability |

---

## 💡 Use Cases

### 🟢 Applicant Eligibility Screening

Analyze structured applicant information and generate an immediate machine learning prediction.

### 🟠 Risk Identification

Identify applicant profiles that the trained model associates with a lower probability of loan approval.

### 🔵 Machine Learning Decision Support

Demonstrate how classification models can be integrated into interactive financial technology applications.

---

## 👥 Project Team

| Role | Name |
|---|---|
| Team Lead | Kaligineedi Dhanush |
| Member | Karumuri Sai Pranavi |
| Member | R Rohith Siva Sai Krishna |
| Member | Tulasi Vijaya Dharma Teja Koppada |
| Member | Anitha Myla |

---

## 🎓 Project Context

This project was developed as part of the **SmartBridge Artificial Intelligence and Machine Learning Internship Program**.

The project demonstrates practical implementation of:

- Data preprocessing
- Exploratory data analysis
- Feature engineering
- Classification algorithms
- Model comparison
- Model evaluation
- Model serialization
- Flask backend development
- REST-style API integration
- Responsive frontend development
- End-to-end machine learning deployment

---

## 🔮 Future Enhancements

- Add explainable AI using SHAP or feature importance analysis
- Improve probability calibration
- Introduce cross-validation for more robust model comparison
- Add hyperparameter optimization
- Implement secure user authentication
- Add application history and prediction tracking
- Build an administrative analytics dashboard
- Containerize the application using Docker
- Deploy the production application to a cloud platform

---

## ⚠️ Disclaimer

Smart Lender is an educational machine learning project developed for academic and internship purposes.

Predictions are generated from a trained machine learning model and should not be used as the sole basis for real-world financial, lending, or credit decisions.

---

## 📬 Project Links

| Resource | Link |
|---|---|
| 🌐 Live Application | https://smart-lender-credit-eligiblity-1.onrender.com |
| 💻 GitHub Repository | https://github.com/Pranavi7777/smart_lender_credit_eligiblity |
| 🎥 Demo Video |https://drive.google.com/file/d/19RYqKajJ6J-OMd2v-9A15cyXmCfVBLjk/view |

---

<div align="center">

### 🏦 Smart Lender

**Machine Learning-Powered Loan Eligibility Analysis**

Built with Python • Machine Learning • Flask • JavaScript

<br>

⭐ If you find this project useful, consider giving the repository a star.

</div>
