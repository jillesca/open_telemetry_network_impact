# netconf_client

The `netconf_client` is a script written to grab telemetry data using netconf, it uses the `ncclient` library.

To use it, install the dependencies needed

```bash
pip install -r requirements.txt
```

## Usage

Currently only uses the [GET operation](netconf_session.py#13) to retrieve data.

It support two methods to retrieve data, using an `xml` file filter or using an `xpath` expression. Only one can be used when performing an action. If you want to use both filters, simply call the device twice using different filter.

```bash
╰─ python main.py -h
usage: main.py [-h] [--device_settings DEVICE_SETTINGS] (--xml_filter XML_FILTER | --xpath_filter XPATH_FILTER)

options:
  -h, --help            show this help message and exit
  --device_settings DEVICE_SETTINGS
                        Device Settings in json fomat. Eg. 'netconf_devices_settings.json'
  --xml_filter XML_FILTER
                        Netconf Filter to apply in xml format. Eg. 'cisco_xe_ietf-interfaces.xml'
  --xpath_filter XPATH_FILTER
                        Netconf Filter to apply in xpath. Formats: <xpath> OR <namespace>:<xpath> Eg. 'interfaces/interface' OR 'http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper:interfaces/interface' xpath is used as
                        ID internally.
```

For example

```bash
python main.py --device_settings=cat8000v-1_settings.json --xml_filter=Cisco-IOS-XE-memory-oper.xml

python3 main.py --device_settings=cat8000v-0_settings.json --xpath_filter=http://cisco.com/ns/yang/Cisco-IOS-XE-isis-oper:/isis-oper-data/isis-instance
```

Once the script finishes, it will print the result. This is enough for working with telegraf as an exec plugin, but might not be for your use case.

## Netconf Filters

At the time of writting it parses the output of the following netconf filters:

- `ietf-interfaces`
- `Cisco-IOS-XE-interfaces-oper`
- `Cisco-IOS-XE-memory-oper`
- `Cisco-IOS-XE-isis-oper`

If using the `--xml_filter` option, you can find the xml used under [the filter directory.](filters)

The python code that parses the RPC reply is found under [the parsers directory](parsers)

## Adding a Parser

If you want to add your own parser. You need to:

- If using an `xml filter` add your `xml` file under [the filter directory](filters)
- Create a parser under [the parsers directory](parsers)
  - You parser must implement the `Parser` class. See an [existing parser for an example](parsers/cisco_ios_xe_memory_oper.py#8)
- Add your new parser to [the factory file](factory.py#5) under the match statement.
