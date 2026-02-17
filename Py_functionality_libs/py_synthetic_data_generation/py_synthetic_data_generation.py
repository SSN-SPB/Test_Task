import numpy as np
import pandas as pd

np.random.seed(42)  # for reproducibility

n_samples = 1000

data = {
    "customer_id": np.arange(1, n_samples + 1),
    "age": np.random.normal(loc=35, scale=10, size=n_samples).astype(int),
    "income": np.random.normal(loc=60000, scale=15000, size=n_samples).astype(int),
    "purchase_amount": np.random.exponential(scale=120, size=n_samples).round(2),
    "is_subscriber": np.random.choice([0, 1], size=n_samples, p=[0.7, 0.3]),
}

df = pd.DataFrame(data)

# Clip unrealistic values
df["age"] = df["age"].clip(18, 80)
df["income"] = df["income"].clip(20000, 200000)

print(df.head())
