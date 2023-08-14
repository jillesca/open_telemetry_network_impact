from netconf_parsers import Parser


def get_parser(netconf_filter: str) -> Parser:
    match netconf_filter:
        case "cisco_xe_ietf-interfaces.xml":
            from parsers.cisco_ex_ietf_interfaces import Interface_stats_iosxe

            return Interface_stats_iosxe()

        case "Cisco-IOS-XE-interfaces-oper.xml":
            from parsers.cisco_ios_xe_interfaces_oper import Interface_stats_iosxe_oper

            return Interface_stats_iosxe_oper()

        case "Cisco-IOS-XE-memory-oper.xml":
            from parsers.cisco_ios_xe_memory_oper import Cisco_ios_xe_memory_oper

            return Cisco_ios_xe_memory_oper()
