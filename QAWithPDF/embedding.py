from llama_index.core import VectorStoreIndex
from llama_index.core import Settings
from llama_index.llms.gemini import Gemini
from llama_index.embeddings.gemini import GeminiEmbedding
import sys
from exception import customexception
from logger import logging
import os
from dotenv import load_dotenv

load_dotenv()

google_api_key = os.getenv("GOOGLE_API_KEY")

model = Gemini(models='gemini-pro', api_key=google_api_key)
gemini_embed_model = GeminiEmbedding(model_name="models/embedding-001")

# Configure Settings
Settings.llm = model
Settings.embed_model = gemini_embed_model
Settings.chunk_size = 800
Settings.chunk_overlap = 20

def download_gemini_embedding(model, document):
    """
    Creates a vector index from the uploaded document and returns a query engine.

    Parameters:
    - model: The Gemini model.
    - document: The uploaded document.

    Returns:
    - Query engine for querying the document.
    """
    try:
        logging.info("Creating vector index...")
        
        # Create index from the document
        index = VectorStoreIndex.from_documents(document)
        
        # Create query engine
        query_engine = index.as_query_engine()
        
        logging.info("Query engine created successfully.")
        return query_engine
    except Exception as e:
        raise customexception(e, sys)