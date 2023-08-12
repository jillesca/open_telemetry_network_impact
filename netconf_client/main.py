from file_utils import (
    read_file,
    find_devices_path,
    find_filter_path,
    remove_path,
    write_to_file,
)
from text_utils import (
    parse_from_json,
    parse_to_json,
    parse_xml_to_dict,
)
from netconf_devices import netconf_device
from factory import get_parser
from netconf_session import connect
from arg_parser import get_arg_parser

LOG_FILE = "/tmp/netconf_client.log"


def main():
    args_parser = get_arg_parser()
    args = args_parser.parse_args()

    devices_settings = args.device_settings
    netconf_filter_id = args.xml_filter

    netconf_filter = find_filter_path(netconf_filter_id)
    devices = load_settings(devices_settings)

    results = []
    for device in devices:
        net_device = netconf_device(**device)
        data_xml = connect(net_device, netconf_filter)
        data_dict = parse_xml_to_dict(data_xml)
        parser = get_parser(remove_path(netconf_filter_id))
        data_parsed = parser.parse(data_dict, net_device)
        results += data_parsed

    parsed_results = parse_results_to_json(results)
    write_to_file(file=LOG_FILE, text="\n")
    write_to_file(file=LOG_FILE, text="#" * 50)
    write_to_file(file=LOG_FILE, text="\n")
    write_to_file(file=LOG_FILE, text=parsed_results)
    write_to_file(file=LOG_FILE, text="\n")
    print(parsed_results)


def load_settings(file: str):
    file_path = find_devices_path(file)
    return parse_from_json(read_file(file_path))


def parse_results_to_json(data: any) -> str:
    result = parse_to_json(data)
    assert parse_from_json(result)
    return result


if __name__ == "__main__":
    main()
