# import yaml
# from src.loader.loader import load_text, chunk_text, chunk_csv_rows
# from src.db.vector_store import create_vector_store, add_chunks_to_db

# with open("config.yaml") as f:
#     config = yaml.safe_load(f)

# collection = create_vector_store(embedding_model=config["embedding_model"])
# print("Starting ingestion...")

# # TXT ingestion
# # txt = load_text("data/knowledge.txt")
# # txt_chunks = chunk_text(txt, config["chunk_size"], config["overlap"])
# # add_chunks_to_db(collection, txt_chunks, source="txt", domain="general")

# # CSV ingestion
# csv_chunks = chunk_csv_rows("data/hr_data.csv")
# # csv_chunks = chunk_csv_rows("data/hospital_data.csv")
# add_chunks_to_db(collection, csv_chunks, source="csv", domain="hr")
# print("✅Ingestion completed.")


import yaml
import os

from src.loader.folder_ingestor import ingest_folder
from src.db.vector_store import create_vector_store, add_chunks_to_db

def run_ingestion():
    # Load config
    with open("config.yaml", "r") as f:
        config = yaml.safe_load(f)

    base_path = config.get("data_path", "data")     # folder to scan
    chunk_size = config.get("chunk_size", 400)
    overlap = config.get("overlap", 80)

    print("🚀 Starting ingestion...")
    print(f"📁 Scanning folder: {base_path}")

    # Initialize vector store
    collection = create_vector_store(embedding_model=config["embedding_model"])

    # Walk folder + load all files
    ingested = ingest_folder(
        folder_path=base_path,
        chunk_size=chunk_size,
        overlap=overlap
    )

    if not ingested:
        print("⚠️ No files ingested. Check folder path.")
        return

    # Store into ChromaDB
    for item in ingested:
        add_chunks_to_db(
            collection=collection,
            chunks=item["chunks"],
            source=item["extension"],           # .csv / .txt / .pdf
            domain=os.path.basename(os.path.dirname(item["file_path"])),  
            # domain = folder name
        )

    print(f"✅ Ingestion completed. Total files processed: {len(ingested)}")


if __name__ == "__main__":
    run_ingestion()

