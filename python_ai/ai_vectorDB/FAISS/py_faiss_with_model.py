import faiss
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler

# 1. Load data
data = pd.read_excel("py_columns_init.xlsx", engine="openpyxl")
X = data.iloc[:, :-1].values.astype('float32')
y = data.iloc[:, -1].values

# Optional: scale features
scaler = StandardScaler()
X = scaler.fit_transform(X).astype('float32')

# Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 2. Train Logistic Regression
model = LogisticRegression()
model.fit(X_train, y_train)

# 3. Create FAISS index using **feature vectors**
d = X_train.shape[1]  # dimension
index = faiss.IndexFlatL2(d)  # L2 distance
index.add(X_train)  # add vectors to FAISS

# 4. Query new record (take first test sample)
query_vector = X_test[0].reshape(1, -1)
D, I = index.search(query_vector, k=5)  # top 5 similar vectors

print("Top 5 similar record indices:", I)
print("Distances:", D)

# 5. Optional: predict class using Logistic Regression
pred_class = model.predict(query_vector)
print("Predicted class:", pred_class[0])