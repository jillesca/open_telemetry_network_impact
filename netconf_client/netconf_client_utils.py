import os
import json
import xmltodict


def read_file(file: str) -> str:
    with open(file, "r") as f:
        return f.read()


def parse_from_json(file: str) -> dict:
    return json.loads(file)


def parse_xml_to_dict(xml: str) -> dict:
    return xmltodict.parse(xml.xml)


def parse_to_json(data: str) -> str:
    return json.dumps(data)


def get_absolute_path(file) -> str:
    return os.path.abspath(os.path.dirname(file))
