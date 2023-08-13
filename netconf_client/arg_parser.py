import argparse


def get_arg_parser():
    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group(required=True)
    parser.add_argument(
        "--device_settings",
        default="netconf_devices_settings.json",
        help="Device Settings in json fomat. Eg. 'netconf_devices_settings.json'",
    )
    group.add_argument(
        "--xml_filter",
        help="Netconf Filter to apply in xml format. Eg. 'cisco_xe_ietf-interfaces.xml'",
    )
    group.add_argument(
        "--xpath_filter",
        help="Netconf Filter to apply in xpath. Formats: <xpath> OR <namespace>:<xpath> Eg. 'interfaces/interface' OR 'http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper:interfaces/interface' xpath is used as ID internally. ",
    )
    return parser
