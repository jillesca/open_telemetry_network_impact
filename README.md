# Lab used

CML or [Cisco Modelling Labs.](https://developer.cisco.com/docs/sandbox/#!networking/networking-overview) Reserve a lab to get started.

# Delete default lab

```bash
cd ansible
ansible-playbook cisco.cml.clean -e cml_lab="'Small NXOS/IOSXE Network'"

```

# Create a lab

```build & start the container
chmod a+x build_and_run_cml.sh
./build_and_run_cml.sh
```

```bash
ansible-playbook cisco.cml.build -e startup='host' -e wait='yes'
```

# Build NSO container

```build & start the container
chmod a+x build_nso.sh
./build_nso.sh
```
