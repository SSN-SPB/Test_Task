import numpy as np
import pandas as pd


# Configuration constants
RANDOM_SEED = 42
N_SAMPLES = 1000
INCOME_MEAN = 60000
INCOME_STD = 15000
NOISE_MEAN = 0
NOISE_STD = 30
AGE_MEAN = 35
AGE_STD = 10
AGE_MIN, AGE_MAX = 18, 80
INCOME_MIN, INCOME_MAX = 20000, 200000
SUBSCRIBER_RATIO = 0.3
LOWEST_AMOUNT = 51

# Set seed for reproducibility in synthetic data generation
np.random.seed(RANDOM_SEED)

# Generate base data
base_income = np.random.normal(INCOME_MEAN, INCOME_STD, N_SAMPLES)
noise = np.random.normal(NOISE_MEAN, NOISE_STD, N_SAMPLES)
purchase_amount = (base_income / 1000) + noise

# Create DataFrame
data = {
    "customer_id": np.arange(1, N_SAMPLES + 1),
    "age": np.random.normal(loc=AGE_MEAN, scale=AGE_STD, size=N_SAMPLES).astype(int),
    "income": base_income.astype(int),
    "purchase_amount": purchase_amount.round(2),
    "is_subscriber": np.random.choice(
        [0, 1], size=N_SAMPLES, p=[1 - SUBSCRIBER_RATIO, SUBSCRIBER_RATIO]
    ),
}

df = pd.DataFrame(data)

# Apply realistic value constraints
df["age"] = df["age"].clip(AGE_MIN, AGE_MAX)
df["income"] = df["income"].clip(INCOME_MIN, INCOME_MAX)
df["purchase_amount"] = df["purchase_amount"].clip(LOWEST_AMOUNT, None)

# Display sample data
print(df.head(25))
