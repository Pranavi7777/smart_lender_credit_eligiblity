import os

os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")
os.environ.setdefault("OMP_NUM_THREADS", "1")
os.environ.setdefault("MKL_NUM_THREADS", "1")
os.environ.setdefault("NUMEXPR_NUM_THREADS", "1")

from pathlib import Path
import pickle

import numpy as np
import pandas as pd

from sklearn.ensemble import (
    GradientBoostingClassifier,
    RandomForestClassifier
)

from sklearn.metrics import (
    accuracy_score,
    f1_score,
    confusion_matrix,
    classification_report
)

from sklearn.model_selection import train_test_split

from sklearn.neighbors import KNeighborsClassifier

from sklearn.tree import DecisionTreeClassifier

from xgboost import XGBClassifier


# ============================================================
# PATH CONFIGURATION
# ============================================================

BASE_DIR = Path(__file__).resolve().parent

DATA_PATH = (
    BASE_DIR
    /
    "dataset"
    /
    "loan_prediction.xlsx"
)

MODEL_DIR = (
    BASE_DIR
    /
    "final model"
)

MODEL_DIR.mkdir(

    parents=True,

    exist_ok=True

)

MODEL_PATH = (
    MODEL_DIR
    /
    "best_model.pkl"
)


# ============================================================
# LOAD AND PREPROCESS DATA
# ============================================================

def load_dataset():

    print("\n======================================")
    print("LOADING DATASET")
    print("======================================")


    data = pd.read_excel(
        DATA_PATH
    )


    print(
        "Original Dataset Shape:",
        data.shape
    )


    # --------------------------------------------------------
    # ENCODE CATEGORICAL FEATURES
    # --------------------------------------------------------

    data["Gender"] = data["Gender"].map({

        "Female": 1,

        "Male": 0

    })


    data["Married"] = data["Married"].map({

        "Yes": 1,

        "No": 0

    })


    data["Education"] = data["Education"].map({

        "Graduate": 1,

        "Not Graduate": 0

    })


    data["Self_Employed"] = data[
        "Self_Employed"
    ].map({

        "Yes": 1,

        "No": 0

    })


    data["Property_Area"] = data[
        "Property_Area"
    ].map({

        "Urban": 2,

        "Semiurban": 1,

        "Rural": 0

    })


    data["Loan_Status"] = data[
        "Loan_Status"
    ].map({

        "Y": 1,

        "N": 0

    })


    # --------------------------------------------------------
    # DEPENDENTS
    # --------------------------------------------------------

    data["Dependents"] = (

        data["Dependents"]

        .astype(str)

        .str.replace(
            "+",
            "",
            regex=False
        )

    )


    data["Dependents"] = pd.to_numeric(

        data["Dependents"],

        errors="coerce"

    )


    # --------------------------------------------------------
    # HANDLE MISSING VALUES
    # --------------------------------------------------------

    categorical_columns = [

        "Gender",

        "Married",

        "Dependents",

        "Self_Employed",

        "Credit_History"

    ]


    for column in categorical_columns:

        data[column] = data[column].fillna(

            data[column].mode()[0]

        )


    numerical_columns = [

        "LoanAmount",

        "Loan_Amount_Term"

    ]


    for column in numerical_columns:

        data[column] = data[column].fillna(

            data[column].median()

        )


    # --------------------------------------------------------
    # FEATURE ENGINEERING
    # --------------------------------------------------------

    data["TotalIncome"] = (

        data["ApplicantIncome"]

        +

        data["CoapplicantIncome"]

    )


    data["IncomeToLoanRatio"] = (

        data["TotalIncome"]

        /

        data["LoanAmount"].replace(
            0,
            np.nan
        )

    )


    data["IncomeToLoanRatio"] = (

        data["IncomeToLoanRatio"]

        .replace(
            [np.inf, -np.inf],
            np.nan
        )

        .fillna(0)

    )


    data["LoanAmountLog"] = np.log1p(

        data["LoanAmount"]

    )


    data["TotalIncomeLog"] = np.log1p(

        data["TotalIncome"]

    )


    # --------------------------------------------------------
    # FEATURES AND TARGET
    # --------------------------------------------------------

    X = data.drop(

        [
            "Loan_ID",
            "Loan_Status"
        ],

        axis=1

    )


    y = data["Loan_Status"]


    print(
        "Final Dataset Shape:",
        X.shape
    )


    print("\nTraining Features:")


    for index, feature in enumerate(
        X.columns,
        start=1
    ):

        print(
            index,
            feature
        )


    return X, y


