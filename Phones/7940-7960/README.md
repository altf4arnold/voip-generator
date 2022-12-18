# 7940 - 7960 Series :
## Intro : 

You will need an IPv4 Network with :
* DHCP server
* TFTP server
* physical access to the phone

## Factory reset sequence :
When the phone start's up, (either POE or local adapter), dial the `#` until the screen starts up.
When the screen tell's factory reset sequence, Dial `1 2 3 4 5 6 7 8 9 * 0 #` in that order. Phone will ask you if you want to save his network config.
Dial 2 (network config erase).

## Flashing process :
After factory reset, the phone will look up in the TFTP server for his own config file (`SEP<mac-address>.cnf.xml`)
In the case of flashing to SIP firmware, that file has to contain the fact that it goes to SIP and a firmware version.
All system files must be stored at the root of the TFTP server.