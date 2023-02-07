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
    while True:
        ntpserver = input("NTP server : ")
        if ntpserver != "":
            return ntpserver

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

def getsoftwareversion():
    """
    getting the software version for the phones. Needed for intial flashing (still need to document)
    :return: a string that contains software version.
    """
    while True:
        software = input("What is the software version : ")
        if software != "":
            return software

def getphonename():
    """
    What name would you like your phone to have (name will be shown in the upper right corner
    :return: Phone name
    """
    while True:
        name = input("What is the phone name? (name will be shown in the upper right corner : ")
        if name != "":
            return name

def getproxy():
    """
    This function takes the address of the PBX
    :return: IP address or hostname in a string (MANDATORY)
    """
    while True:
        proxy = input("Enter the Hostname or IP address of the IP-PBX (proxy) : ")
        if proxy != "":
            return proxy

def getlineamount():
    return int(input("How many phone lines do you have : "))

def getusername():
    return input("What is the line username : ")

def getpassword():
    return input("What is the line password : ")

def getlinename():
    return input("line name : ")

def getlogourl():
    return input("Logo URL : ")

def generatefile(ntp_server,timezone,software_version,phonename,proxy,lineamount,logourl):
    return True

def main():
    username=[]
    password=[]
    linename=[]
    mac_address = mac()
    ntp_server = getntp()
    timezone = gettimezone()
    software_version = getsoftwareversion()
    phonename = getphonename()
    proxy = getproxy()
    lineamount = getlineamount()
    for i in lineamount:
        username[i] = getusername()
        password[i] = getpassword()
        linename[i] = getlinename()

    if input("Do you have a custom logo link? (y/n) : ") == "y":
        logourl = getlogourl()

    generatefile(ntp_server,timezone,software_version,phonename,proxy,lineamount,logourl)