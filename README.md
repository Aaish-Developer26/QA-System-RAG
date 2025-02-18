# QA System - RAG-based Question Answering System
This project is a Retrieval-Augmented Generation (RAG) based Question Answering (QA) system. It allows users to upload documents, ask questions, and retrieve answers using a combination of document retrieval and generative AI models (Gemini). The system is built using Python, Streamlit for the frontend, and various libraries for data ingestion, embeddings, and model integration.

Features
1. Document Upload: Users can upload PDF documents for processing.
2. Question Answering: Users can ask questions related to the uploaded documents.
3. Gemini Embeddings: Utilizes Google's Gemini embeddings for document retrieval.
4. Streamlit Interface: A user-friendly web interface for interacting with the system.
5. Logging and Exception Handling: Robust logging and custom exception handling for debugging and monitoring.

Prerequisites
Python 3.8 or higher

Pip (Python package manager)

Setup Instructions
1. Clone the Repository
git clone <repository-url>
cd QA_System
2. Create and Activate a Virtual Environment
python -m venv .venv
source .venv/bin/activate  # On Windows: .\.venv\Scripts\activate
3. Install Dependencies
Install the required Python packages using the requirements.txt file:
pip install -r requirements.txt
4. Set Up Environment Variables
Create a .env file in the root directory to store sensitive information (e.g., API keys):
GEMINI_API_KEY=your_gemini_api_key_here
5. Run the Streamlit Application
Start the Streamlit app:
streamlit run streamlitApp.py