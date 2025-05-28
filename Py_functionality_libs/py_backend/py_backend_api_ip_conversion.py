#!/usr/bin/env python3


import ipaddress
from ipaddress import IPv4Network
from ipaddress import ip_network
from ipaddress import ip_interface

# https://docs.python.org/3/library/ipaddress.html#module-ipaddress


def get_first_ip(ip):
    list_of_hosts = ipaddress.IPv4Network(ip)
    print(list_of_hosts)

    return list_of_hosts


def main():
    # get_first_ip('17.11.127.67/27')
    # print('expected_ip')
    print(IPv4Network("17.11.127.67"))
    # print(ip_network('17.11.127.67/27'))
    print(list(ip_network("19.11.127.0/28").hosts()))
    print(list(ip_network("17.11.127.8/30").hosts()))
    print(list(ip_network("19.11.20.67/32").hosts()))
    print(list(ip_network("19.11.20.67/32")))
    print(list(ip_network("19.11.20.64/27")))
    print(ip_interface("19.11.20.67/27"))  # 19.11.20.67/27
    print(ip_interface("19.11.20.67/27").network)  # 19.11.20.64/27


if __name__ == "__main__":
    main()
