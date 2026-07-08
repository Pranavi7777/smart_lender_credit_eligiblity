import os

os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")
os.environ.setdefault("OMP_NUM_THREADS", "1")
os.environ.setdefault("MKL_NUM_THREADS", "1")
os.environ.setdefault("NUMEXPR_NUM_THREADS", "1")

from pathlib import Path
import pickle

import numpy as np
import pandas as pd

from flask import Flask, render_template, request, jsonify


# ============================================================
# FLASK APPLICATION
# ============================================================

app = Flask(__name__)


# ============================================================
# PATH CONFIGURATION
# ============================================================

BASE_DIR = Path(__file__).resolve().parent

MODEL_DIR = BASE_DIR / "final model"

MODEL_PATH = MODEL_DIR / "best_model.pkl"


# ============================================================
# LOAD TRAINED MODEL
# ============================================================

try:

    with MODEL_PATH.open("rb") as file:

        model = pickle.load(file)

    print("\n======================================")
    print("MODEL LOADED SUCCESSFULLY")
    print("======================================")

    print("Model Type:", type(model).__name__)

    print("Model Classes:", model.classes_)

    print("Model Features:")

    for feature in model.feature_names_in_:
        print("-", feature)


except Exception as error:

    print("\n======================================")
    print("MODEL LOADING ERROR")
    print("======================================")

    print(error)

    model = None


# ============================================================
# FEATURE ENCODING
# ============================================================

FEATURE_MAP = {

    "Gender": {
        "Female": 1,
        "Male": 0,
        "1": 1,
        "0": 0
    },

    "Married": {
        "Yes": 1,
        "No": 0,
        "1": 1,
        "0": 0
    },

    "Dependents": {
        "0": 0,
        "1": 1,
        "2": 2,
        "3": 3,
        "3+": 3
    },

    "Education": {
        "Graduate": 1,
        "Not Graduate": 0,
        "1": 1,
        "0": 0
    },

    "Self_Employed": {
        "Yes": 1,
        "No": 0,
        "1": 1,
        "0": 0
    },

    "Credit_History": {
        "Poor": 0,
        "Bad": 0,
        "Good": 1,
        "0": 0,
        "1": 1
    },

    "Property_Area": {
        "Rural": 0,
        "Semiurban": 1,
        "Semi-Urban": 1,
        "Urban": 2,
        "0": 0,
        "1": 1,
        "2": 2
    }
}


# ============================================================
# BASE MODEL FEATURES
# ============================================================

BASE_FEATURES = [

    "Gender",

    "Married",

    "Dependents",

    "Education",

    "Self_Employed",

    "ApplicantIncome",

    "CoapplicantIncome",

    "LoanAmount",

    "Loan_Amount_Term",

    "Credit_History",

    "Property_Area"

]


# ============================================================
# CONVERT FRONTEND INPUT
# ============================================================

def convert_feature(feature_name, value):

    value_string = str(value).strip()

    if feature_name in FEATURE_MAP:

        mapping = FEATURE_MAP[feature_name]

        if value_string in mapping:

            return mapping[value_string]

        raise ValueError(
            f"Invalid value '{value}' for {feature_name}"
        )

    try:

        return float(value)

    except (ValueError, TypeError):

        raise ValueError(
            f"Invalid numeric value '{value}' for {feature_name}"
        )


# ============================================================
# BUILD COMPLETE FEATURE ROW
# ============================================================

def build_feature_row(input_data):

    feature_row = {}


    # --------------------------------------------------------
    # BASE FEATURES
    # --------------------------------------------------------

    for feature in BASE_FEATURES:

        if feature not in input_data:

            raise ValueError(
                f"Missing required field: {feature}"
            )

        feature_row[feature] = convert_feature(
            feature,
            input_data[feature]
        )


    # --------------------------------------------------------
    # FEATURE ENGINEERING
    # --------------------------------------------------------

    applicant_income = feature_row["ApplicantIncome"]

    coapplicant_income = feature_row["CoapplicantIncome"]

    loan_amount = feature_row["LoanAmount"]


    total_income = (
        applicant_income
        +
        coapplicant_income
    )


    if loan_amount > 0:

        income_to_loan_ratio = (
            total_income
            /
            loan_amount
        )

    else:

        income_to_loan_ratio = 0.0


    feature_row["TotalIncome"] = total_income


    feature_row["IncomeToLoanRatio"] = (
        income_to_loan_ratio
    )


    feature_row["LoanAmountLog"] = float(
        np.log1p(loan_amount)
    )


    feature_row["TotalIncomeLog"] = float(
        np.log1p(total_income)
    )


    return feature_row


