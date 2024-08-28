from src.data_preprocessing import load_and_preprocess_data
from src.model_training import train_model
from src.model_evaluation import evaluate_model

def main():
    X, y = load_and_preprocess_data("data/customer_churn.csv")
    model, X_test, y_test = train_model(X, y)
    evaluate_model(model, X_test, y_test)

if __name__ == "__main__":
    main()
