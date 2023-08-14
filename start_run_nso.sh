source ~/nso/ncsrc

ncs-setup --package ~/nso/packages/neds/cisco-ios-cli-6.91/ --dest nso-instance

cd nso-instance

ncs

ncs --status | grep -i status

ncs_load -F c -lm nso/base_config.conf

echo "devices connect" | ncs_cli -C -u admin

echo "devices sync-from" | ncs_cli -C -u admin

ncs_load -F c -lm nso/cat8000v-0.conf

ncs_load -F c -lm nso/cat8000v-1.conf