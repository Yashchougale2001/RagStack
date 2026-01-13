import yaml
from src.loader.loader import load_text, chunk_text, chunk_csv_rows
from src.db.vector_store import create_vector_store, add_chunks_to_db

with open("config.yaml") as f:
    config = yaml.safe_load(f)

collection = create_vector_store(embedding_model=config["embedding_model"])
print("Starting ingestion...")

# TXT ingestion
# txt = load_text("data/knowledge.txt")
# txt_chunks = chunk_text(txt, config["chunk_size"], config["overlap"])
# add_chunks_to_db(collection, txt_chunks, source="txt", domain="general")

# CSV ingestion
# csv_chunks = chunk_csv_rows("data/hr_data.csv")
csv_chunks = chunk_csv_rows("data/hospital_data.csv")
add_chunks_to_db(collection, csv_chunks, source="csv", domain="hospital")