from file_utils import (
    read_file,
    find_filter_path,
)
from arg_parser import get_arg_parser
from netconf_xpath_parse import get_xpath


class parse_settings:
    def __init__(self) -> None:
        self._filter_id: str
        self._net_filter: any
        self._devices_settings: str
        self._get_arguments()

    def _get_arguments(self) -> None:
        args = get_arg_parser().parse_args()
        self._devices_settings = args.device_settings
        if args.xml_filter:
            self._parse_xml(args.xml_filter)
        elif args.xpath_filter:
            self._parse_xpath(args.xpath_filter)

    def get_device_settings(self) -> str:
        return self._devices_settings

    def get_filter_id(self) -> str:
        return self._filter_id

    def get_net_filter(self) -> any:
        return self._net_filter

    def _parse_xml(self, filter_id: str) -> None:
        if ".xml" not in filter_id:
            raise ValueError('no XML extension detected in filter')
        self._filter_id = filter_id
        self._net_filter = read_file(find_filter_path(filter_id))

    def _parse_xpath(self, filter_id: str) -> None:
        self._filter_id = filter_id
        self._net_filter = get_xpath(filter_id)
