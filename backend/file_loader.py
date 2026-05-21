from pathlib import Path

from backend.config import SUPPORTED_EXTENSIONS

# Common directories to completely ignore during indexing
IGNORED_DIRS = {
    "venv", ".venv", "node_modules", "bower_components", 
    ".git", "__pycache__", ".vscode", ".idea", 
    "third-party", "vendor"
}


def load_repository_files(repo_path: str):
    """
    Load all supported files from repository. Skips common ignored directories,
    third-party libraries, and test files for optimal performance and cleaner RAG context.
    """

    repository_data = []

    repo_path = Path(repo_path)

    # Traverse all files recursively
    for file_path in repo_path.rglob("*"):

        # Skip directories
        if file_path.is_dir():
            continue

        # Get components of the relative path to check for ignored directories
        try:
            rel_path = file_path.relative_to(repo_path)
            parts = rel_path.parts
        except ValueError:
            # Fallback if path construction is outside repo_path
            continue

        # Skip files in ignored directories or hidden directories (starting with .)
        if any(part.lower() in IGNORED_DIRS or part.startswith(".") for part in parts):
            continue

        # Skip test files and directories (to satisfy user request of removing/excluding tests)
        if any("test" in part.lower() for part in parts):
            continue

        # Check supported extensions
        if file_path.suffix not in SUPPORTED_EXTENSIONS:
            continue

        try:
            # Read file content
            content = file_path.read_text(
                encoding="utf-8",
                errors="ignore"
            )

            # Skip empty files
            if not content.strip():
                continue

            repository_data.append(
                {
                    "file_path": str(rel_path),
                    "content": content
                }
            )

        except Exception as error:
            print(f"Error reading file {file_path}: {error}")

    return repository_data