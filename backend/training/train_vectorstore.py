# training/train_vectorstore.py
from training.data_ingestor import DataIngestor
from vectorstore.vectorstore_manager import VectorStoreManager

def train_vector_store():
    # Initialize the ingestor to load and process PDFs
    ingestor = DataIngestor()
    ingestor.ingest_new_data()

    # Use vector store manager to build embeddings
    vector_store_manager = VectorStoreManager()
    vector_store_manager.build_embeddings()
    print("Vector store training complete.")

if __name__ == "__main__":
    train_vector_store()
