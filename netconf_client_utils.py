from typing import Dict
import xmltodict
import json

def read_file(file: str) -> str:
    with open(file, "r") as f:
        return f.read()

def parse_from_json(file: str) -> Dict:
    return json.loads(file)

def parse_xml_to_dict(xml: str) -> Dict:
    return xmltodict.parse(xml.xml)