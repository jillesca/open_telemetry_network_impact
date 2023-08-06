from netconf_client_utils import (
    read_file,
    parse_from_json,
    parse_to_json,
    parse_xml_to_dict,
)
from netconf_device import netconf_device
from factory import get_parser
from netconf_session import connect

DEVICES_SETTINGS = "./netconf_devices_settings.json"
FILTER = "netconf_interface_stats.xml"
# NETCONF_INTERFACE_STATS = "/opt/netconf_client/netconf_interface_stats.xml"


def main():
    devices = load_settings(DEVICES_SETTINGS)
    for device in devices:
        data_xml = connect(netconf_device(**device), FILTER)
        data_dict = parse_xml_to_dict(data_xml)
        parser = get_parser(FILTER)
        data_parsed = parser.parse(data_dict)
        parse_result_to_json(data_parsed)


def load_settings(settings: str):
    return parse_from_json(read_file(settings))


def parse_result_to_json(data: dict) -> None:
    json_result = parse_to_json(data)
    assert parse_from_json(json_result)
    print(json_result)


if __name__ == "__main__":
    main()
