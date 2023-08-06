from ncclient import manager
from netconf_client_utils import read_file


def connect(device: dict, netconf_payload: str) -> str:
    with manager.connect(
        host=device.host,
        port=device.port,
        username=device.username,
        password=device.password,
        hostkey_verify=device.hostkey_verify,
        device_params=device.device_params,
    ) as session:
        # TODO fix filter dir
        return rpc_get(session, read_file("filters/" + netconf_payload))


def rpc_get(session: manager, call: str) -> str:
    return session.get(call)
