from netconf_parsers import Parser


def get_parser(netconf_filter: str) -> Parser:
    match netconf_filter:
        case "cisco_xe_ietf-interfaces.xml":
            from parsers.cisco_xe_ietf_interfaces import Interface_stats_ietf_iosxe

            return Interface_stats_ietf_iosxe()

        case "Cisco-IOS-XE-interfaces-oper.xml":
            from parsers.cisco_ios_xe_interfaces_oper import Interface_stats_iosxe_oper

            return Interface_stats_iosxe_oper()

        case "Cisco-IOS-XE-memory-oper.xml":
            from parsers.cisco_ios_xe_memory_oper import Cisco_ios_xe_memory_oper

            return Cisco_ios_xe_memory_oper()

        case "http://cisco.com/ns/yang/Cisco-IOS-XE-isis-oper:/isis-oper-data/isis-instance":
            from parsers.cisco_ios_xe_isis_oper import isis_stats_iosxe_oper

            return isis_stats_iosxe_oper()
