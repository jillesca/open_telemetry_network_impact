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
from arg_parser import get_arg_parser


def main():
    args_parser = get_arg_parser()
    args = args_parser.parse_args()

    devices_settings = args.device_settings
    netconf_filter = args.netconf_filter

    devices = load_settings(devices_settings)
    for device in devices:
        data_xml = connect(create_device(**device), netconf_filter)
        data_dict = parse_xml_to_dict(data_xml)
        parser = get_parser(netconf_filter)
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
