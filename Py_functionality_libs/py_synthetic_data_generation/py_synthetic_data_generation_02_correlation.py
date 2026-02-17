import numpy as np
import pandas as pd

np.random.seed(42)  # for reproducibility

n_samples = 1000
base_income = np.random.normal(60000, 15000, n_samples)
noise = np.random.normal(0, 30, n_samples)

purchase_amount = (base_income / 1000) + noise

data = {
    "customer_id": np.arange(1, n_samples + 1),
    "age": np.random.normal(loc=35, scale=10, size=n_samples).astype(int),
    "income": base_income.astype(int),
    "purchase_amount": purchase_amount.round(2),
    "is_subscriber": np.random.choice([0, 1], size=n_samples, p=[0.7, 0.3]),
}

df = pd.DataFrame(data)

# Clip unrealistic values
df["age"] = df["age"].clip(18, 80)
df["income"] = df["income"].clip(20000, 200000)
# df["purchase_amount"] = df["purchase_amount"].clip(5, None)

print(df.head(25))
