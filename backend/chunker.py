from langchain_text_splitters import (
    RecursiveCharacterTextSplitter
)

from backend.config import (
    CHUNK_SIZE,
    CHUNK_OVERLAP
)


def chunk_repository_data(repository_data):

    splitter = (
        RecursiveCharacterTextSplitter(
            chunk_size=CHUNK_SIZE,
            chunk_overlap=CHUNK_OVERLAP
        )
    )

    chunks = []

    chunk_id = 0

    for file_data in repository_data:

        split_result = splitter.split_text(
            file_data["content"]
        )

        for chunk in split_result:

            chunks.append(
                {
                    "chunk_id": chunk_id,
                    "file_path": file_data["file_path"],
                    "chunk_text": chunk
                }
            )

            chunk_id += 1

    return chunks