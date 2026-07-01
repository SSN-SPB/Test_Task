import faiss
import numpy as np

# -------------------------------
# FAISS Index Setup
# -------------------------------
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

# train and add database vectors
index.train(xb)
index.add(xb)

# number of clusters to search
index.nprobe = 10

# -------------------------------
# Simulate IVF Metrics for the DATABASE
# -------------------------------
def simulate_ivf_metrics(n_cycles):
    metrics_list = []
    for _ in range(n_cycles):
        metrics = {
            "fertilization_rate": np.random.uniform(0.5, 0.9),
            "blastocyst_rate": np.random.uniform(0.4, 0.8),
            "clinical_pregnancy_rate": np.random.uniform(0.3, 0.7),
            "lab_contamination": np.random.uniform(0.0, 0.05)  # lower is better
        }
        metrics_list.append(metrics)
    return metrics_list

db_metrics = simulate_ivf_metrics(nb)

# -------------------------------
# FAIS IVF Index & Quality Gateway Functions
# -------------------------------
weights = {
    "fertilization_rate": 0.3,
    "blastocyst_rate": 0.3,
    "clinical_pregnancy_rate": 0.4
}

quality_gateway_thresholds = {
    "fertilization_rate": 0.7,
    "blastocyst_rate": 0.6,
    "clinical_pregnancy_rate": 0.5,
    "lab_contamination": 0.05
}

def calculate_fais_index(metrics):
    return sum(metrics[k] * w for k, w in weights.items())

def check_quality_gateway(metrics):
    for k, threshold in quality_gateway_thresholds.items():
        if k == "lab_contamination":
            if metrics[k] > threshold:
                return False
        else:
            if metrics[k] < threshold:
                return False
    return True

# -------------------------------
# Search and Report IVF Metrics for Neighbors
# -------------------------------
D, I = index.search(xq, 5)  # top-5 nearest neighbors

for q_idx, neighbors in enumerate(I):
    print(f"\nQuery {q_idx + 1}:")
    for rank, db_idx in enumerate(neighbors):
        metrics = db_metrics[db_idx]
        fais_index = calculate_fais_index(metrics)
        gateway_passed = check_quality_gateway(metrics)
        print(f" Neighbor {rank+1} (db_idx={db_idx}):")
        print(f"   FAIS IVF Index: {fais_index:.2f}")
        print(f"   Quality Gateway Passed: {gateway_passed}")
        if not gateway_passed:
            suggestions = []
            for k, threshold in quality_gateway_thresholds.items():
                if k == "lab_contamination" and metrics[k] > threshold:
                    suggestions.append(f"Reduce lab contamination ({metrics[k]:.2f} > {threshold})")
                elif k != "lab_contamination" and metrics[k] < threshold:
                    suggestions.append(f"Improve {k.replace('_',' ')} ({metrics[k]:.2f} < {threshold})")
            if suggestions:
                print(f"   Improvement Suggestions: {', '.join(suggestions)}")