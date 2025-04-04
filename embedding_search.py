from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import FAISS
from langchain.text_splitter import RecursiveCharacterTextSplitter

def create_faiss_index(texts):
    splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    chunks = splitter.split_text(texts)
    embeddings = HuggingFaceEmbeddings()
    vectorstore = FAISS.from_texts(chunks, embeddings)
    return vectorstore