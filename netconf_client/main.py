from file_utils import (
    read_file,
    find_devices_path,
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
from netconf_session import netconf_handler
from netconf_settings import parse_settings


def netconf_client() -> None:
    settings = parse_settings()
    devices_settings = settings.get_device_settings()
    netconf_filter_id = settings.get_filter_id()
    netconf_filter = settings.get_net_filter()

    devices = load_settings(devices_settings)

    results = []
    for device in devices:
        net_device = netconf_device(**device)
        connection = netconf_handler(net_device)
        data_xml = connection.rpc_get(netconf_filter)
        data_dict = parse_xml_to_dict(data_xml)
        parser = get_parser(remove_path(netconf_filter_id))
        data_parsed = parser.parse(data_dict, net_device)
        results += data_parsed

    parsed_results = parse_results_to_json(results)
    print(parsed_results)


def load_settings(file: str) -> dict:
    file_path = find_devices_path(file)
    return parse_from_json(read_file(file_path))


def parse_results_to_json(data: any) -> str:
    result = parse_to_json(data)
    assert parse_from_json(result)
    return result


def main() -> None:
    netconf_client()


if __name__ == "__main__":
    main()
