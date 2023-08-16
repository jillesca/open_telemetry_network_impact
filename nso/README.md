# NSO Setup

#### Connect to devbox VM on the sandbox

```bash
 ssh developer@10.10.20.50

 Pass: C1sco12345
```

#### Bash process

```bash
bash start_run_nso.sh
```

#### Manual Process

```bash
source ~/nso/ncsrc

ncs-setup --package ~/nso/packages/neds/cisco-ios-cli-6.91/ --dest nso-instance

cd nso-instance

ncs
```

##### Connect to NSO

```bash
ncs_cli -C -u admin
config
```

For a quick copy paste use `load merge terminal`

Once the config is added use Ctrl+d to return to the NSO prompt

##### Add IOS-XE devices

```bash
devices authgroups group labadmin
default-map remote-name cisco
default-map remote-password cisco
default-map remote-secondary-password cisco
!
devices device cat8000v-0
 address   10.10.20.175
 ssh host-key-verification none
 authgroup labadmin
 device-type cli ned-id cisco-ios-cli-6.91
 device-type cli protocol ssh
 state admin-state unlocked
!
devices device cat8000v-1
 address   10.10.20.176
 ssh host-key-verification none
 authgroup labadmin
 device-type cli ned-id cisco-ios-cli-6.91
 device-type cli protocol ssh
 state admin-state unlocked

```

Sync to devices

```
do devices sync-from
```

###### Add config for Cat8000v-0

```bash
devices device cat8000v-0
 config
  aaa new-model
  aaa authentication login default local
  aaa authorization exec default local
  aaa session-id common
  username admin privilege 15 password 0 Cisco123
  interface GigabitEthernet2
   ip address 10.1.1.1 255.255.255.0
   ip router isis
   no shutdown
  exit
  interface GigabitEthernet3
   ip address 172.16.101.1 255.255.255.0
   no shutdown
  exit
  interface GigabitEthernet4
   ip address 10.2.2.1 255.255.255.0
   ip router isis
   no shutdown
  exit
  telemetry ietf subscription 1010
   encoding       encode-kvgpb
   filter xpath /process-cpu-ios-xe-oper:cpu-usage/cpu-utilization/five-seconds
   source-address 10.10.20.175
   stream         yang-push
   update-policy periodic 2000
   receiver ip address 10.10.20.50 57500 protocol grpc-tcp
  !
  netconf-yang
  router isis
   net 49.0001.0000.0000.000a.00
   is-type level-1
  !
 !
!

```

###### Add config for Cat8000v-1

```bash
devices device cat8000v-1
 config
  aaa new-model
  aaa authentication login default local
  aaa authorization exec default local
  aaa session-id common
  username admin privilege 15 password 0 Cisco123
  interface GigabitEthernet2
   ip address 10.1.1.2 255.255.255.0
   ip router isis
   no shutdown
  exit
  interface GigabitEthernet3
   ip address 172.16.102.1 255.255.255.0
   no shutdown
  exit
  interface GigabitEthernet4
   ip address 10.2.2.2 255.255.255.0
   ip router isis
   no shutdown
  exit
  telemetry ietf subscription 1010
   encoding       encode-kvgpb
   filter xpath /process-cpu-ios-xe-oper:cpu-usage/cpu-utilization/five-seconds
   source-address 10.10.20.176
   stream         yang-push
   update-policy periodic 2000
   receiver ip address 10.10.20.50 57500 protocol grpc-tcp
  !
  netconf-yang
  router isis
   net 49.0001.0000.0000.000b.00
   is-type level-1
  !
 !
!

```
