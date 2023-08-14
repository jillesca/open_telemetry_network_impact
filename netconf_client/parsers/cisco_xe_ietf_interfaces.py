from netconf_parsers import Parser
from netconf_devices import netconf_device


class Interface_stats_ietf_iosxe(Parser):
    def parse(self, data_to_parse: dict, net_device: netconf_device) -> list[dict]:
        self.net_device = net_device
        return self.intf_stats_xe_to_json(data_to_parse)

    def intf_stats_xe_to_json(self, rpc_reply: dict) -> list[dict]:
        stats: list = []
        xpath: dict = rpc_reply["rpc-reply"]["data"]["interfaces-state"]["interface"]

        for intf_entry in xpath:
            stats.append(self.sort_stats(intf_entry))
        return stats

    def sort_stats(self, entry: dict) -> dict:
        return {
            "operational_status": 1 if entry["oper-status"] == "up" else 0,
            "in_octets": int(entry["statistics"]["in-octets"]),
            "in_errors": int(entry["statistics"]["in-errors"]),
            "out_octets": int(entry["statistics"]["out-octets"]),
            "out_errors": int(entry["statistics"]["out-errors"]),
            "name": entry["name"].replace(" ", "_"),
            "field": "intf_stats",
            "device": self.net_device.hostname,
            "ip": self.net_device.host,
        }
