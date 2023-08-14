from collections import ChainMap
from dataclasses import dataclass
from netconf_parsers import Parser
from netconf_devices import netconf_device


@dataclass
class Interface_stats_iosxe_oper(Parser):
    device: netconf_device = None

    def parse(self, data: dict, device: netconf_device) -> list[dict]:
        self.device = device
        return self.interface_stats(data)

    def interface_stats(self, data: dict) -> list[dict]:
        stats: list = []
        interfaces: dict = data["rpc-reply"]["data"]["interfaces"]["interface"]

        for interface in interfaces:
            metadata = self.metadata(interface)
            intf_stats = self.statistics(interface["statistics"])
            stats.append(dict(ChainMap(metadata, intf_stats)))
        return stats

    def metadata(self, interface: dict) -> dict:
        return {
            "operational_status": 1 if interface["oper-status"] == "up" else 0,
            "name": interface["name"].replace(" ", "_"),
            "field": "intf_stats",
            "device": self.device.hostname,
            "ip": self.device.host,
        }

    def statistics(self, interface: dict) -> dict:
        return {
            "in_octets": int(interface["in-octets"]),
            "in_errors": int(interface["in-errors"]),
            "out_octets": int(interface["out-octets"]),
            "out_errors": int(interface["out-errors"]),
            "in-broadcast-pkts": int(interface["in-broadcast-pkts"]),
            "in-crc-errors": int(interface["in-crc-errors"]),
            "in-discards": int(interface["in-discards"]),
            "in-discards-64": int(interface["in-discards-64"]),
            "in-errors-64": int(interface["in-errors-64"]),
            "in-multicast-pkts": int(interface["in-multicast-pkts"]),
            "in-unicast-pkts": int(interface["in-unicast-pkts"]),
            "in-unknown-protos": int(interface["in-unknown-protos"]),
            "in-unknown-protos-64": int(interface["in-unknown-protos-64"]),
            "num-flaps": int(interface["num-flaps"]),
            "out-broadcast-pkts": int(interface["out-broadcast-pkts"]),
            "out-discards": int(interface["out-discards"]),
            "out-multicast-pkts": int(interface["out-multicast-pkts"]),
            "out-octets-64": int(interface["out-octets-64"]),
            "out-unicast-pkts": int(interface["out-unicast-pkts"]),
            "rx-kbps": int(interface["rx-kbps"]),
            "rx-pps": int(interface["rx-pps"]),
            "tx-kbps": int(interface["tx-kbps"]),
            "tx-pps": int(interface["tx-pps"]),
        }
