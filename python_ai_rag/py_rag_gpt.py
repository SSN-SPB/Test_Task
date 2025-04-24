from sentence_transformers import SentenceTransformer
from transformers import pipeline
import faiss
import numpy as np

# Sample documents (your "knowledge base")
documents = [
    "Paris is the capital of France.",
    "The Eiffel Tower is located in Paris.",
    "France is known for its wine and cheese.",
    "France is a city.",
    "The Louvre is one of the most famous museums in the world."
]

# 1. Embed documents
# 'all-MiniLM-L6-v2' model for retrieval
model = SentenceTransformer('all-MiniLM-L6-v2')
doc_embeddings = model.encode(documents, convert_to_numpy=True)

# 2. Create FAISS index
dimension = doc_embeddings.shape[1]
index = faiss.IndexFlatL2(dimension)
index.add(doc_embeddings)

# 3. Define user query
# query = "Where is the Eiffel Tower located?"
# query = "What is Paris?"
query = "is Paris country?"
query_embedding = model.encode([query], convert_to_numpy=True)

# 4. Retrieve top-k relevant documents
k = 2
_, top_k_indices = index.search(query_embedding, k)
retrieved_docs = [documents[i] for i in top_k_indices[0]]

# 5. Generate answer using a language model
# "google/flan-t5-small" pretrained model for generator
# generator = pipeline("text2text-generation", model="google/flan-t5-small")
generator = pipeline("text2text-generation", model="google/flan-t5-large")
# generator = pipeline("text2text-generation", model="mistral")

# Combine retrieved docs with the query
context = " ".join(retrieved_docs)
rag_prompt = f"Context: {context} Question: {query}"

# Generate answer
response = generator(rag_prompt, max_length=50)
print("Answer:", response[0]['generated_text'])