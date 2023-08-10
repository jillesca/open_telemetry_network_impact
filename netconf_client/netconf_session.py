from ncclient import manager
from file_utils import read_file


def connect(device: dict, netconf_payload: str) -> str:
    with manager.connect(
        host=device.host,
        port=device.port,
        username=device.username,
        password=device.password,
        hostkey_verify=device.hostkey_verify,
        device_params=device.device_params,
    ) as session:
        return rpc_get(
            session,
            read_file(netconf_payload),
        )


def rpc_get(session: manager, netconf_payload: str) -> str:
    return session.get(netconf_payload)