# ============================================================
# LOAD DATA
# ============================================================

X, y = load_dataset()


# ============================================================
# TRAIN TEST SPLIT
# ============================================================

X_train, X_test, y_train, y_test = train_test_split(

    X,

    y,

    test_size=0.20,

    random_state=42,

    stratify=y

)


print("\n======================================")
print("TRAIN TEST SPLIT")
print("======================================")

print(
    "Training Records:",
    len(X_train)
)

print(
    "Testing Records:",
    len(X_test)
)


# ============================================================
# MODEL CONFIGURATION
# ============================================================

models = {


    "Decision Tree":

        DecisionTreeClassifier(

            random_state=42,

            class_weight="balanced"

        ),


    "Random Forest":

        RandomForestClassifier(

            n_estimators=800,

            max_depth=10,

            min_samples_leaf=4,

            max_features=0.7,

            class_weight="balanced_subsample",

            random_state=42

        ),


    "KNN":

        KNeighborsClassifier(

            n_neighbors=7

        ),


    "Gradient Boosting":

        GradientBoostingClassifier(

            random_state=42

        ),


    "XGBoost":

        XGBClassifier(

            n_estimators=300,

            learning_rate=0.05,

            max_depth=3,

            subsample=0.9,

            colsample_bytree=0.9,

            random_state=42,

            eval_metric="logloss"

        )

}


# ============================================================
# TRAIN AND EVALUATE MODELS
# ============================================================

results = []

best_model = None

best_model_name = None

best_f1_score = -1


print("\n======================================")
print("MODEL TRAINING STARTED")
print("======================================")


for model_name, current_model in models.items():


    print(
        f"\nTraining {model_name}..."
    )


    # --------------------------------------------------------
    # TRAIN MODEL
    # --------------------------------------------------------

    current_model.fit(

        X_train,

        y_train

    )


    # --------------------------------------------------------
    # MAKE TEST PREDICTIONS
    # --------------------------------------------------------

    predictions = current_model.predict(

        X_test

    )


    # --------------------------------------------------------
    # CALCULATE METRICS
    # --------------------------------------------------------

    accuracy = accuracy_score(

        y_test,

        predictions

    )


    f1 = f1_score(

        y_test,

        predictions

    )


    matrix = confusion_matrix(

        y_test,

        predictions

    )


    # --------------------------------------------------------
    # SAVE RESULTS
    # --------------------------------------------------------

    results.append({

        "model": model_name,

        "accuracy": accuracy,

        "f1_score": f1,

        "confusion_matrix": matrix

    })


    print(
        "Accuracy:",
        f"{accuracy * 100:.2f}%"
    )


    print(
        "F1 Score:",
        f"{f1 * 100:.2f}%"
    )


    print(
        "Confusion Matrix:"
    )


    print(matrix)


    # --------------------------------------------------------
    # FIND BEST MODEL
    # --------------------------------------------------------

    if f1 > best_f1_score:

        best_f1_score = f1

        best_model_name = model_name

        best_model = current_model


# ============================================================
# PRINT FINAL COMPARISON
# ============================================================

print("\n======================================")
print("FINAL MODEL COMPARISON")
print("======================================")


for result in results:

    print(

        f"\n{result['model']}"

    )


    print(

        "Accuracy:",

        f"{result['accuracy'] * 100:.2f}%"

    )


    print(

        "F1 Score:",

        f"{result['f1_score'] * 100:.2f}%"

    )


# ============================================================
# BEST MODEL
# ============================================================

print("\n======================================")
print("BEST MODEL")
print("======================================")

print(
    "Model:",
    best_model_name
)

print(
    "F1 Score:",
    f"{best_f1_score * 100:.2f}%"
)


# ============================================================
# CLASSIFICATION REPORT
# ============================================================

best_predictions = best_model.predict(

    X_test

)


print("\nClassification Report:")


print(

    classification_report(

        y_test,

        best_predictions

    )

)


# ============================================================
# SAVE BEST MODEL
# ============================================================

with MODEL_PATH.open("wb") as file:

    pickle.dump(

        best_model,

        file

    )


print("\n======================================")
print("MODEL SAVED SUCCESSFULLY")
print("======================================")

print(
    "Saved Model:",
    best_model_name
)

print(
    "Location:",
    MODEL_PATH
)