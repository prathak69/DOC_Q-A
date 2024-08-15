import streamlit as st
from .pdf_processing import extract_text_from_pdf
from .text_processing import preprocess_text
from .openai_integration import ask_question

def render_app():
    st.title("PDF Q&A App 📝")
    st.markdown("Upload a PDF file and ask questions about its content!")
    
    # Optionally display a logo or any other image
    st.image("assets/logo.png", width=150)

    api_key = st.text_input("Enter your OpenAI API Key:", type="password")

    uploaded_file = st.file_uploader("Upload a PDF file", type="pdf")

    if uploaded_file is not None:
        with st.spinner("Extracting text from PDF..."):
            text = extract_text_from_pdf(uploaded_file)
        st.success("PDF content extracted successfully!")

        if text:
            with st.spinner("Processing text..."):
                processed_text = preprocess_text(text)

            question = st.text_input("Ask a question about the document:")
            if question:
                with st.spinner("Getting your answer..."):
                    answer = ask_question(processed_text, question, api_key)
                st.write("**Answer:**", answer)
        else:
            st.warning("The PDF seems to be empty or text could not be extracted.")
