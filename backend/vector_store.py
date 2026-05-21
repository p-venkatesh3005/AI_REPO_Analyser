import chromadb

from backend.config import (
    CHROMA_DB_DIR,
    TOP_K
)


# Create persistent Chroma client
client = chromadb.PersistentClient(
    path=str(CHROMA_DB_DIR)
)

# Repository collection
collection = client.get_or_create_collection(
    name="repository_chunks"
)


def clear_vector_store():
    """
    Delete and recreate the repository_chunks collection to clear old data.
    """
    global collection
    try:
        client.delete_collection(name="repository_chunks")
        print("Deleted existing Chroma collection 'repository_chunks'.")
    except Exception as e:
        print(f"Chroma collection deletion skipped or failed: {e}")
    
    collection = client.create_collection(name="repository_chunks")
    print("Recreated empty Chroma collection 'repository_chunks'.")

def store_embeddings(embedded_data):
    """
    Store embeddings inside ChromaDB in batches to prevent timeouts/hanging and show progress.
    """
    batch_size = 500
    total_items = len(embedded_data)
    
    for i in range(0, total_items, batch_size):
        batch = embedded_data[i:i + batch_size]
        
        ids = []
        documents = []
        embeddings = []
        metadatas = []
        
        for item in batch:
            ids.append(str(item["chunk_id"]))
            documents.append(item["chunk_text"])
            embeddings.append(item["embedding"])
            metadatas.append({"file_path": item["file_path"]})
            
        collection.upsert(
            ids=ids,
            documents=documents,
            embeddings=embeddings,
            metadatas=metadatas
        )
        print(f"Stored batch {min(i + batch_size, total_items)}/{total_items} chunks in ChromaDB.")
        
    return total_items


def search_repository(
        question_embedding,
        top_k=TOP_K
):
    """
    Retrieve most relevant chunks.
    """

    results = collection.query(
        query_embeddings=[
            question_embedding
        ],
        n_results=top_k
    )

    return results