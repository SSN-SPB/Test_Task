import faiss
import numpy as np
from transformers import pipeline
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

# ----------------------------
# 1. Load LLM
# ----------------------------
llm = pipeline("text2text-generation", model="google/flan-t5-small")

# ----------------------------
# 2. Example documents
# ----------------------------
documents = [
    "Python is a programming language used for AI and data science.",
    "FAISS is a library for fast similarity search over vectors.",
    "Logistic regression is a machine learning classification algorithm.",
    "RAG stands for Retrieval Augmented Generation."
]

# ----------------------------
# 3. Create embeddings
# ----------------------------
# That loads another pretrained embedding model:
#
# all-MiniLM-L6-v2
#
# Used to convert text → vectors.
embed_model = SentenceTransformer("all-MiniLM-L6-v2")

doc_embeddings = embed_model.encode(documents).astype("float32")

# ----------------------------
# 4. Store embeddings in FAISS
# ----------------------------
dimension = doc_embeddings.shape[1]

index = faiss.IndexFlatL2(dimension)
index.add(doc_embeddings)

# ----------------------------
# 5. Ask a question
# ----------------------------
question = "What is FAISS?"

query_vector = embed_model.encode([question]).astype("float32")
print(query_vector.shape)
print(f"query_vector: {query_vector}")

# retrieve top 2 documents
D, I = index.search(query_vector, k=2)

retrieved_docs = [documents[i] for i in I[0]]

context = " ".join(retrieved_docs)

print("Retrieved context:")
print(context)

# ----------------------------
# 6. Ask LLM with context
# ----------------------------
prompt = f"""
Answer the question using the context.

Context:
{context}

Question:
{question}
"""

response = llm(prompt, max_length=50)

answer = response[0]["generated_text"]

print("\nModel answer:")
print(answer)

# ----------------------------
# 7. Evaluate response
# ----------------------------
expected_answer = "FAISS is a library for similarity search."

# embed both answers
ans_emb = embed_model.encode([answer])
exp_emb = embed_model.encode([expected_answer])

score = cosine_similarity(ans_emb, exp_emb)[0][0]

print("\nEvaluation score (semantic similarity):")
print(score)