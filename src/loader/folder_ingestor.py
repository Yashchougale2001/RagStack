import os
from src.loader.file_router import load_file, is_supported_file
from src.loader.chunker import chunk_text

def ingest_folder(folder_path, chunk_size=400, overlap=80):
    """
    Walks through folder recursively.
    Loads each supported file, chunks it, and returns:
    
    [
        {
            "chunks": [...],
            "file_path": "...",
            "extension": ".csv",
            "domain": "... (optional)",
        },
        ...
    ]
    """

    ingested_data = []

    for root, dirs, files in os.walk(folder_path):
        for file in files:
            full_path = os.path.join(root, file)

            if not is_supported_file(full_path):
                continue  # skip unsupported types

            try:
                raw_text = load_file(full_path)
                chunks = chunk_text(raw_text, chunk_size, overlap)

                ingested_data.append({
                    "file_path": full_path,
                    "extension": os.path.splitext(file)[1].lower(),
                    "chunks": chunks
                })

                print(f"✓ Loaded & chunked: {full_path} ({len(chunks)} chunks)")

            except Exception as e:
                print(f"⚠️ Failed: {full_path} | Error: {e}")

    return ingested_data
