import shutil
import zipfile
from pathlib import Path

from fastapi import (
    FastAPI,
    UploadFile,
    File
)

from fastapi.middleware.cors import (
    CORSMiddleware
)

from pydantic import BaseModel

from backend.config import (
    UPLOAD_DIR,
    EXTRACTED_REPO_DIR
)

from backend.rag_pipeline import (
    index_repository,
    ask_repository
)


# ======================
# APP INITIALIZATION
# ======================

app = FastAPI(
    title="AI Repository Explainer"
)


# ======================
# CORS
# ======================

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"]
)


# ======================
# CREATE DIRECTORIES
# ======================

UPLOAD_DIR.mkdir(
    exist_ok=True
)

EXTRACTED_REPO_DIR.mkdir(
    exist_ok=True
)


# ======================
# REQUEST MODEL
# ======================

class QuestionRequest(
    BaseModel
):
    question: str


# ======================
# HOME
# ======================

@app.get("/")
def home():

    return {
        "message":
        "Backend Running"
    }


# ======================
# UPLOAD REPOSITORY
# ======================

@app.post("/upload")
async def upload_repository(
    file: UploadFile = File(...)
):

    # Clear old uploads and extractions to prevent directory bloat and file mixing
    if UPLOAD_DIR.exists():
        try:
            shutil.rmtree(UPLOAD_DIR)
        except Exception as e:
            print(f"Error cleaning UPLOAD_DIR: {e}")
    UPLOAD_DIR.mkdir(exist_ok=True)

    if EXTRACTED_REPO_DIR.exists():
        try:
            shutil.rmtree(EXTRACTED_REPO_DIR)
        except Exception as e:
            print(f"Error cleaning EXTRACTED_REPO_DIR: {e}")
    EXTRACTED_REPO_DIR.mkdir(exist_ok=True)

    upload_path = (
        UPLOAD_DIR /
        file.filename
    )

    with open(
        upload_path,
        "wb"
    ) as buffer:

        shutil.copyfileobj(
            file.file,
            buffer
        )

    repo_name = (
        Path(
            file.filename
        ).stem
    )

    extract_path = (
        EXTRACTED_REPO_DIR /
        repo_name
    )

    with zipfile.ZipFile(
        upload_path,
        "r"
    ) as zip_ref:

        zip_ref.extractall(
            extract_path
        )

    chunk_count = (
        index_repository(
            str(
                extract_path
            )
        )
    )

    return {
        "message":
        f"{chunk_count} chunks indexed"
    }


# ======================
# ASK QUESTION
# ======================

@app.post("/ask")
def ask_question(
    request:
    QuestionRequest
):

    answer = (
        ask_repository(
            request.question
        )
    )

    return {
        "answer":
        answer
    }


# ======================
# HEALTH
# ======================

@app.get("/health")
def health():

    return {
        "status":
        "healthy"
    }