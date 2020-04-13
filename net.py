#!/usr/bin/env python

import os
import sys
from ip import get_ip, ping_ip

if __name__ == "__main__":    
    ipaddr = get_ip(sys.argv)
    if not ping_ip(ipaddr, "out/"):
        exit(5)
    print(ipaddr)
