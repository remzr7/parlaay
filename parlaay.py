#!/usr/bin/env python
import sys

from docker import Client
cli = Client(base_url='tcp://45.79.170.248:2375')

def build():
    print("building...")


def info():
    print(cli.info())


def main():
    arg = sys.argv[1]
    print(arg)
    if arg == "info":
        info()
    elif arg == "build":
        build()
    else:
        print("Command not found")
    print('execed')
    return 0

main()
