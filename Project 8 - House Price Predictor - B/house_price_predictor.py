# Task 1 - Load the California Housing Dataset
# Step 1: Import Required Libraries
from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, r2_score

# Step 2: Fetch Dataset
housing_data = fetch_california_housing(as_frame=True)

# Step 3: Extract X and y
X = housing_data.data
y = housing_data.target * 100000.0

# Task 2 - Split the Data into Training and Testing Sets
# Step 1: Execute Train/Test Split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Task 3 - Build and Train the Machine Learning Pipeline
# Step 1: Create Pipeline
pipeline = Pipeline([
    ("scaler", StandardScaler()),
    ("model", LinearRegression())
])

# Step 2: Fit Pipeline
pipeline.fit(X_train, y_train)

# Task 4 - Evaluate the Model Performance
# Step 1: Predict Test Prices
y_pred = pipeline.predict(X_test)

# Step 2: Calculate and Print Metrics
error = mean_absolute_error(y_test, y_pred)
accuracy = r2_score(y_test, y_pred)
print(f"Average Error (MAE): ${error:,.2f}")
print(f"R-squared Score: {accuracy:.4f}")
