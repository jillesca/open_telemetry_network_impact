from netconf_client_utils import (
    read_file,
    parse_from_json,
    parse_to_json,
    parse_xml_to_dict,
)
from netconf_device import netconf_device
from netconf_session import connect_netconf_to
from intf_stats_xe_to_json import intf_stats_xe_to_json

DEVICES_SETTINGS = "./netconf_devices_settings.json"


def parse_result_to_json(device_data: dict) -> None:
    json_result = parse_to_json(device_data)
    print(json_result)


def parse_result_to_dict(device_data: dict) -> str:
    return intf_stats_xe_to_json(device_data)


def main():
    devices_settings = parse_from_json(read_file(DEVICES_SETTINGS))
    for device_setting in devices_settings:
        device_data_xml = connect_netconf_to(netconf_device(**device_setting))
        device_data_dict = parse_xml_to_dict(device_data_xml)
        device_data_parsed = parse_result_to_dict(device_data_dict)
        parse_result_to_json(device_data_parsed)


if __name__ == "__main__":
    main()
