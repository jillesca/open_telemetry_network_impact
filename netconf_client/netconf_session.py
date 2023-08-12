from dataclasses import dataclass
from netconf_devices import netconf_device
from ncclient import manager


@dataclass
class netconf_handler:
    device: netconf_device
    netconf_filter: str = None

    def rpc_get(self, netconf_filter: str) -> str:
        self.netconf_filter = netconf_filter
        return self._connect(operation="GET")

    def _connect(self, operation: str) -> str:
        with manager.connect(
            host=self.device.host,
            port=self.device.port,
            username=self.device.username,
            password=self.device.password,
            hostkey_verify=self.device.hostkey_verify,
            device_params=self.device.device_params,
        ) as m:
            match operation:
                case "GET":
                    return m.get(self.netconf_filter)
