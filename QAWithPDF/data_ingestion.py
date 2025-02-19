from llama_index.core import Document
from pypdf import PdfReader
import sys
from exception import customexception
from logger import logging

def load_data(uploaded_file):
    """
    Load and process the uploaded PDF document.

    Parameters:
    - uploaded_file (UploadedFile): The file uploaded via Streamlit.

    Returns:
    - List of llama_index Document objects.
    """
    try:
        logging.info("Data loading started...")
        
        # Read the uploaded PDF file
        pdf_reader = PdfReader(uploaded_file)
        text = ""
        for page in pdf_reader.pages:
            text += page.extract_text()
        
        # Create a llama_index Document object
        documents = [Document(text=text)]
        
        logging.info("Data loading completed...")
        return documents
    except Exception as e:
        logging.info("Exception in loading data...")
        raise customexception(e, sys)