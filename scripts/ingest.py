from pathlib import Path
from langchain_text_splitters import MarkdownHeaderTextSplitter, RecursiveCharacterTextSplitter
from langchain_core.documents import Document

KNOWLEDGE_BASE_DIR = Path(__file__).resolve().parent.parent / "data" / "knowledge_base"
CHUNK_SIZE = 1300
CHUNK_OVERLAP = 150
HEADERS_TO_SPLIT_ON = [
    ("#", "h1"),
    ("##", "h2"),
    ("###", "h3"),
]

def load_files(directory: Path):
    files = sorted(directory.glob("*.md"))
    if not files:
        raise FileNotFoundError(f"No .md files found in {directory}")

    loaded = []
    for file_path in files:
        text = file_path.read_text(encoding="utf-8")
        loaded.append((file_path.name, text))
    return loaded

def split_into_chunks(filename: str, text: str):

    header_splitter = MarkdownHeaderTextSplitter(
        headers_to_split_on=HEADERS_TO_SPLIT_ON,
        strip_headers=False,
    )
    header_chunks = header_splitter.split_text(text)

    char_splitter = RecursiveCharacterTextSplitter(
        chunk_size=CHUNK_SIZE,
        chunk_overlap=CHUNK_OVERLAP,
    )

    final_chunks = []

    for chunk in header_chunks:
        chunk.metadata["source"] = filename

        if len(chunk.page_content) <= CHUNK_SIZE:
            final_chunks.append(chunk)
        else:
            sub_chunks = char_splitter.split_documents([chunk])
            final_chunks.extend(sub_chunks)

    return final_chunks

def build_all_chunks():
    all_chunks = []
    for filename, text in load_files(KNOWLEDGE_BASE_DIR):
        chunks = split_into_chunks(filename, text)
        all_chunks.extend(chunks)
    return all_chunks

if __name__ == "__main__":
    chunks = build_all_chunks()
    print(f"Loaded and chunked {len(chunks)} chunks total.\n")

    counts: dict[str, int] = {}
    for c in chunks:
        counts[c.metadata["source"]] = counts.get(c.metadata["source"], 0) + 1

    print("Chunks per file:")
    for filename, count in counts.items():
        print(f"  {filename}: {count} chunks")

    print("\n--- Sample chunk ---")
    sample = chunks[0]
    print("Metadata:", sample.metadata)
    print("Content preview:")
    print(sample.page_content[:300])