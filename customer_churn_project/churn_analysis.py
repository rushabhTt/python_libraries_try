import pandas as pd
import numpy as np
import xgboost as xgb
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report
import matplotlib.pyplot as plt

# Step 1: Load Data
df = pd.read_csv('customer_churn.csv')

# Display the column names
print(df.columns)

# Step 2: Data Preprocessing
df.fillna(method='ffill', inplace=True)  # Example: Fill missing values
df = pd.get_dummies(df)  # Encode categorical variables

X = df.drop('Churn', axis=1)  # Features
y = df['Churn']               # Target variable

# Step 3: Train-Test Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Step 4: Model Building and Training
model = xgb.XGBClassifier(random_state=42)
model.fit(X_train, y_train)

# Step 5: Model Evaluation
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy}")
print(classification_report(y_test, y_pred))

# Optional: Visualize feature importance
xgb.plot_importance(model)
plt.show()
