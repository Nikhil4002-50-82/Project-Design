# Task 1 - Load the Customer Churn Dataset
# Step 1: Import Required Libraries
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, roc_auc_score

# Step 2: Ingest CSV File
customer_data = pd.read_csv("WA_Fn-UseC_-Telco-Customer-Churn.csv")

# Task 2 - Clean and Prepare Features
# Step 1: Clean TotalCharges and Binarize Churn
customer_data["TotalCharges"] = pd.to_numeric(customer_data["TotalCharges"], errors="coerce").fillna(0.0)
customer_data["Churn"] = (customer_data["Churn"] == "Yes").astype(int)

# Step 2: Separate X and y
X = customer_data.drop(columns=["customerID", "Churn"])
y = customer_data["Churn"]

# Task 3 - Split Data into Training and Testing Sets
# Step 1: Execute Stratified Partition
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# Task 4 - Build and Train the Preprocessing & Model Pipeline
# Step 1: Define Column Groups
numerical_columns = ["SeniorCitizen", "tenure", "MonthlyCharges", "TotalCharges"]
categorical_columns = [
    "gender", "Partner", "Dependents", "PhoneService", "MultipleLines",
    "InternetService", "OnlineSecurity", "OnlineBackup", "DeviceProtection",
    "TechSupport", "StreamingTV", "StreamingMovies", "Contract",
    "PaperlessBilling", "PaymentMethod"
]

# Step 2: Create ColumnTransformer
preprocessor = ColumnTransformer(
    transformers=[
        ("numeric", StandardScaler(), numerical_columns),
        ("categorical", OneHotEncoder(drop="first", handle_unknown="ignore"), categorical_columns)
    ]
)

# Step 3: Assemble Pipeline and Train
pipeline = Pipeline([
    ("preprocessor", preprocessor),
    ("classifier", RandomForestClassifier(n_estimators=50, random_state=42))
])
pipeline.fit(X_train, y_train)

# Task 5 - Evaluate the Pipeline
# Step 1: Predict Classes and Probabilities
y_pred = pipeline.predict(X_test)
y_prob = pipeline.predict_proba(X_test)[:, 1]

# Step 2: Display Evaluation Reports
print("Classification Report:")
print(classification_report(y_test, y_pred))
print(f"ROC-AUC Score: {roc_auc_score(y_test, y_prob):.4f}")
