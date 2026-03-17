# 📄 AI PDF Question Answering System (Endee Project)

## 🚀 Overview

This project is an AI-powered PDF Question Answering system that allows users to upload any PDF document and ask questions based on its content.

The system uses **vector embeddings and semantic search** to retrieve relevant information and generate concise answers.

---

## 🎯 Problem Statement

Reading large PDF documents manually is time-consuming and inefficient.

This project solves that by enabling:

- Intelligent document understanding
- Fast question answering
- Context-based retrieval using AI

---

## 🧠 Solution Approach

This project implements a **basic Retrieval-Augmented Generation (RAG)** pipeline:

1. 📄 Upload PDF
2. ✂️ Extract text from PDF
3. 🔢 Convert text into embeddings
4. 📦 Store embeddings in vector store
5. ❓ Convert user question into embedding
6. 🔍 Perform similarity search
7. 📌 Retrieve context and generate answer

---

## ⚙️ Tech Stack

- Python
- Streamlit
- Sentence Transformers
- NumPy
- PyPDF2

---

## 💡 Features

- 📂 Upload any PDF
- ❓ Ask questions from document
- 🔍 Semantic search-based retrieval
- 📌 Context-based answer generation
- 📝 Document summarization
- ⚡ Fast and lightweight

---

## 🏗️ Project Structure

```bash
endee-rag-project/
│
├── app.py
├── rag_pipeline.py
├── endee_db.py
├── requirements.txt
├── README.md
├── endee/   # Forked Endee repository
```

---

## 🏗️ System Architecture

```
PDF → Text Extraction → Chunking → Embeddings
→ Vector Storage → Query Embedding
→ Similarity Search → Context → Answer Generation
```

---

## 🔗 Endee Integration

This project is aligned with the concept of using a vector database like **Endee**.

Currently:

- A simple in-memory vector store is used
- Embeddings are stored and retrieved for similarity search

In real-world applications, Endee can be used to:

- Store large-scale embeddings
- Perform fast similarity search
- Improve scalability and performance

---

## ▶️ How to Run

```bash
# Clone repository
git clone https://github.com/43mohammed-umar/endee-rag-project

# Navigate to folder
cd endee-rag-project

# Create virtual environment
python -m venv venv

# Activate environment
venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run application
streamlit run app.py
```

---

## 🧪 Example

**Question:**
What skills are mentioned?

**Answer:**
Python, SQL, Machine Learning, etc.

---

## 🔮 Future Improvements

- Full Endee vector database integration
- LLM-based answer generation
- Multi-document support
- Chat-based interface
- Deployment

---

## 🙌 Conclusion

This project demonstrates how AI can transform static PDF documents into interactive systems using semantic search and RAG.

It highlights core AI concepts such as:

- Embeddings
- Vector search
- Context-based answering
