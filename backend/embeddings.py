import backend.utils as utils

from sentence_transformers import (
    SentenceTransformer
)

from backend.config import (
    EMBEDDING_MODEL_NAME
)


# Initialize embedding model
embedding_model = (
    SentenceTransformer(
        EMBEDDING_MODEL_NAME
    )
)


def generate_embeddings(
        chunks
):
    """
    Generate embeddings for repository chunks using local SentenceTransformer.
    """

    if not chunks:

        return []

    texts = [
        chunk["chunk_text"]
        for chunk in chunks
    ]

    # Encode all texts once for performance
    embeddings = (
        embedding_model
        .encode(
            texts,
            convert_to_numpy=True,
            show_progress_bar=True,
            batch_size=128
        )
    )

    embeddings = embeddings.tolist()

    embedded_chunks = []

    for chunk, vector in zip(
        chunks,
        embeddings
    ):

        embedded_chunks.append(
            {
                "chunk_id": chunk["chunk_id"],
                "file_path": chunk["file_path"],
                "chunk_text": chunk["chunk_text"],
                "embedding": vector
            }
        )

    return embedded_chunks

