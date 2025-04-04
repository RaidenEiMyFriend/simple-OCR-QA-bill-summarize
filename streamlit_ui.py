import streamlit as st
from ocr_engine import extract_text
from embedding_search import create_faiss_index
from qa_module import setup_qa_system

def main():
    st.title("Simple OCR & QA System")
    uploaded_file = st.file_uploader("Upload an image of your bills, i'll summarize it for you!", type=["png", "jpg", "jpeg"])
    if uploaded_file is not None:
        image_path = "temp.jpg"
        with open(image_path, "wb") as f:
            f.write(uploaded_file.getbuffer())
        
        text = extract_text(image_path)
        st.text_area("Extracted Text", text)
        
        vectorstore = create_faiss_index(text)
        qa = setup_qa_system(vectorstore)
        
        query = st.text_input("Ask a question about the given infos")
        if query:
            answer = qa.run(query)
            st.write("Answer:", answer)

if __name__ == "__main__":
    main()