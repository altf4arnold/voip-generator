# 7940 - 7960 Series :
## Intro : 

You will need an IPv4 Network with :
* DHCP server (tested on tagged Voice-Vlan)
* TFTP server (option 66 configured in DHCP server)
* physical access to the phone

## Factory reset sequence :
When the phone start's up, (either POE or local adapter), dial the `#` until the screen starts up.
When the screen tell's factory reset sequence, Dial `1 2 3 4 5 6 7 8 9 * 0 #` in that order. Phone will ask you if you want to save his network config.
Dial 2 (network config erase).

## Flashing process :
After factory reset, the phone will look up in the TFTP server for his own config file (`SEP<mac-address>.cnf.xml`)
In the case of flashing to SIP firmware, that file has to contain the fact that it goes to SIP and a firmware version.
All system files must be stored at the root of the TFTP server.

## SIP phone provisioning :
After the SIP firmware has been flashed, the phone will start to TFTP try `SIPDefault.cnf`.
`SIPDefault.cnf` is the file that contain's SIP options that will be used across all phones that can access that file.
(like NTP server's, time format etc.) so that the specific SIP file can be smaller (not that usefull on a modern server with 3 phones in the system. kind of a big deal on a big phone system on a small CME router)

Either `SIPDefault.cnf` gets found and the phone will load the options, either it's not and the phone jumps to the next file. `SIP<mac-address>.cnf`

That file contains the phone specific options. If some options were present in `SIPDefault.cnf`, they will be overwritten on the local phone.

## Startup Sequence :
At every reboot, the phone will look up for the ``SEP<mac-address>.cnf.xml`` to see what firmware is needed. Then `SIPDefault.cnf` and then `SIP<mac-address>.cnf`.