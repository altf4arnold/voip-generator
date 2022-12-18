"""
This module creates config files for the Cisco 7940 and Cisco 7960
"""

def mac():
    """
    This takes the mac address and puts it into correct format for use
    :return: raw mac
    """
    mac = input("Phone mac address : ")
    raw_mac = "none"
    if len(mac) == 12:
        raw_mac = mac.upper()
    elif len(mac) == 17:
        raw_mac = ""
        for i in mac:
            if i != ":":
                raw_mac = raw_mac + i.upper()

    return raw_mac

def main():
    mac_address = mac()
    print(mac_address)