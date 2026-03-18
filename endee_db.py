from endee import Client

# Initialize Endee client
client = Client()

# Create collection
collection = client.get_or_create_collection("pdf_docs")


def store_embeddings(texts, embeddings):
    ids = [str(i) for i in range(len(texts))]

    collection.add(
        ids=ids,
        embeddings=embeddings.tolist(),
        documents=texts
    )


def search_embeddings(query_embedding, top_k=3):
    results = collection.query(
        query_embeddings=[query_embedding.tolist()],
        n_results=top_k
    )

    return results["documents"][0]