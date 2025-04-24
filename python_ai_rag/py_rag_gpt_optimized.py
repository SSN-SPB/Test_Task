from sentence_transformers import SentenceTransformer
from transformers import pipeline
import faiss

# ✅ Clean document collection (no conflicting info)
documents = [
    "Paris is the capital city of France.",
    "The Eiffel Tower is located in Paris.",
    "France is a country known for its wine and cheese.",
    "The Louvre is one of the most famous museums in the world."
]

# 1. Embedding model for retrieval
embedding_model = SentenceTransformer('all-MiniLM-L6-v2')
doc_embeddings = embedding_model.encode(documents, convert_to_numpy=True)

# 2. Build FAISS index
dimension = doc_embeddings.shape[1]
index = faiss.IndexFlatL2(dimension)
index.add(doc_embeddings)

# 3. User query
query = "Is Paris a country?"
query_embedding = embedding_model.encode([query], convert_to_numpy=True)

# 4. Retrieve top-k similar documents
k = 3
_, top_k_indices = index.search(query_embedding, k)
retrieved_docs = [documents[i] for i in top_k_indices[0]]
context = " ".join(retrieved_docs)

# 5. Better prompt construction
prompt = f"""Based on the following context, determine whether the statement is true or false.

Statement: "Paris is a country."
Context: {context}
Answer:"""

# 6. Use a smarter generation model
# generator = pipeline("text2text-generation", model="google/flan-t5-large")
generator = pipeline("text2text-generation", model="mistral")
response = generator(prompt, max_length=50)

# 7. Print answer
print("Answer:", response[0]['generated_text'])