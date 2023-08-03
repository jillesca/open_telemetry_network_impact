from typing import Dict
from dataclasses import dataclass
from netconf_client_utils import parse_from_json

@dataclass
class netconf_device:
    host: str
    port: str
    username: str
    password: str
    hostkey_verify: str
    device_params: Dict
    hostname: str
