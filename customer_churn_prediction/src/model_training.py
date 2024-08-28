import numpy as np
import xgboost as xgb
from sklearn.model_selection import train_test_split

def train_model(X, y):
    y = np.array(y)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    model = xgb.XGBClassifier(random_state=42)
    model.fit(X_train, y_train)
    return model, X_test, y_test
