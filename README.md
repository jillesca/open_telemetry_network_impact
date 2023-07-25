# Lab used

CML or [Cisco Modelling Labs.](https://developer.cisco.com/docs/sandbox/#!networking/networking-overview) Reserve a lab to get started.

# Delete default lab

```bash
cd ansible
ansible-playbook cisco.cml.clean -e cml_lab="'Small NXOS/IOSXE Network'"

```

# Create a lab

```build & start the container
chmod a+x build_and_run.sh
./build_and_run.sh
```

```bash
ansible-playbook cisco.cml.build -e startup='host' -e wait='yes'
```
