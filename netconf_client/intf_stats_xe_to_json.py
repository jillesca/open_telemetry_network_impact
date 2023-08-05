def intf_stats_xe_to_json(rpc_reply: dict) -> str:
    stats: list = []
    for intf_entry in rpc_reply["rpc-reply"]["data"]["interfaces-state"]["interface"]:
        stats.append(sort_stats(intf_entry))
    return stats


def sort_stats(entry: dict) -> dict:
    return {
        "operational_status": 1 if entry["oper-status"] == "up" else 0,
        "in_octets": int(entry["statistics"]["in-octets"]),
        "in_errors": int(entry["statistics"]["in-errors"]),
        "out_octets": int(entry["statistics"]["out-octets"]),
        "out_errors": int(entry["statistics"]["out-errors"]),
        "name": entry["name"].replace(" ", "_"),
        "field": "intf_stats",
    }
