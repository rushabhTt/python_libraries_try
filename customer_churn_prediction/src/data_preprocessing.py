# src/data_preprocessing.py

import pandas as pd
import numpy as np

def load_and_preprocess_data(file_path):
    # Load the dataset from the specified CSV file
    df = pd.read_csv(file_path)

    # Convert 'TotalCharges' to numeric, replacing non-convertible values with NaN
    if 'TotalCharges' in df.columns:
        df['TotalCharges'] = pd.to_numeric(df['TotalCharges'], errors='coerce')

    # Identify all numeric columns in the dataset
    numeric_columns = df.select_dtypes(include=['number']).columns

    # Fill missing values in numeric columns with the median value of the column
    df[numeric_columns] = df[numeric_columns].fillna(df[numeric_columns].median())

    # Convert categorical columns to numeric using one-hot encoding
    df = pd.get_dummies(df, drop_first=True)

    # Separate the dataset into features (X) and target (y)
    if 'Churn_Yes' in df.columns:
        X = df.drop('Churn_Yes', axis=1)  # Features (all columns except 'Churn_Yes')
        y = df['Churn_Yes'].values        # Target (the 'Churn_Yes' column)
    else:
        # Raise an error if the target column 'Churn_Yes' is missing
        raise ValueError("The target column 'Churn_Yes' is missing from the dataset")

    # Convert X to a NumPy array for compatibility with XGBoost
    X = X.values

    # Return the features and target variables
    return X, y
