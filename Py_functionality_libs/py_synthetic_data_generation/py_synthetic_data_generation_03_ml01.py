from sklearn.datasets import (
    make_classification,
)  # Generate synthetic classification dataset
from sklearn.model_selection import (
    train_test_split,
)  # Split dataset into training and testing sets
from sklearn.ensemble import (
    RandomForestClassifier,
)  # Machine learning model for classification (Random Forest) - a popular ensemble method - that combines multiple decision trees to improve predictive performance and control overfitting. (https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestClassifier.html) (many decision trees voting together).
from sklearn.metrics import (
    classification_report,
)  # Evaluate classification performance (precision, recall, f1-score)
import joblib

# Generate synthetic dataset
# x - feature matrix, y - target variable (class labels)
# x is a 2D array where each row represents a sample (what the model sees as input), and each column represents a feature (a characteristic or attribute of the data).
# y is a 1D array where each element corresponds to the class label for the corresponding sample in x (what the model is trying to predict - answers).
# n_samples=5000, - each row is a sample, and each column is a feature (characteristic or attribute of the data)

X, y = make_classification(
    n_samples=5000,  # number of samples (rows) in the dataset  - each row is a sample, and each column is a feature (characteristic or attribute of the data)
    n_features=10,  # number of features (columns) in the dataset - each row is a sample, and each column is a feature (characteristic or attribute of the data)
    n_informative=5,  # number of informative features (features that are actually useful for predicting the target variable)
    n_redundant=2,  # number of redundant features (features that are linear combinations of the informative features)
    n_classes=2,  # number of classes (unique values in the target variable)
    weights=[0.9, 0.1],  # imbalanced dataset (e.g., fraud detection)
    random_state=35,
)

# Train / test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train model
model = RandomForestClassifier(random_state=42)


def check_model_is_trained_with_parameter(model=model, parameter="estimators_"):
    if hasattr(model, parameter):
        print(
            f"✅ Model is trained. {parameter} - Trees:", len(getattr(model, parameter))
        )
    else:
        print(f"❌ Model is NOT trained yet. parameter: {parameter}")


check_model_is_trained_with_parameter()


model.fit(X_train, y_train)
for n, p in model.get_params().items():
    print(f"{n}: {p}")
check_model_is_trained_with_parameter()
check_model_is_trained_with_parameter(parameter="feature_importances_")
# Evaluate
y_pred = model.predict(X_test)
print(classification_report(y_test, y_pred))
joblib.dump(model, "random_forest_model.pkl")
