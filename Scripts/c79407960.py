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

def getntp():
    """
    geting the NTP server. Getting FQDN or IP address
    :return: the NTP server
    """
    return (input("NTP server : "))

def gettimezone():
    """
    Timezone Selection.
    Default is GMT. (thank you cisco for making that part very long)
    :return: the string of the local timezone
    """
    timezone = "GMT"
    offset = input("What is your GMT offset? (example for Belgium :  +01:00) : ")
    if offset == "-12:00":
        timezone = "IDL"
    elif offset == "-11:00":
        timezone = "NT"
    elif offset == "-10:00":
        timezone = "AHST"
    elif offset == "-09:30":
        timezone = "IMT"
    elif offset == "-09:00":
        timezone = "YST"
    elif offset == "-08:00":
        timezone = "PST"
    elif offset == "-07:00":
        timezone = "MST"
    elif offset == "-06:00":
        timezone = "CST"
    elif offset == "-05:00":
        timezone = "EST"
    elif offset == "-04:00":
        timezone = "AST"
    elif offset == "-03:30":
        timezone = "NST"
    elif offset == "-03:00":
        timezone = "BST"
    elif offset == "-02:00":
        timezone = "AT"
    elif offset == "-01:00":
        timezone = "WAT"
    elif offset == "00:00" or offset == "+00:00" or offset == "-00:00":
        timezone = "GMT"
    elif offset == "+01:00":
        timezone = "CET"
    elif offset == "+02:00":
        timezone = "EET"
    elif offset == "+03:00":
        timezone = "BT"
    elif offset == "+03:30":
        timezone = "IT"
    elif offset == "+04:00":
        timezone = "ZP4"
    elif offset == "+04:30":
        timezone = "AFG"
    elif offset == "+05:00":
        timezone = "ZP5"
    elif offset == "+05:30":
        timezone = "IST"
    elif offset == "+06:00":
        timezone = "ZP6"
    elif offset == "+06:30":
        timezone = "SUM"
    elif offset == "+07:00":
        timezone = "WAST"
    elif offset == "+08:00":
        timezone = "HST"
    elif offset == "+09:00":
        timezone = "JST"
    elif offset == "+09:30":
        timezone = "CAST"
    elif offset == "+10:00":
        timezone = "EAST"
    elif offset == "+11:00":
        timezone = "EADT"
    elif offset == "+12:00":
        timezone = "NZST"
    else:
        print("invalid option")

    return timezone

def main():
    mac_address = mac()
    ntp_server = getntp()
    timezone = gettimezone()