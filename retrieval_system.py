import faiss
import numpy as np
from transformers import AutoTokenizer, AutoModel

# Initialize the model and tokenizer
model_name = "sentence-transformers/all-MiniLM-L6-v2"  # Small and efficient model
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModel.from_pretrained(model_name)

# Function to create embeddings
def create_embedding(text):
    inputs = tokenizer(text, return_tensors="pt", padding=True, truncation=True)
    with torch.no_grad():
        outputs = model(**inputs)
    return outputs.last_hidden_state.mean(dim=1).numpy()

# Sample documents
documents = [
    "Document 1: This is an example document.",
    "Document 2: This is another document.",
    "Document 3: More content here.",
]

# Create embeddings for all documents
embeddings = np.array([create_embedding(doc) for doc in documents])

# Initialize FAISS index
dim = embeddings.shape[1]
index = faiss.IndexFlatL2(dim)  # L2 distance (Euclidean)
index.add(embeddings)  # Add vectors to the index

# Function to search the index
def search_index(query, k=3):
    query_embedding = create_embedding(query)
    D, I = index.search(query_embedding, k)
    return [documents[i] for i in I[0]]

# Example usage
if __name__ == "__main__":
    query = "Example query to search"
    print("Top documents:", search_index(query))
