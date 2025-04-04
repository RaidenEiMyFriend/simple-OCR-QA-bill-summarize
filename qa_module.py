from langchain.chains import RetrievalQA
from langchain.llms import HuggingFacePipeline
from langchain.chains.question_answering import load_qa_chain
from transformers import pipeline

def setup_qa_system(vectorstore):
    hf_pipeline = pipeline("summarization", model="facebook/bart-large-cnn")  # Xác định task
    llm = HuggingFacePipeline(pipeline=hf_pipeline)

    retriever = vectorstore.as_retriever()
    qa_chain = load_qa_chain(llm, chain_type="stuff")  # Thêm chain

    qa = RetrievalQA(combine_documents_chain=qa_chain, retriever=retriever)  # Fix lỗi
    return qa
