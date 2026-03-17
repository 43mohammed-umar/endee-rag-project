import PyPDF2
from sentence_transformers import SentenceTransformer
from endee_db import store_embeddings, search_embeddings

# Load model
model = SentenceTransformer("all-MiniLM-L6-v2")


def process_pdf(file_path):
    texts = []

    # Read PDF manually (no LangChain)
    with open(file_path, "rb") as file:
        reader = PyPDF2.PdfReader(file)

        for page in reader.pages:
            text = page.extract_text()
            if text:
                texts.append(text)

    # Simple chunking
    chunks = []
    for text in texts:
        for i in range(0, len(text), 200):
            chunks.append(text[i:i+200])

    embeddings = model.encode(chunks)

    store_embeddings(chunks, embeddings)

    return chunks


def get_answer(question, texts):
    query_embedding = model.encode([question])[0]

    results = search_embeddings(query_embedding)

    if not results:
        return "No relevant answer found."

    context = " ".join([text for text, _ in results])

    question_words = question.lower().split()
    sentences = context.split(".")

    for sentence in sentences:
        if any(word in sentence.lower() for word in question_words):
            return sentence.strip()

    return context[:200]