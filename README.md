# Lab used

[NSO 6 Reservable Sandbox](https://developer.cisco.com/site/sandbox/) Reserve a lab to get started.

This lab doesn't use the default topology from the NSO sandbox.

Go to CML `10.10.20.161` (developer/C1sco12345) **stop** and **wipe** the default topology to avoid IP conflicts.

Then load the [cml topology](https://github.com/jillesca/open_telemetry_network/blob/main/ansible/cml_lab/topology.yaml) prepared for this lab.

# Start containers on Devbox VM

```bash
chmod +x build_run_grafana.sh
chmod +x build_run_influxdb.sh
chmod +x build_run_telegraf.sh

./build_run_grafana.sh
./build_run_influxdb.sh
./build_run_telegraf.sh
```

# verify telemetry on IOS-XE

```
show telemetry ietf subscription 1010 receiver
show telemetry ietf subscription 1010 detail
```

# Bonus: Create a lab using ansible

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
