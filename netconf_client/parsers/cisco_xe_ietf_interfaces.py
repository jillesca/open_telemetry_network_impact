from dataclasses import dataclass
from netconf_parsers import Parser
from netconf_devices import netconf_device


@dataclass
class Interface_stats_ietf_iosxe(Parser):
    device: netconf_device = None

    def parse(self, data: dict, device: netconf_device) -> list[dict]:
        self.device = device
        return self.interface_stats(data)

    def interface_stats(self, data: dict) -> list[dict]:
        stats: list = []
        interfaces: dict = data["rpc-reply"]["data"]["interfaces-state"]["interface"]

        for interface in interfaces:
            stats.append(self.statistics(interface))
        return stats

    def statistics(self, interface: dict) -> dict:
        return {
            "operational_status": 1 if interface["oper-status"] == "up" else 0,
            "in_octets": int(interface["statistics"]["in-octets"]),
            "in_errors": int(interface["statistics"]["in-errors"]),
            "out_octets": int(interface["statistics"]["out-octets"]),
            "out_errors": int(interface["statistics"]["out-errors"]),
            "name": interface["name"].replace(" ", "_"),
            "field": "intf_stats",
            "device": self.device.hostname,
            "ip": self.device.host,
        }
