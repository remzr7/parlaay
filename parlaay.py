#!/usr/bin/env python
import sys

from docker import Client
cli = Client(base_url='tcp://45.79.170.248:2375')

def build():
    print("building...")

def main():
    for arg in sys.argv[0]:
        if arg is "info":
            ##
            continue
        elif arg is "build":
            build()

    print('execed')
    return 0

main()
