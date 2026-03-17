store = []

def store_embeddings(texts, embeddings):
    global store
    store = []

    for text, emb in zip(texts, embeddings):
        store.append({
            "text": text,
            "embedding": emb
        })


def search_embeddings(query_embedding, top_k=3):
    import numpy as np

    similarities = []

    for item in store:
        sim = np.dot(item["embedding"], query_embedding) / (
            np.linalg.norm(item["embedding"]) * np.linalg.norm(query_embedding)
        )
        similarities.append((item["text"], sim))

    similarities.sort(key=lambda x: x[1], reverse=True)

    return similarities[:top_k]