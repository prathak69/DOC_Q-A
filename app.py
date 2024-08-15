import streamlit as st
from app.ui import render_app

def main():
    st.set_page_config(page_title="PDF Q&A App", page_icon="📝", layout="wide")
    render_app()

if __name__ == "__main__":
    main()
