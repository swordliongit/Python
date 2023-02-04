"""
import socket

print ([ip for ip in socket.gethostbyname_ex(socket.gethostname())[2] if not ip.startswith("127.")][:1])
"""

import netifaces as nif
from getmac import get_mac_address
import netifaces

"""def getmac(interface):
    try:
        mac = open('/sys/class/net/'+interface+'/address').readline()
    except:
        mac = "00:00:00:00:00:00"
    return mac[0:17]

"""


def ip4_addresses():
    ip_list = []
    mac_list = []
    for interface in netifaces.interfaces():
        for link in netifaces.ifaddresses(interface)[netifaces.AF_INET]:
            ip_list.append(link['addr'])
            mac_list.append(netifaces.ifaddresses(interface))
            print("\n")

    return ip_list


def mac_for_ip(ip):
    'Returns a list of MACs for interfaces that have given IP, returns None if not found'
    for i in nif.interfaces():
        addrs = nif.ifaddresses(i)
        try:
            if_mac = addrs[nif.AF_LINK][0]['addr']
            if_ip = addrs[nif.AF_INET][0]['addr']
        except IndexError or KeyError:  # ignore ifaces that dont have MAC or IP
            if_mac = if_ip = None
        if if_ip == ip:
            return if_mac
    return None


print(ip4_addresses())
# print(mac_for_ip('192.168.5.1'))
"""for i in ip4_addresses():
    print(mac_for_ip(i))"""
# print(get_mac_address())
# print(netifaces.gateways()['default'][netifaces.AF_INET])


# 1c184a
