from backend.file_loader import (
    load_repository_files
)

from backend.chunker import (
    chunk_repository_data
)

import backend.embeddings as embeddings

from backend.vector_store import (
    store_embeddings,
    search_repository,
    clear_vector_store
)

from backend.llm_handler import (
    generate_answer
)

def safe_print(*args, **kwargs):
    import builtins
    try:
        builtins.print(*args, **kwargs)
    except UnicodeEncodeError:
        safe_args = [
            str(arg).encode('ascii', errors='replace').decode('ascii')
            for arg in args
        ]
        builtins.print(*safe_args, **kwargs)

# Override print with safe_print in this module scope
print = safe_print


def index_repository(
        repository_path
):
    """
    Process repository
    and store vectors.
    """

    print("\n=== INDEXING START ===")

    # Clear old database chunks first to ensure a clean slate for the new repository
    clear_vector_store()

    # Load repository files
    files = (
        load_repository_files(
            repository_path
        )
    )

    if not files:

        raise Exception(
            "No supported files found."
        )

    print(
        f"Files Loaded: {len(files)}"
    )

    # Chunk repository
    chunks = (
        chunk_repository_data(
            files
        )
    )

    print(
        f"Chunks Created: {len(chunks)}"
    )

    # Generate embeddings
    embedded = (
        embeddings
        .generate_embeddings(
            chunks
        )
    )

    print(
        f"Embeddings Generated: "
        f"{len(embedded)}"
    )

    # Store vectors
    stored_count = (
        store_embeddings(
            embedded
        )
    )

    print(
        f"Stored: {stored_count}"
    )

    print(
        "=== INDEX COMPLETE ==="
    )

    return stored_count


def ask_repository(
        question
):
    """
    Ask repository questions.
    """

    print(
        "\n=== QUESTION ==="
    )

    print(question)

    # Generate question embedding
    question_embedding = (
        embeddings
        .embedding_model
        .encode(
            question
        )
        .tolist()
    )

    print(
        "Question Embedded"
    )

    # Retrieve chunks
    results = (
        search_repository(
            question_embedding
        )
    )

    print(
        "\nRetrieved Results:"
    )

    print(results)

    documents = (
        results
        .get(
            "documents",
            [[]]
        )[0]
    )

    metadatas = (
        results
        .get(
            "metadatas",
            [[]]
        )[0]
    )

    if not documents:

        return (
            "No relevant repository "
            "content found."
        )

    # Build context
    context = ""

    for doc, meta in zip(
        documents,
        metadatas
    ):

        file_name = (
            meta.get(
                "file_path",
                "unknown"
            )
        )

        context += (
            f"\nFile: "
            f"{file_name}\n\n"

            f"{doc}\n"
        )

    print(
        "\nContext Prepared"
    )

    # Generate final answer
    response = (
        generate_answer(
            question,
            context
        )
    )

    print(
        "\nAnswer Generated"
    )

    return response