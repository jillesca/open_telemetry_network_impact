from ncclient import manager
from netconf_client_utils import read_file, get_absolute_path

FILTER_DIR = "filters"


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
            read_file(get_path(netconf_payload)),
        )


def get_path(payload: str) -> str:
    return f"{get_absolute_path(__file__)}/{FILTER_DIR}/{payload}"


def rpc_get(session: manager, netconf_payload: str) -> str:
    return session.get(netconf_payload)
