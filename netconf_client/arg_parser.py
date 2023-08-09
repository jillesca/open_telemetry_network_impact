import argparse


def get_arg_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--device_settings",
        default="netconf_devices_settings.json",
        help="Device Settings in json fomat",
    )
    parser.add_argument(
        "--netconf_filter",
        required=True,
        # default="netconf_interface_stats.xml",
        help="Netconf Filter to apply in xml format",
    )
    return parser
