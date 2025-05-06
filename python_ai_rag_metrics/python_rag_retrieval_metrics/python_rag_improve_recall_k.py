from sklearn.metrics import recall_score
from sentence_transformers import SentenceTransformer
import numpy as np
import faiss

# --- 1. Sample documents and queries ---
documents = [
    "Paris is the capital of France.",
    "Berlin is the capital of Germany.",
    "Canberra is the capital of Australia.",
    "Ottawa is the capital of Canada.",
    "Tokyo is the capital of Japan."
]

query = "What is the capital of Germany?"
ground_truth = "Berlin is the capital of Germany."  # We want this to be retrieved

# --- 2. Define function to calculate Recall@k ---
def recall_at_k(query_vec, doc_vecs, ground_truth_idx, k=3):
    scores = np.dot(doc_vecs, query_vec)
    top_k_indices = np.argsort(scores)[::-1][:k]
    return int(ground_truth_idx in top_k_indices)

# --- 3. Try with basic embedding model (baseline) ---
model_baseline = SentenceTransformer('all-MiniLM-L6-v2')
doc_vecs_baseline = model_baseline.encode(documents, normalize_embeddings=True)
query_vec_baseline = model_baseline.encode([query], normalize_embeddings=True)[0]

# Compute Recall@k (before)
gt_index = documents.index(ground_truth)
recall_before = recall_at_k(query_vec_baseline, doc_vecs_baseline, gt_index, k=3)
print(f"Recall@3 (BEFORE improvement): {recall_before}")

# --- 4. Try improved embedding model (larger, more accurate) ---
model_improved = SentenceTransformer('all-mpnet-base-v2')  # More powerful model
doc_vecs_improved = model_improved.encode(documents, normalize_embeddings=True)
query_vec_improved = model_improved.encode([query], normalize_embeddings=True)[0]

# Compute Recall@k (after)
recall_after = recall_at_k(query_vec_improved, doc_vecs_improved, gt_index, k=3)
print(f"Recall@3 (AFTER improvement): {recall_after}")