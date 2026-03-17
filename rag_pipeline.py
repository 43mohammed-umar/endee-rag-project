from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from sentence_transformers import SentenceTransformer
import numpy as np

# Load embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")
# STEP 1: Process PDF
=======

#  STEP 1: Process PDF
def process_pdf(file_path):
    loader = PyPDFLoader(file_path)
    documents = loader.load()

    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=50
    )

    texts = text_splitter.split_documents(documents)
    texts = [doc.page_content for doc in texts]

    embeddings = model.encode(texts)

    return texts, embeddings

# --STEP 2: SMART ANSWER SYSTEM 
#  STEP 2: SMART ANSWER SYSTEM
def get_answer(question, texts, embeddings):

    # 1. KEYWORD BASED SEARCH (STRONG FIX)
    keywords = question.lower().split()

    keyword_hits = []
    for text in texts:
        if any(word in text.lower() for word in keywords):
            keyword_hits.append(text)

    # If strong keyword match found → return directly
    if keyword_hits:
        return [("🔍 Exact Match:\n" + keyword_hits[0], 1.0)]


    # 2. FALLBACK TO SEMANTIC SEARCH
    # FALLBACK TO SEMANTIC SEARCH
    query_embedding = model.encode([question])[0]
    similarities = np.dot(embeddings, query_embedding)

    top_indices = np.argsort(similarities)[-3:][::-1]

    results = [(texts[i], similarities[i]) for i in top_indices]

    return results
