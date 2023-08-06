from netconf_filter import Filter_call


def get_parser(netconf_filter: str) -> Filter_call:
    match netconf_filter:
        case "netconf_interface_stats.xml":
            from parsers.stats import Interface_stats_iosxe

            return Interface_stats_iosxe()
