import os
from src.loader.csv_loader import load_csv
from src.loader.txt_loader import load_txt
from src.loader.pdf_loader import load_pdf

SUPPORTED_EXT = [".csv", ".txt", ".pdf"]

def load_file(file_path):
    ext = os.path.splitext(file_path)[1].lower()

    if ext == ".csv":
        return load_csv(file_path)

    elif ext == ".txt":
        return load_txt(file_path)

    elif ext == ".pdf":
        return load_pdf(file_path)

    else:
        raise ValueError(f"Unsupported file type: {ext}")


def is_supported_file(file_path):
    ext = os.path.splitext(file_path)[1].lower()
    return ext in SUPPORTED_EXT
