import logging
from file_utils import read_file
from ncclient import manager
from ncclient.operations.errors import TimeoutExpiredError
from ncclient.transport.errors import SSHError, AuthenticationError

logging.basicConfig(
    level=logging.CRITICAL,
)


def connect_to(device: dict, netconf_payload: str) -> str:
    try:
        return connect(device, netconf_payload)
    except AuthenticationError as error:
        raise ValueError(f"{error=}") from error

    except SSHError as error:
        raise ValueError(f"{error=}") from error

    except TimeoutExpiredError as error:
        raise ValueError(f"{error=}") from error

    except Exception as error:
        raise ValueError(f"{error=}") from error


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
