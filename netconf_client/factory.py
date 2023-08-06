from netconf_parsers import Parser


def get_parser(netconf_filter: str) -> Parser:
    match netconf_filter:
        case "netconf_interface_stats.xml":
            from parsers.interface_stats_iosxe import Interface_stats_iosxe

            return Interface_stats_iosxe()
