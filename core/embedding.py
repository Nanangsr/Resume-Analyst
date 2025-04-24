from langchain.embeddings.sentence_transformer import SentenceTransformerEmbeddings
import os

def get_embedding_model():
    """Get the embedding model"""
    model_name = os.getenv("EMBEDDING_MODEL", "all-MiniLM-L6-v2")
    return SentenceTransformerEmbeddings(model_name=model_name)