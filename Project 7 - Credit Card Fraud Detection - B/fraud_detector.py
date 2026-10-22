# Task 1 - Load the Credit Card Dataset
# Step 1: Import Required Libraries
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix, classification_report

# Step 2: Ingest CSV File
dataset = pd.read_csv("creditcard.csv")

# Task 2 - Separate Features and Target
# Step 1: Isolate Feature Matrix (X)
X = dataset.drop(columns=["Class"])
# Step 2: Isolate Target Vector (y)
y = dataset["Class"]

# Task 3 - Split the Data into Training and Testing Sets
# Step 1: Execute Stratified Partition
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# Task 4 - Build and Train the Machine Learning Pipeline
# Step 1: Configure ColumnTransformer
preprocessor = ColumnTransformer(
    transformers=[
        ("scaler", StandardScaler(), ["Time", "Amount"])
    ],
    remainder="passthrough"
)

# Step 2: Assemble Pipeline
pipeline = Pipeline([
    ("preprocessor", preprocessor),
    ("model", LogisticRegression(class_weight="balanced", max_iter=1000))
])

# Step 3: Train Pipeline
pipeline.fit(X_train, y_train)

# Task 5 - Evaluate the Model Pipeline
# Step 1: Generate Predictions
y_pred = pipeline.predict(X_test)

# Step 2: Display Evaluation Reports
print("Confusion Matrix:")
print(confusion_matrix(y_test, y_pred))
print("\nClassification Report:")
print(classification_report(y_test, y_pred))
