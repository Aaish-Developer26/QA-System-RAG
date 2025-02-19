import streamlit as st
from QAWithPDF.data_ingestion import load_data
from QAWithPDF.embedding import download_gemini_embedding
from QAWithPDF.model_api import load_model

def main():
    st.set_page_config("QA with Documents")
    
    # File uploader
    uploaded_file = st.file_uploader("Upload your document", type="pdf")
    
    st.header("QA with Documents (Information Retrieval)")
    
    user_question = st.text_input("Ask your question")
    
    if uploaded_file and user_question and st.button("Submit & Process"):
        with st.spinner("Processing..."):
            try:
                # Load the uploaded document
                document = load_data(uploaded_file)
                
                # Load the model
                model = load_model()
                
                # Create query engine
                query_engine = download_gemini_embedding(model, document)
                
                # Query the document
                response = query_engine.query(user_question)
                
                # Display the response
                st.write(response.response)
            except Exception as e:
                st.error(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main()