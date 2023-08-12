import argparse


def get_arg_parser():
    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group(required=True)
    parser.add_argument(
        "--device_settings",
        default="netconf_devices_settings.json",
        help="Device Settings in json fomat",
    )
    group.add_argument(
        "--xml_filter",
        help="Netconf Filter to apply in xml format",
    )
    group.add_argument(
        "--xpath_filter",
        help="Netconf Filter to apply in xpath format, see https://github.com/ncclient/ncclient/pull/405 for an example",
    )
    return parser
