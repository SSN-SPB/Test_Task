# Top-level Steps (Summary):
#
# Step	What it does
# 1. Import libraries	Use tools (numpy, pandas, sklearn)
# 2. Load data	Read the input data (CSV, database, etc.)
# 3. Preprocess	Clean and prepare data (features + labels)
# 4. Split data	Train-test division
# 5. Create model	Define model type (Logistic Regression, Neural Network, etc.)
# 6. Train model	Fit the model to the data
# 7. Evaluate model	Check performance (accuracy, loss, etc.)
# 8. Main entry	Organize the program cleanly
# 🧠 Notes:
# Here I used Logistic Regression (super simple, good for first ML examples).
#
# You could replace it easily with Decision Tree, Random Forest, or even a Neural Network.
#
# Real-world projects would add hyperparameter tuning, cross-validation, logging, etc.
#
# 🎯 In short:
# Creating and training a model is a structured pipeline: data → model → training → evaluation.

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score


# 2. Load and prepare data
def load_data():
    # Load dataset from file
    # data = pd.read_csv(filepath)
    data = pd.read_excel("py_columns_init.xlsx", engine="openpyxl")

    return data


def preprocess_data(data):
    # Handle missing values, normalize, etc.
    # Example: Assume last column is the label
    X = data.iloc[:, :-1]  # features
    y = data.iloc[:, -1]  # labels
    return X, y


# 3. Split data into train/test sets
def split_data(X, y, test_size=0.2):
    return train_test_split(X, y, test_size=test_size, random_state=42)


# 4. Define and create the model
def create_model():
    # Initialize a simple Logistic Regression model
    model = LogisticRegression()
    return model


# 5. Train the model
def train_model(model, X_train, y_train):
    model.fit(X_train, y_train)
    return model


# 6. Evaluate the model
def evaluate_model(model, X_test, y_test):
    predictions = model.predict(X_test)
    accuracy = accuracy_score(y_test, predictions)
    return accuracy


# 7. Main program
def main():
    # Step-by-step running
    # data = load_data('your_dataset.csv')
    data = load_data()
    X, y = preprocess_data(data)
    X_train, X_test, y_train, y_test = split_data(X, y)

    model = create_model()
    model = train_model(model, X_train, y_train)

    accuracy = evaluate_model(model, X_test, y_test)
    print(f"Model Accuracy: {accuracy:.2f}")


if __name__ == "__main__":
    main()