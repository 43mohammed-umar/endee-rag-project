import PyPDF2
from sentence_transformers import SentenceTransformer
from endee_client import store_embeddings, search_embeddings
from transformers import pipeline

embed_model = SentenceTransformer("all-MiniLM-L6-v2")
qa_pipeline = pipeline(
    "text-generation",
    model="distilgpt2"
)


def process_pdf(file_path):
    texts = []

    with open(file_path, "rb") as file:
        reader = PyPDF2.PdfReader(file)

        for page in reader.pages:
            text = page.extract_text()
            if text:
                texts.append(text)

    chunks = []
    for text in texts:
        for i in range(0, len(text), 300):
            chunks.append(text[i:i+300])

    embeddings = embed_model.encode(chunks)

    store_embeddings(chunks, embeddings)

    return chunks


def get_answer(question):
    query_embedding = embed_model.encode(question)

    results = search_embeddings(query_embedding)

    if not results:
        return "No relevant information found."

    context = " ".join(results[:3])

    if not context.strip():
        return "No useful context found."

    # 🔥 Simple intelligent extraction (NO LLM)
    sentences = context.split(".")

    question_words = question.lower().split()

    best_sentence = ""

    for sentence in sentences:
        score = sum(word in sentence.lower() for word in question_words)

        if score > 0:
            best_sentence = sentence

    if best_sentence:
        return best_sentence.strip()

    return context[:200]  # fallback