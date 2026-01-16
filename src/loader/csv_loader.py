import csv

def load_csv(file_path, columns=None):
    """Load CSV file and convert rows to text format."""
    rows = []
    with open(file_path, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for i, row in enumerate(reader, start=1):
            parts = []
            for col, val in row.items():
                if val and val.strip() and (columns is None or col in columns):
                    parts.append(f"{col}: {val.strip()}")
            if parts:
                rows.append(f"Row {i}: " + " | ".join(parts))

    return "\n".join(rows)
