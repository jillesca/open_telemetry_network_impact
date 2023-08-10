from file_utils import (
    read_file,
    get_file,
    find_filter_path,
    remove_path,
)
from text_utils import (
    parse_from_json,
    parse_to_json,
    parse_xml_to_dict,

)
from netconf_device import create_device
from factory import get_parser
from netconf_session import connect
from arg_parser import get_arg_parser



def main():
    args_parser = get_arg_parser()
    args = args_parser.parse_args()

    devices_settings = args.device_settings
    netconf_filter_id = args.netconf_filter

    netconf_filter = find_filter_path(netconf_filter_id) 
    devices = load_settings(devices_settings)

    results = []
    for device in devices:
        data_xml = connect(create_device(**device), netconf_filter)
        data_dict = parse_xml_to_dict(data_xml)
        parser = get_parser(remove_path(netconf_filter_id))
        data_parsed = parser.parse(data_dict)
        results += data_parsed

    print(parse_results_to_json(results))


def load_settings(file: str):
    file_path = get_file(file)
    return parse_from_json(read_file(file_path))


def parse_results_to_json(data: any) -> str:
    result = parse_to_json(data)
    assert parse_from_json(result)
    return result


if __name__ == "__main__":
    main()
