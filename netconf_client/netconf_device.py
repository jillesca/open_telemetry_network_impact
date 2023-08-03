from typing import Dict
from dataclasses import dataclass

@dataclass
class netconf_device:
    host: str
    port: str
    username: str
    password: str
    hostkey_verify: str
    device_params: Dict
    hostname: str
