import json
from pathlib import Path

# Logic: Find the exact folder where THIS file sits
BASE_DIR = Path(__file__).parent
DATA_FILE = BASE_DIR / "students.json"

def load_data():
    """Reads data from the JSON file. Returns an empty list if file doesn't exist."""
    if DATA_FILE.exists():
        with open(DATA_FILE, "r") as f:
            try:
                return json.load(f)
            except json.JSONDecodeError:
                # If the file is empty or corrupted, return an empty list
                return []
    return []

def save_data(data):
    """Writes the provided list/dictionary data into the JSON file."""
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=4)