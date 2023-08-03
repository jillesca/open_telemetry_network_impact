from typing import Dict, List
from ncclient import manager
from intf_stats_xe_to_json import intf_stats_xe_to_json
from netconf_client_utils import read_file, parse_xml_to_dict

NETCONF_INTERFACE_STATS = "/opt/netconf_client/netconf_interface_stats.xml"

def connect_netconf_to(device: Dict) -> str:
    with manager.connect(
            host = device.host,
            port = device.port,
            username = device.username,
            password = device.password,
            hostkey_verify= device.hostkey_verify,
            device_params = device.device_params
        ) as session:
            netconf_reply = parse_xml_to_dict(rpc_get(session, read_file(NETCONF_INTERFACE_STATS)))
            return intf_stats_xe_to_json(netconf_reply)

def rpc_get(session: manager, call: str) -> str:
    return session.get(call)
