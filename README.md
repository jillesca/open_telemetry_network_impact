# Open Telemetry Network

Go to [NSO 6 Reservable Sandbox](https://developer.cisco.com/site/sandbox/) and reserve a lab. **Clone this repo to the devbox VM - 10.10.20.50 developer/C1sco12345**

This lab doesn't use the default topology from the NSO sandbox.

Go to CML <https://10.10.20.161> (developer/C1sco12345) **stop** and **wipe** the default topology to avoid IP conflicts.

Then load the [cml topology](ansible/cml_lab/topology.yaml) prepared for this lab.

**hint** you can load the topology using ansible, see the bonus part at the end of the readme.

# Setup NSO

[See NSO Setup](nso/README.md)

# Start containers on Devbox VM

```bash
chmod +x build_run_grafana.sh
chmod +x build_run_influxdb.sh
chmod +x build_run_telegraf.sh

./build_run_grafana.sh
./build_run_influxdb.sh
./build_run_telegraf.sh
```

# Verify telemetry on IOS-XE

```
show telemetry ietf subscription 1010 receiver
show telemetry ietf subscription 1010 detail
```

# Verify telemetry on Telegraf, Influxdb, Grafana

- telegraf - [tail -F /tmp/telegraf-grpc.log](telegraf/dockerfile#30)
- Grafana - <http://10.10.20.50:3000>
- Influxdb - <http://10.10.20.50:8086>

# Network Telemetry captured

<!-- interface state -> dial out
interface counters, specially traffic pps -> dial in -->

<!-- memory and cpu are fine -> dial in -->

isis state -> dial out
cdp neighboar might be?? -> dial in

<https://github.com/jeremycohoe/cisco-ios-xe-mdt/blob/master/cat9k-174-device-health-dashboa#L132>
<https://github.com/jeremycohoe/cisco-ios-xe-mdt/blob/master/cat9k-174-device-health-dashboa#L150C6-L150C35>

<!-- xpath_filter = "/process-cpu-ios-xe-oper:cpu-usage/cpu-utilization"
update_trigger = "periodic" -->

<!-- xpath_filter = "/memory-ios-xe-oper:memory-statistics/memory-statistic"
update_trigger = "periodic" -->

<!-- xpath_filter = "/oc-if:interfaces/interface/state/counters"
update_trigger = "periodic" -->

<!-- xpath_filter = "/interfaces-ios-xe-oper:interfaces/interface"
update_trigger = "periodic" -->

<!-- xpath_filter = "/if:interfaces-state"
update_trigger = "periodic" -->

# Bonus: Create the lab using Ansible

Start ansible container

```bash
chmod +x build_run_cml.sh
./build_run_cml.sh
```

Enter the container first

```bash
docker exec -it cml /bin/sh
```

## Delete default lab

```bash
cd ansible
ansible-playbook cisco.cml.clean -e cml_lab="'Small NXOS/IOSXE Network'"

```

## Create a lab

```bash
ansible-playbook cisco.cml.build -e startup='host' -e wait='yes'
```

# Links that helped to build the lab

- <https://github.com/jeremycohoe/cisco-ios-xe-mdt/tree/master>
- <https://anirudhkamath.github.io/network-automation-blog/notes/network-telemetry-using-netconf-telegraf-prometheus.html>

# Find which subscriptions could be on-change

Use `show platform software ndbman ...` and autocomplete for your device.

On the lab you can use

```bash
show platform software ndbman R0 models | inc Emul|no
```
