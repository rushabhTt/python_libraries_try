import numpy as np
from sklearn.metrics import accuracy_score, classification_report
import xgboost as xgb

def evaluate_model(model, X, y):
    # Convert data to DMatrix format for XGBoost
    dtest = xgb.DMatrix(X)
    
    # Predict using the trained model
    y_pred_prob = model.predict(dtest)
    y_pred = np.round(y_pred_prob)  # Convert probabilities to 0 or 1
    
    # Calculate accuracy
    accuracy = accuracy_score(y, y_pred)
    print(f"Accuracy: {accuracy}")
    
    # Print detailed classification report
    print("Classification Report:")
    print(classification_report(y, y_pred))
