from pathlib import Path

# =========================
# PROJECT ROOT DIRECTORY
# =========================

BASE_DIR = Path(__file__).resolve().parent.parent


# =========================
# STORAGE DIRECTORIES
# =========================

UPLOAD_DIR = BASE_DIR / "uploads"

EXTRACTED_REPO_DIR = BASE_DIR / "extracted_repos"

CHROMA_DB_DIR = BASE_DIR / "chroma_storage"


SUPPORTED_EXTENSIONS = [
    ".py",
    ".js",
    ".ts",
    ".jsx",
    ".tsx",
    ".md",
    ".txt",
    ".html",
    ".css",
    ".json",
    ".yaml",
    ".yml",
    ".toml",
    ".ini",
    ".sql",
    ".sh",
    ".bat",
    ".java",
    ".cpp",
    ".c",
    ".h",
    ".cs",
    ".go"
]


# =========================
# CHUNKING CONFIGURATION
# =========================

CHUNK_SIZE = 1000

CHUNK_OVERLAP = 200

TOP_K = 10



# =========================
# EMBEDDING MODEL
# =========================

EMBEDDING_MODEL_NAME = "all-MiniLM-L6-v2"


# =========================
# GEMINI MODEL
# =========================

GEMINI_MODEL_NAME = "gemini-3.1-flash-lite"