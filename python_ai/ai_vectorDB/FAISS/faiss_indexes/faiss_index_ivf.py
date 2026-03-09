# FAISS IndexIVFFlat example
import faiss
import numpy as np

d = 128  # vector dimension
nb = 10000  # database size
nq = 5  # queries

np.random.seed(0)

xb = np.random.random((nb, d)).astype("float32")
xq = np.random.random((nq, d)).astype("float32")

# number of clusters
nlist = 100

quantizer = faiss.IndexFlatL2(d)
index = faiss.IndexIVFFlat(quantizer, d, nlist)

# training step required
index.train(xb)

index.add(xb)

# number of clusters to search
index.nprobe = 10

D, I = index.search(xq, 5)

print(f"xb: {xb.shape}")
print(f"xq: {xq.shape}")
print(f"D: {D}")
print(I)
