import numpy as np

# np.random.rand and np.random.randn: Generating synthetic feature and noise.
# np.c_[]: Concatenating arrays (used here to add bias column).
# Matrix multiplication with .dot().
# np.linalg.inv: Inverse of a matrix (used in closed-form regression solution).
# Broadcasting: The operations on arrays of different shapes (e.g., X * slope).

# 1. Generate synthetic data
np.random.seed(42)
X = 2 * np.random.rand(100, 1)  # 100 samples, 1 feature
print(X)
true_slope = 3.5
true_intercept = 1.2
noise = np.random.randn(100, 1) * 0.5
y = true_slope * X + true_intercept + noise

# 2. Add a bias term (column of 1s) to X
X_b = np.c_[np.ones((100, 1)), X]  # shape: (100, 2)

# 3. Use the Normal Equation to solve for theta (best-fit line)
theta_best = np.linalg.inv(X_b.T.dot(X_b)).dot(X_b.T).dot(y)

print("Estimated coefficients:")
print(f"Intercept: {theta_best[0][0]:.2f}")
print(f"Slope: {theta_best[1][0]:.2f}")