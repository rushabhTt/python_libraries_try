from src.data_preprocessing import load_and_preprocess_data
from src.train_model import train_model
from src.evaluate_model import evaluate_model

import os

def main():
    print("Current Working Directory:", os.getcwd())

    # Load and preprocess the data
    X, y = load_and_preprocess_data('data/diabetes.csv')
    
    # Train the model
    model = train_model(X, y)
    
    # Evaluate the model
    evaluate_model(model, X, y)

# This line ensures that the main() function is called only when the script is run directly, not when it is imported as a module.
if __name__ == "__main__":
    main()
