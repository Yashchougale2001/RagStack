# import csv

# def load_text(file_path):
#     with open(file_path, "r", encoding="utf-8") as f:
#         return f.read()

# def load_csv_as_text(file_path, columns=None):
#     """Convert CSV rows into structured text."""
#     rows_as_text = []
#     with open(file_path, "r", encoding="utf-8") as f:
#         reader = csv.DictReader(f)
#         for row in reader:
#             parts = []
#             for col, val in row.items():
#                 if val and val.strip() and (columns is None or col in columns):
#                     parts.append(f"{col}: {val.strip()}")
#             if parts:
#                 rows_as_text.append(" | ".join(parts))
#     return "\n".join(rows_as_text)

# def chunk_text(text, chunk_size=200, overlap=40):
#     words = text.split()
#     chunks = []
#     start = 0
#     while start < len(words):
#         end = start + chunk_size
#         chunks.append(" ".join(words[start:end]))
#         start += chunk_size - overlap
#     return chunks

# def chunk_csv_rows(file_path):
#     chunks = []
#     with open(file_path, "r", encoding="utf-8") as f:
#         reader = csv.DictReader(f)
#         for i, row in enumerate(reader, start=1):
#             text = f"Row {i}:\n" + "\n".join([f"- {k}: {v}" for k, v in row.items()])
#             chunks.append(text)
#     return chunks
