# 📄 AI PDF Question Answering System (Endee + RAG)

## 🚀 Overview

This project is an AI-powered PDF Question Answering system that allows users to upload PDF documents and ask questions based on their content.

It uses a **Retrieval-Augmented Generation (RAG)** pipeline with semantic search to retrieve relevant information and generate answers.

---

## 🎯 Problem Statement

Manually reading large PDF documents is inefficient and time-consuming.

This project solves that by enabling:

- Intelligent document understanding
- Fast question answering
- Semantic search instead of keyword search

---

## 🧠 Solution Approach

The system implements a **RAG pipeline**:

1. 📄 Upload PDF
2. ✂️ Extract text from PDF
3. 🔢 Convert text into embeddings
4. 📦 Store embeddings in vector store
5. ❓ Convert query into embedding
6. 🔍 Perform similarity search
7. 📌 Retrieve relevant context
8. 🤖 Generate answer

---

## ⚙️ Tech Stack

- Python
- Streamlit
- Sentence Transformers
- Transformers (FLAN-T5)
- NumPy
- PDFPlumber

---

## 💡 Features

- 📂 Upload PDF
- ❓ Ask questions
- 🔍 Semantic search
- 📌 Context-based answers
- 📝 Document summarization
- ⚡ Lightweight and fast

---

## ⚠️ Limitations

- Works only with **text-based PDFs**
- Does not support scanned/image PDFs
- Accuracy depends on extracted text quality

---

## 🏗️ System Architecture

```text
PDF → Text Extraction → Chunking → Embeddings
     → Vector Storage → Query Embedding
     → Similarity Search → Context → Answer
```

---

## 🔗 Endee Integration

This project follows the architecture of a vector database like **Endee**.

- A custom in-memory vector store is used
- Embeddings are stored and retrieved using similarity search

The system is designed in a way that allows easy replacement of the storage layer with **Endee for scalability and performance**.

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

## ▶️ How to Run

```bash
git clone https://github.com/43mohammed-umar/endee-rag-project
cd endee-rag-project

python -m venv venv
venv\Scripts\activate

pip install -r requirements.txt

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

- Full Endee integration
- OCR support for scanned PDFs
- Multi-document support
- Better LLM integration
- Deployment

---

## 🙌 Conclusion

This project demonstrates how AI can convert static PDF documents into an interactive system using:

- Embeddings
- Semantic search
- Retrieval-Augmented Generation (RAG)

It reflects a practical implementation of modern AI workflows.
