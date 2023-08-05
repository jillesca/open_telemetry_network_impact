from ncclient import manager
from netconf_client_utils import read_file

NETCONF_INTERFACE_STATS = "netconf_interface_stats.xml"
# NETCONF_INTERFACE_STATS = "/opt/netconf_client/netconf_interface_stats.xml"


def connect_netconf_to(device: dict) -> str:
    with manager.connect(
        host=device.host,
        port=device.port,
        username=device.username,
        password=device.password,
        hostkey_verify=device.hostkey_verify,
        device_params=device.device_params,
    ) as session:
        return rpc_get(session, read_file(NETCONF_INTERFACE_STATS))


def rpc_get(session: manager, call: str) -> str:
    return session.get(call)
