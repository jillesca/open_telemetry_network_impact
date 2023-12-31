from dataclasses import dataclass, field
from netconf_parsers import Parser
from netconf_devices import netconf_device

FIELD_CODE = "isis_interface_state"


@dataclass
class isis_stats_iosxe_oper(Parser):
    device: netconf_device = None
    isis_interfaces_adj_up: int = 0
    stats: list = field(default_factory=list)

    def parse(self, data: dict, device: netconf_device) -> list[dict]:
        self.device = device
        self.neighbor_stats(data)
        return self.stats

    def neighbor_stats(self, data: dict) -> None:
        isis_instances: dict = data["rpc-reply"]["data"]["isis-oper-data"][
            "isis-instance"
        ]

        for key, value in isis_instances.items():
            if "isis-neighbor" in key:
                self.count_adjcencies(value)

        for key, value in isis_instances.items():
            if "isis-neighbor" in key:
                self.gather_metadata(value)

    def count_adjcencies(self, instance: list) -> None:
        # if you have 2 isis interfaces data comes inside a list.
        # if you shutdown one interface and only 1 is up, the data will not come insdie a list.
        if isinstance(instance, list):
            for neighbor in instance:
                if "isis-adj-up" in neighbor["state"]:
                    self.isis_interfaces_adj_up += 1
        else:
            if "isis-adj-up" in instance["state"]:
                self.isis_interfaces_adj_up += 1

    def gather_metadata(self, instance: list) -> None:
        if isinstance(instance, list):
            for neighbor in instance:
                self.stats.append(self.metadata(neighbor))
        else:
            self.stats.append(self.metadata(instance))

    def metadata(self, neighbor: dict) -> dict:
        return {
            "isis_interfaces_adj_up": self.isis_interfaces_adj_up,
            "isis_status": neighbor["state"],
            "neighbor_id": neighbor["system-id"].replace(" ", "_"),
            "field": FIELD_CODE,
            "device": self.device.hostname,
            "ip": self.device.host,
            "interface_name": neighbor["if-name"],
            "ipv4_address": neighbor["ipv4-address"],
        }
