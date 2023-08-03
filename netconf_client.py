from typing import Dict
from ncclient import manager
import xmltodict
import json

def dict_to_telegraf_json(rpc_reply_dict: Dict) -> str:

    intf_stats_array = []
    for intf_entry in rpc_reply_dict["rpc-reply"]["data"]["interfaces-state"]["interface"]:
        intf_stats = {}
        intf_name = intf_entry["name"].replace(" ", "_")
        intf_stats = {
            "operational_status": 1 if intf_entry["oper-status"]=="up" else 0,
            "in_octets": int(intf_entry["statistics"]["in-octets"]),
            "in_errors": int(intf_entry["statistics"]["in-errors"]),
            "out_octets": int(intf_entry["statistics"]["out-octets"]),
            "out_errors": int(intf_entry["statistics"]["out-errors"]),
            "name": intf_name,
            "field": "intf_stats"
        }
        intf_stats_array.append(intf_stats)

    return json.dumps(intf_stats_array)  # return JSON formatted data


def main():
    with manager.connect(
        host = "10.10.20.175",  # sandbox ios-xe always on
        port = 830,
        username = "cisco",
        password = "cisco",  # enter device password
        hostkey_verify=False,
        device_params = {'name': 'iosxe'}
    ) as m:
        # https://github.com/YangModels/yang/blob/master/vendor/cisco/xe/16111/ietf-interfaces.yang
        netconf_filter = """
        <filter xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">
                <interfaces-state xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces">
                        <interface>
                                <name/>
                                <type/>
                                <oper-status/>
                                <statistics>
                                        <in-octets/>
                                        <in-errors/>
                                        <out-octets/>
                                        <out-errors/>
                                </statistics>
                        </interface>
                </interfaces-state>
        </filter>
        """

        netconf_rpc_reply = m.get(
            filter = netconf_filter
        ).xml

        netconf_reply_dict = xmltodict.parse(netconf_rpc_reply)
        
        telegraf_json_input = dict_to_telegraf_json(netconf_reply_dict)

        # telegraf needs data in a certain data format.
        # I have chosen JSON data that will be picked up by the exec plugin
        print(telegraf_json_input)


if __name__ == "__main__":
    main()
