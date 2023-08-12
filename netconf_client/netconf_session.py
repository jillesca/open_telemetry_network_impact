from ncclient import manager
from ncclient.operations.errors import TimeoutExpiredError
from ncclient.transport.errors import SSHError, AuthenticationError


def connect_to(device: dict, netconf_filter: str) -> str:
    try:
        return connect(device, netconf_filter)
    except AuthenticationError as error:
        raise ValueError(f"{error=}") from error

    except SSHError as error:
        raise ValueError(f"{error=}") from error

    except TimeoutExpiredError as error:
        raise ValueError(f"{error=}") from error

    except Exception as error:
        raise ValueError(f"{error=}") from error


def connect(device: dict, netconf_filter: str) -> str:
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
            netconf_filter,
        )


def rpc_get(session: manager, netconf_filter: str) -> str:
    return session.get(netconf_filter)
