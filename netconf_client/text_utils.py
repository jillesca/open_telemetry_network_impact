import json
import xmltodict



def parse_from_json(file: str) -> dict:
    return json.loads(file)


def parse_xml_to_dict(xml: str) -> dict:
    return xmltodict.parse(xml.xml)


def parse_to_json(data: str) -> str:
    return json.dumps(data)
