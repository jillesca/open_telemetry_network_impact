# Open Telemetry Network

This demo uses the CML sandbox, but technically any IOS-XE device with two ISIS interfaces will work.

Go to [Cisco Modeling Labs](https://developer.cisco.com/site/sandbox/) and reserve a lab. **Clone this repo to the devbox VM - 10.10.20.50 developer/C1sco12345**

This lab doesn't use the default topology from the sandbox. Go to CML <https://10.10.20.161> (developer/C1sco12345) **stop** and **wipe** the default topology to avoid IP conflicts. Then load the [cml topology](cml/ansible/cml_lab/topology.yaml) prepared for this lab.

**hint** you can load the topology using ansible, see the bonus part at the end of the readme.

## Goal

This an exercise to play with AI, specifically OpenAI. The end goal is to get help from AI understanding alarms and giving steps we could do to fix the issue.

These alarms are triggered by Grafana using webhooks. The network data is collected using telemetry data via netconf.

Two alarms were created for this demo

- If less than two `ISIS` interfaces are `UP` per device.
- If one interface goes down on any device.

## Prepare Demo

### Start containers on your laptop

```bash
chmod +x build_run_grafana.sh
chmod +x build_run_influxdb.sh
chmod +x build_run_telegraf.sh

bash build_run_grafana.sh
bash build_run_influxdb.sh
bash build_run_telegraf.sh
```

### Start the chatbot

Install the dependencies needed.

```bash
pip install -r llm/requirements.txt
```

Add your OpenAI key as environment variable.

```bash
export LLM_API_KEY=your_open_ai_key
```

```bash
cd llm/chatbot
python app.py
```

### Verify telemetry on IOS-XE

Devices used (cisco/cisco):

- 10.10.20.175
- 10.10.20.176

### Verify telemetry on Telegraf, Influxdb, Grafana

- telegraf - [tail -F /tmp/telegraf-grpc.log](telegraf/dockerfile#30)
- Grafana - <http://localhost:3000>
- Influxdb - <http://localhost:8086>

## User your own devices

If you want to use your own devices, you only need to tell the [netconf client](netconf_client) which devices it has to query and their credentials.

To add your devices [create a configuration file under the devices directory.](netconf_client/devices/) Follow the structure of the existing files.

Then you need to tell telegraf, which configuration file it should use under [netconf.conf file](telegraf/netconf.conf#2)

Rebuild the container using `bash build_run_telegraf.sh`

## Bonus: Create the lab using Ansible from your laptop

```bash
chmod +x build_run_cml.sh
bash build_run_cml.sh
```

## Links that helped to build the lab

- <https://github.com/jeremycohoe/cisco-ios-xe-mdt/tree/master>
- <https://anirudhkamath.github.io/network-automation-blog/notes/network-telemetry-using-netconf-telegraf-prometheus.html>

## Find which subscriptions could be on-change

Use `show platform software ndbman ...` and autocomplete for your device.

On the lab you can use

```bash
show platform software ndbman R0 models | inc Emul|no
```
