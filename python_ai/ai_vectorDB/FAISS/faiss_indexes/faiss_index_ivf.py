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
print(f"I: {I}")
print(f"I shape: {I.shape}")
print(I)


# -------------------------------
# Simulate IVF Metrics for Queries
# -------------------------------
# We'll assume each query has a "cycle" with random IVF KPIs
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


query_metrics = simulate_ivf_metrics(nq)

# -------------------------------
# Calculate FAIS IVF Index & Quality Gateway
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
    "lab_contamination": 0.05  # max allowed
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
# Report per query
# -------------------------------
for i, metrics in enumerate(query_metrics):
    fais_index = calculate_fais_index(metrics)
    gateway_passed = check_quality_gateway(metrics)
    print(f"\nQuery {i + 1}:")
    print(f"Nearest neighbors indices: {I[i]}")
    print(f"FAIS IVF Index: {fais_index:.2f}")
    print(f"Quality Gateway Passed: {gateway_passed}")

    if not gateway_passed:
        print("Improvement Suggestions:")
        for k, threshold in quality_gateway_thresholds.items():
            if k == "lab_contamination" and metrics[k] > threshold:
                print(f"- Reduce lab contamination ({metrics[k]:.2f} > {threshold})")
            elif k != "lab_contamination" and metrics[k] < threshold:
                print(f"- Improve {k.replace('_', ' ')} ({metrics[k]:.2f} < {threshold})")