# ============================================================
# HOME PAGE
# ============================================================

@app.route("/")
def home():

    return render_template("index.html")


# ============================================================
# PREDICTION API
# ============================================================

@app.route("/predict", methods=["POST"])
def predict():

    try:

        # ----------------------------------------------------
        # CHECK MODEL
        # ----------------------------------------------------

        if model is None:

            return jsonify({

                "success": False,

                "message":
                    "ML model is not loaded. Run retrain_models.py first."

            }), 500


        # ----------------------------------------------------
        # GET FRONTEND DATA
        # ----------------------------------------------------

        input_data = request.get_json(silent=True)


        if not input_data:

            return jsonify({

                "success": False,

                "message": "No applicant data received."

            }), 400


        print("\n======================================")
        print("NEW PREDICTION REQUEST")
        print("======================================")

        print("\nReceived Data:")

        print(input_data)


        # ----------------------------------------------------
        # PREPARE FEATURES
        # ----------------------------------------------------

        feature_row = build_feature_row(
            input_data
        )


        # ----------------------------------------------------
        # USE EXACT TRAINING FEATURE ORDER
        # ----------------------------------------------------

        feature_names = list(
            model.feature_names_in_
        )


        features = pd.DataFrame(

            [feature_row],

            columns=feature_names

        )


        print("\nModel Input:")

        print(features)


        # ----------------------------------------------------
        # MAKE PREDICTION
        # ----------------------------------------------------

        prediction = int(
            model.predict(features)[0]
        )


        probabilities = model.predict_proba(
            features
        )[0]


        # ----------------------------------------------------
        # FIND CLASS PROBABILITY INDEXES
        # ----------------------------------------------------

        class_list = list(
            model.classes_
        )


        approval_index = class_list.index(1)

        rejection_index = class_list.index(0)


        approval_probability = float(
            probabilities[approval_index]
        )


        rejection_probability = float(
            probabilities[rejection_index]
        )


        # ----------------------------------------------------
        # PREDICTION RESULT
        # ----------------------------------------------------

        if prediction == 1:

            prediction_text = "Loan Approved"

            prediction_confidence = (
                approval_probability
            )

        else:

            prediction_text = "Loan Rejected"

            prediction_confidence = (
                rejection_probability
            )


        print("\nPrediction:", prediction_text)

        print(
            "Approval Probability:",
            f"{approval_probability * 100:.2f}%"
        )

        print(
            "Rejection Probability:",
            f"{rejection_probability * 100:.2f}%"
        )

        print(
            "Prediction Confidence:",
            f"{prediction_confidence * 100:.2f}%"
        )


        # ----------------------------------------------------
        # SEND RESPONSE TO JAVASCRIPT
        # ----------------------------------------------------

        return jsonify({

            "success": True,

            "prediction": prediction_text,

            "prediction_value": prediction,

            "approval_probability":
                round(
                    approval_probability * 100,
                    2
                ),

            "rejection_probability":
                round(
                    rejection_probability * 100,
                    2
                ),

            "confidence":
                f"{prediction_confidence * 100:.2f}%"

        })


    except Exception as error:

        print("\n======================================")
        print("PREDICTION ERROR")
        print("======================================")

        print(error)


        return jsonify({

            "success": False,

            "message": str(error)

        }), 400


# ============================================================
# HEALTH CHECK
# ============================================================

@app.route("/health", methods=["GET"])
def health():

    return jsonify({

        "status": "ok",

        "model_loaded": model is not None,

        "model_type":
            type(model).__name__
            if model is not None
            else None

    })


# ============================================================
# RUN APPLICATION
# ============================================================

if __name__ == "__main__":

    app.run(

        debug=True,

        use_reloader=False,

        port=5000

    )