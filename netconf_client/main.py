from netconf_client_utils import (
    read_file,
    parse_from_json,
    parse_to_json,
    parse_xml_to_dict,
    get_absolute_path,
)
from netconf_device import create_device
from factory import get_parser
from netconf_session import connect

DEVICES_SETTINGS = "netconf_devices_settings.json"
NETCONF_FILTER = "netconf_interface_stats.xml"


def main():
    devices = load_settings(DEVICES_SETTINGS)
    for device in devices:
        data_xml = connect(create_device(**device), NETCONF_FILTER)
        data_dict = parse_xml_to_dict(data_xml)
        parser = get_parser(NETCONF_FILTER)
        data_parsed = parser.parse(data_dict)
        parse_result_to_json(data_parsed)


def load_settings(file: str):
    file_path = f"{get_absolute_path(file)}/{file}"
    return parse_from_json(read_file(file_path))


def parse_result_to_json(data: dict) -> None:
    json_result = parse_to_json(data)
    assert parse_from_json(json_result)
    print(json_result)


if __name__ == "__main__":
    main()
