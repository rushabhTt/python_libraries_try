import xgboost as xgb

def train_model(X, y):
    # Convert data to DMatrix format for XGBoost
    dtrain = xgb.DMatrix(X, label=y)
    
    # Set parameters for XGBoost
    params = {
        'objective': 'binary:logistic',  # For binary classification
        'max_depth': 4,
        'learning_rate': 0.1,
        'eval_metric': 'logloss'
    }
    
    # Train the model
    model = xgb.train(params, dtrain, num_boost_round=100)
    
    return model
