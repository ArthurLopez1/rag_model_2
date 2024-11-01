# training/data_ingestor.py
import os
from utils.pdf_parser import parse_pdf_with_pypdf
from vectorstore.vectorstore_manager import VectorStoreManager

class DataIngestor:
    def __init__(self, data_folder="data"):
        self.data_folder = data_folder
        self.vectorstore_manager = VectorStoreManager()

    def ingest_new_data(self):
        for filename in os.listdir(self.data_folder):
            if filename.endswith(".pdf"):
                pdf_path = os.path.join(self.data_folder, filename)
                documents = parse_pdf_with_pypdf(pdf_path)
                self.vectorstore_manager.add_documents(documents)
                print(f"Added {filename} to vector store.")
