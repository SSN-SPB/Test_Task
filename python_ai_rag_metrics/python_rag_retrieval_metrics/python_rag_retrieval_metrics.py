# Retrieval metrics
# Recall@k	Is the ground-truth document in the top-k retrieved?
# Precision@k	What proportion of top-k documents are relevant?
# Hit@k	Binary version of Recall@k (1 if any relevant doc is in top-k)
# MRR (Mean Reciprocal Rank)	How high in the ranking is the first relevant document?
# good / bad
# Recall@k	> 0.8 /	< 0.5	Is the retriever finding all relevant docs? High recall = coverage.
# Precision@k	> 0.6 /	< 0.3	Are the top-k results mostly relevant? High precision = signal strength.
# Hit@k	= 1.0 / = 0.0	Did any relevant doc appear in the top-k? A must-have metric for grounding.
# MRR	> 0.5 / < 0.2	Are relevant docs appearing near the top? Higher = less effort for the LLM.

# Use Case	Recommended K	Reason
# Small context window (OpenAI/GPT-4 Turbo, Claude 3, etc.)	K = 3 to 5	You only want a few chunks that fit in prompt.
# Exploratory search / semantic recall tasks	K = 10 or more	Less precision, more recall to let the model explore.
# Re-ranking with LLMs	K = 20+	Retrieve many, then rank down to top-3 with an LLM.


from typing import List

# --- Simulated Input ---

# Query from user
query = "What is Databricks used for?"

# Retrieved document IDs in ranked order
retrieved_docs = ["doc2", "doc5", "doc3", "doc1", "doc4"]

# Ground truth relevant documents for the query
ground_truth_docs = {"doc1", "doc3"}

# --- Retrieval Metrics ---

def recall_at_k(retrieved: List[str], relevant: set, k: int) -> float:
    return len(set(retrieved[:k]) & relevant) / len(relevant)

def precision_at_k(retrieved: List[str], relevant: set, k: int) -> float:
    return len(set(retrieved[:k]) & relevant) / k

def hit_at_k(retrieved: List[str], relevant: set, k: int) -> int:
    return 1 if len(set(retrieved[:k]) & relevant) > 0 else 0

def mrr(retrieved: List[str], relevant: set) -> float:
    for i, doc in enumerate(retrieved):
        if doc in relevant:
            return 1 / (i + 1)
    return 0.0

# --- Evaluate ---

K = 3 # Example: top-3 documents

print(f"🔍 Recall@{K}: {recall_at_k(retrieved_docs, ground_truth_docs, K):.2f}")
print(f"📐 Precision@{K}: {precision_at_k(retrieved_docs, ground_truth_docs, K):.2f}")
print(f"✅ Hit@{K}: {hit_at_k(retrieved_docs, ground_truth_docs, K)}")
print(f"🏅 MRR: {mrr(retrieved_docs, ground_truth_docs):.2f}")


# What’s K?	The cutoff for how many top docs to consider in evaluation.
# K=3 vs K=7?	Higher K improves recall, but doesn't mean better quality — the position of relevant docs matters.
# How to pick K?	Base it on how many chunks your LLM will see, usually K=3 to K=5 is realistic.
#
# What Is an LLM "Chunk"?
# In RAG, a chunk is a small piece of a document that you pass to the retriever (and eventually the LLM) as part of the context for generation.
#
# Think of a chunk as:
# A passage or paragraph of text
#
# Usually preprocessed from larger documents
#
# Small enough to be embedded and scored efficiently
#
# 🧠 Why Chunk at All?
# Because:
#
# Most documents are too long to embed or use whole.
#
# Chunking allows granular retrieval, improving relevance.
#
# It helps fit content into the LLM's context window (token limit).
#
# 📏 How Big Is a Chunk?
# That depends on your use case and model. Chunk size is usually defined in:
#
#
# Unit	Typical Value	Notes
# Words	100–300 words	Easier to interpret and split on.
# Tokens	200–500 tokens	More precise when working with LLM token limits.
# Sentences	3–5 sentences	Good for semantically meaningful passages.
#
# 3.
# Subword
# tokens
# help
# compress
# common
# stuff
# Instead
# of
# storing
# every
# full
# word, LLMs
# store
# frequent
# subword
# pieces.
#
# For
# example:
#
# "going" → ["go", "ing"]
#
# "builder" → ["build", "er"]
#
# "reusable" → ["re", "us", "able"]
#
# That’s way more efficient
# than memorizing every full word.
