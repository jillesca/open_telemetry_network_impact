from netconf_parsers import Parser


def get_parser(netconf_filter: str) -> Parser:
    match netconf_filter:
        case "cisco_ex_ietf-interfaces.xml":
            from parsers.cisco_ex_ietf_interfaces import Interface_stats_iosxe

            return Interface_stats_iosxe()
