import faiss
import numpy as np

# create random vectors
data = np.random.random((1000, 128)).astype('float32')
print("Random data:", data)

# build index
index = faiss.IndexFlatL2(128)
index.add(data)

# query vector
query = np.random.random((1,128)).astype('float32')
# print(query)

# search
distances, indices = index.search(query, k=5)
print(indices)