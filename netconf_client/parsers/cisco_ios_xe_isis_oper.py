from dataclasses import dataclass
from netconf_parsers import Parser
from netconf_devices import netconf_device


@dataclass
class isis_stats_iosxe_oper(Parser):
    device: netconf_device = None
    interfaces_adj_up_count: int = 0

    def parse(self, data: dict, device: netconf_device) -> list[dict]:
        self.device = device
        return self.neighbor_stats(data)

    def neighbor_stats(self, data: dict) -> list[dict]:
        stats: list = []
        neighbors: dict = data["rpc-reply"]["data"]["isis-oper-data"]["isis-instance"]

        for neighbor in neighbors:
            if "isis-neighbor" in neighbor and "isis-adj-up" in neighbor["state"]:
                self.interfaces_adj_up_count += 1 
    
        for neighbor in neighbors:
            if "isis-neighbor" in neighbor:
                metadata = self.metadata(neighbor)
                stats.append(metadata)
        return stats

    def metadata(self, neighbor: dict) -> dict:
        return {
            "operational_status": 1
            if "isis-adj-up" in neighbor["state"]
            else 0,
            "name": neighbor["system-id"].replace(" ", "_"),
            "field": "neighbor_statistics",
            "device": self.device.hostname,
            "ip": self.device.host,
            "if-name":neighbor["if-name"],
            "ipv4-address":neighbor["ipv4-address"],
            "interfaces_adj_up_count": self.interfaces_adj_up_count,
        }

# python3 main.py --device_settings cat8000v-0_settings.json --xml_filter Cisco-IOS-XE-isis-oper.xml