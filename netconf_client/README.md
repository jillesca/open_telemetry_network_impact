# netconf_client

The `netconf_client` is a script written to grab telemetry data using netconf, it uses the `ncclient` library.

To use it, install the dependencies needed

```bash
pip install -r requirements.txt
```

## Usage

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

## Operations

Currently only uses the [GET operation](netconf_session.py#L13) to retrieve data.

## Ways to retrieve data

Relative and absolute paths are supported to define device or filters files.

### Define your devices

Under the [devices directory](devices) create a json file. Follow the structure defined of the existing files. **Don't add or remove fields,** these are used to [build a netconf_device object](netconf_devices.py)

### xml filter

You need to specify an `xml` file with the filter you want to use and the `--xml_filter` option when calling the script.

For example:

- `--xml_filter=cisco_xe_ietf-interfaces.xml`

The script supports relative and absolute paths. Default directory is [the filter directory](filters), place your `xml` files there if you don't want to deal with absolute or relative paths.

### xpath

`xpath` can be use with the following formats:

- `--xpath_filter=<xpath>`
- `--xpath_filter=<namespace>:<xpath>`

For example:

```bash
--xpath_filter=interfaces/interface
--xpath_filter=http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper:interfaces/interface
```

The `xpath` filter is used as [ID internally](factory.py#L21).

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

- Create a parser under [the parsers directory](parsers)
  - You parser must implement the `Parser` class. See an [existing parser for an example](parsers/cisco_ios_xe_memory_oper.py#L8)
- Add your new parser to [the factory file](factory.py#L5) under the match statement.
  - If using a `xml` file, use the file name as ID, including the `.xml` extension.
  - If using `xpath`, use the whole xpath expression.
