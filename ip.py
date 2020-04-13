#!/usr/bin/env python

import sys
import os
import socket

def strip_https(domain):
    http = domain.find('http://')
    https = domain.find('https://')
    if http != -1:
        domain = domain[http + len('http://'):]
    elif  https != -1:
        domain = domain[https + len('https://'):]
    return domain

def get_ip(str):
    if len(str) < 2:
        print('Usage: python net.py ipaddr')
        sys.exit(1)
    else:
        ipstrip = str[1].strip()
        split = ipstrip.split('.')
        if len(split) == 4:
            splat = strip_https(ipstrip)
            for khra in splat.split('.'):
                if not khra.isdigit():
                    print('Invalid IP')
                    exit(3)
            return splat
        elif len(split) == 2 and not split[1].isdigit():
            splat = strip_https(ipstrip)
            return socket.gethostbyname(splat)
        elif len(split) == 3 and not split[2].isdigit():
            return socket.gethostbyname(split[1] + '.' +  split[2])
        else:
            print('Invalid argument')
            exit(4)

def ping_ip(ipaddr, output):
    output_file = output + ipaddr + '.txt'
    ret = os.system("ping -c 2 " + ipaddr + " > " + output_file)
    if ret == 0:
        print('Host up')
        return True
    else:
        print('Host down or does not exist')
        return False
