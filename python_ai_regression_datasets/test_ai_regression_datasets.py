import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

# 1. Create sample dataset
np.random.seed(42)
X = 2 * np.random.rand(100, 1)  # feature
y = 4 + 3 * X + np.random.randn(100, 1)  # target with noise

# 2. Split dataset
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# 3. Train model
model = LinearRegression()
model.fit(X_train, y_train)

# 4. Predict on test set
y_pred = model.predict(X_test)

# 5. Evaluate
mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)
r2 = r2_score(y_test, y_pred)

print("MAE:", mae)
print("MSE:", mse)
print("RMSE:", rmse)
print("R2 Score:", r2)


def test_regression_metrics_rmse():
    assert rmse < 1.0, f"RMSE is too high: {rmse}"

def test_regression_metrics_mae():
    assert mae < 1.0, f"MAE is too high: {mae}"

def test_regression_metrics_mse():
    assert mse < 1.0, f"MSE is too high: {mse}"

def test_regression_metrics_r2():
    assert r2 > 0.75, f"R2 Score is too low: {r2}"
