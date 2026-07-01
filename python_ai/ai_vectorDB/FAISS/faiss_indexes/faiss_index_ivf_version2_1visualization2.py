import faiss
import numpy as np
import matplotlib.pyplot as plt

# -------------------------------
# FAISS Index Setup
# -------------------------------
d = 128
nb = 10000
nq = 5

np.random.seed(0)

xb = np.random.random((nb, d)).astype("float32")
xq = np.random.random((nq, d)).astype("float32")

nlist = 100
quantizer = faiss.IndexFlatL2(d)
index = faiss.IndexIVFFlat(quantizer, d, nlist)
index.train(xb)
index.add(xb)
index.nprobe = 10


# -------------------------------
# Simulate IVF Metrics for DATABASE
# -------------------------------
def simulate_ivf_metrics(n_cycles):
    metrics_list = []
    for _ in range(n_cycles):
        metrics = {
            "fertilization_rate": np.random.uniform(0.5, 0.9),
            "blastocyst_rate": np.random.uniform(0.4, 0.8),
            "clinical_pregnancy_rate": np.random.uniform(0.3, 0.7),
            "lab_contamination": np.random.uniform(0.0, 0.05)
        }
        metrics_list.append(metrics)
    return metrics_list


db_metrics = simulate_ivf_metrics(nb)

# -------------------------------
# FAIS IVF Index & Quality Gateway
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
# Search and Aggregate Metrics
# -------------------------------
D, I = index.search(xq, 5)

agg_fais_indices = []
gateway_results = []
agg_kpis_per_query = []

for q_idx, neighbors in enumerate(I):
    agg_metrics = {"fertilization_rate": 0, "blastocyst_rate": 0,
                   "clinical_pregnancy_rate": 0, "lab_contamination": 0}
    for db_idx in neighbors:
        metrics = db_metrics[db_idx]
        for k in agg_metrics.keys():
            agg_metrics[k] += metrics[k]
    for k in agg_metrics.keys():
        agg_metrics[k] /= len(neighbors)

    agg_fais_index = calculate_fais_index(agg_metrics)
    gateway_passed = check_quality_gateway(agg_metrics)

    agg_fais_indices.append(agg_fais_index)
    gateway_results.append(gateway_passed)

    # Store averaged KPI for second chart
    agg_kpis_per_query.append([
        agg_metrics["fertilization_rate"],
        agg_metrics["blastocyst_rate"],
        agg_metrics["clinical_pregnancy_rate"]
    ])

    print(f"Query {q_idx + 1}: FAIS IVF Index = {agg_fais_index:.2f}, Gateway Passed = {gateway_passed}")

# -------------------------------
# Chart 1: FAIS IVF Index per Query
# -------------------------------
colors = ['green' if passed else 'red' for passed in gateway_results]

plt.figure(figsize=(8, 5))
plt.bar(range(1, nq + 1), agg_fais_indices, color=colors)
plt.axhline(0.6, color='blue', linestyle='--', label='Reference FAIS Index')
plt.xticks(range(1, nq + 1), [f"Query {i}" for i in range(1, nq + 1)])
plt.ylim(0, 1)
plt.ylabel("Aggregated FAIS IVF Index")
plt.title("IVF Metrics: FAIS Index per Query (Green=Pass, Red=Fail)")
plt.legend()
plt.show()

# -------------------------------
# Chart 2: Average IVF KPIs per Query
# -------------------------------
agg_kpis_per_query = np.array(agg_kpis_per_query)  # shape (nq, 3)

labels = ['Fertilization', 'Blastocyst', 'Clinical Pregnancy']
x = np.arange(nq)
width = 0.25

plt.figure(figsize=(10, 6))
for i in range(3):
    plt.bar(x + i * width, agg_kpis_per_query[:, i], width=width, label=labels[i])

plt.xticks(x + width, [f"Query {i}" for i in range(1, nq + 1)])
plt.ylim(0, 1)
plt.ylabel("Average KPI")
plt.title("Average IVF KPIs per Query (Top-5 Neighbors)")
plt.legend()
plt.show()