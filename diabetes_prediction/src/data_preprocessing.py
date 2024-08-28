import pandas as pd
import numpy as np

def load_and_preprocess_data(filepath):
    # Define column names for the dataset
    column_names = ['Pregnancies', 'Glucose', 'BloodPressure', 'SkinThickness', 
                    'Insulin', 'BMI', 'DiabetesPedigreeFunction', 'Age', 'Outcome']
    
    # Load the dataset
    df = pd.read_csv(filepath, header=None, names=column_names)
    
    # Here, we're using the DataFrame's loc accessor to explicitly select and modify the values in each column.
    # We locate all rows where the column value is 0 and replace those values with NaN.
    # This approach avoids chained assignment, making the operation more explicit and avoiding future warnings.
    df.loc[df['Glucose'] == 0, 'Glucose'] = np.nan
    df.loc[df['BloodPressure'] == 0, 'BloodPressure'] = np.nan
    df.loc[df['SkinThickness'] == 0, 'SkinThickness'] = np.nan
    df.loc[df['Insulin'] == 0, 'Insulin'] = np.nan
    df.loc[df['BMI'] == 0, 'BMI'] = np.nan
    
    # Fill missing values with the mean of the respective columns
    df.fillna(df.mean(), inplace=True)
    
    # Split the data into features (X) and target (y)
    X = df.drop('Outcome', axis=1)
    y = df['Outcome']
    
    return X, y