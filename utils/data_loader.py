import csv
import json
from pathlib import Path

def load_data(filename):

    base_path = Path(__file__).parent.parent.resolve() / "data"
    file_path = base_path / filename

    if not file_path.exists():
        raise FileNotFoundError(f"❌ File not found: {file_path}")

    if filename.endswith(".csv"):
        with open(file_path, newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            return [row for row in reader]

    elif filename.endswith(".json"):
        with open(file_path, encoding="utf-8") as f:
            return json.load(f)

    else:
        raise ValueError("Format file tidak didukung. Gunakan CSV atau JSON")
    
    return file_path