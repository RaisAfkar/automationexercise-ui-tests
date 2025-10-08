import json, csv
from pathlib import Path

def save_data(filename, data):
    base_path = Path(__file__).parent.parent.resolve() / "data"
    base_path.mkdir(parents=True, exist_ok=True)
    file_path = base_path / filename

    if filename.endswith(".json"):
        with open(file_path,"w",encoding="utf-8") as j:
            json.dump(data, j, indent=2)
    
    elif filename.endswith(".csv"):
        with open(file_path,"w",newline="",encoding="utf-8") as c:
            writer = csv.DictWriter(c, fieldnames=data[0].keys())
            writer.writeheader()
            writer.writerows(data)
    
    elif filename.endswith(".txt"):
        with open(file_path,"w",encoding="utf-8") as t:
            t.write(data)
    
    else:
        raise ValueError("Using format data file txt, csv, and json")
    
    return file_path