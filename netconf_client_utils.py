from typing import Dict
import json

def read_file(file: str) -> str:
    with open(file, "r") as f:
        return f.read()

def parse_from_json(file: str) -> Dict:
    return json.loads(file)
