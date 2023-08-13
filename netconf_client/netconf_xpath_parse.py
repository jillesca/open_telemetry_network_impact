import re


def get_xpath(netconf_filter: str) -> tuple():
    if ":" not in netconf_filter:
        return ("xpath", netconf_filter)
    elif "http://" or "https://" in netconf_filter:
        ns_xpath = re.search(r"(https*:\/\/\S+):(\S+)", netconf_filter)
        ns = ns_xpath.group(1)
        select = ns_xpath.group(2)
        return ("xpath", ({"ns0": ns}, select))
    else:
        ns, select = netconf_filter.split(":")
        return ("xpath", ({"ns0": ns}, select))
