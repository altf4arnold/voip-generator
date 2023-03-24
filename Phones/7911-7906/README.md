# 7911 - 7906 Series :

## Intro :

You will need an IPv4 Network with :

* DHCP server (tested on tagged Voice-Vlan)
* TFTP server (option 66 configured in DHCP server)
* physical access to the phone

## Factory reset sequence :

When the phone start's up, (either POE or local adapter), dial the `#` until the red headset light starts blinking.
Dial `1 2 3 4 5 6 7 8 9 * 0 #` in that order. The phone will factory reset

## Flashing process :

```<loadInformation>``` is what needs to contain the firmware number.

After factory reset, the phone will look up in the TFTP server for his own config file (`SEP<mac-address>.cnf.xml`)
In the case of flashing to SIP firmware, that file has to contain the fact that it goes to SIP and a firmware version.
All system files must be stored at the root of the TFTP server.

## Startup Sequence :

At every reboot, the phone will look up for the ``SEP<mac-address>.cnf.xml``.

## Common problems:

Phone can start to boot-loop after flashing. Apparently, if it can't connect to the IPPBX, it will reboot.