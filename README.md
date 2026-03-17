# 📄 AI PDF Question Answering System (Endee Project)

## 🚀 Overview

This project is an AI-powered PDF Question Answering system that allows users to upload a PDF document and ask questions based on its content.

The system uses **vector embeddings and semantic search** to retrieve the most relevant information from the document and display accurate answers.

---

## 🎯 Problem Statement

Reading large PDF documents manually is time-consuming and inefficient.
This project solves that by enabling **intelligent document search using AI**.

---

## 🧠 How It Works

1. 📄 Upload PDF
2. ✂️ Split text into chunks
3. 🔢 Convert text into vector embeddings
4. ❓ Convert user question into embedding
5. 🔍 Perform similarity search
6. 📌 Return top relevant answers

Additionally:

- ✅ Keyword-based matching improves accuracy
- ✅ Semantic search ensures better context understanding

---

## ⚙️ Tech Stack

- Python
- Streamlit (UI)
- Sentence Transformers (Embeddings)
- NumPy
- LangChain (Document Processing)

---

## 💡 Features

- 📂 Upload any PDF
- ❓ Ask questions from document
- 📊 Top 3 relevant answers with similarity score
- 🔍 Hybrid search (Keyword + Semantic)
- 📝 Document summarization

---

## 🗂️ Project Structure

```
endee-rag-project/
│
├── app.py                # Streamlit UI
├── rag_pipeline.py       # Core AI logic
├── requirements.txt      # Dependencies
├── README.md             # Project documentation
├── data/                 # Optional data folder
└── endee/                # Forked Endee repository
```

---

## 🧪 Example

**Question:**
Who is the project guide?

**Answer:**
Dr. S. Shabana Begum

---

## 🔗 Endee Integration (Conceptual)

This project demonstrates how vector-based search works.
In real-world applications, tools like **Endee Vector Database** can be used to:

- Store embeddings efficiently
- Perform fast similarity search
- Scale to large datasets

---

## ▶️ How to Run

```bash
# Step 1: Clone repository
git clone https://github.com/43mohammed-umar/endee

# Step 2: Navigate to project folder
cd endee-rag-project

# Step 3: Create virtual environment
python -m venv venv

# Step 4: Activate environment
venv\Scripts\activate

# Step 5: Install dependencies
pip install -r requirements.txt

# Step 6: Run application
streamlit run app.py
```

---

## 📌 Future Improvements

- Integration with Endee vector database
- LLM-based answer generation (OpenAI / ChatGPT)
- Multi-document support
- Improved UI/UX

---

## 🙌 Conclusion

This project demonstrates a practical implementation of **Retrieval-Augmented Generation (RAG)** using vector embeddings and hybrid search techniques.

It showcases how AI can make document interaction faster, smarter, and more efficient.
