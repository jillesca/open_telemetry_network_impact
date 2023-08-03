import json
from typing import Dict

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

    return json.dumps(intf_stats_array) 