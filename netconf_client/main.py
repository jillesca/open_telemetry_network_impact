from netconf_client_utils import read_file, parse_from_json
from netconf_device import netconf_device
from netconf_session import connect_netconf_to

DEVICES_SETTINGS = "/opt/netconf_client/netconf_devices_settings.json"

def main():
    devices_settings = parse_from_json(read_file(DEVICES_SETTINGS)) 
    for device_setting in devices_settings:
        print(connect_netconf_to(netconf_device(**device_setting)))


if __name__ == "__main__":
    main()
