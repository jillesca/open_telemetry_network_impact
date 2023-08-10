from netconf_parsers import Parser


def calc_percent(entry: dict) -> int:
    return (int(entry["used-memory"]) / int(entry["total-memory"])) * 100


class Cisco_ios_xe_memory_oper(Parser):
    def parse(self, data_to_parse: dict) -> list[dict]:
        return self.memory_oper_to_json(data_to_parse)

    def memory_oper_to_json(self, rpc_reply: dict) -> str:
        stats: list = []
        xpath: dict = rpc_reply["rpc-reply"]["data"]["memory-statistics"][
            "memory-statistic"
        ]

        for entry in xpath:
            stats.append(self.sort_stats(entry))
        return stats

    def sort_stats(self, entry: dict) -> dict:
        return {
            "name": entry["name"],
            "percent_used": calc_percent(entry),
            "field": "memory_pool",
        }
