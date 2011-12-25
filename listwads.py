#!/usr/bin/env python3

import re, os, sys
import sre_constants

from urllib import request


BASENAME = os.path.basename(sys.argv[0])
USAGE = "{} <re>".format(BASENAME)

PARSERE = r''' +<a href=".+?">(.+?)</a> +? (\d{2}-[A-Za-z]{3}-\d{4}) (\d{2}:\d{2}) +([\d\.]+[GKM]?) +'''
PARSERE = re.compile(PARSERE)

def errorExit(reason):
    print("{}: error: {}".format(BASENAME, reason))
    sys.exit(1)

def usage():
    print("usage:", USAGE)

def usageExit(reason):
    print("{}: error: {}".format(BASENAME, reason))
    usage()
    sys.exit(128)

if len(sys.argv) < 2:
    usageExit("needs an RE")

try:
    matchRE = re.compile(sys.argv[1])
except sre_constants.error:
    errorExit("invalid RE")

url   = request.urlopen("http://wadhost.fathax.com/files")
derp  = url.read().decode()

for line in derp.split("\n"):
    match = PARSERE.match(line)
    
    if match:
        name, date, time, size = match.groups()

        if matchRE.match(name):
            print(name)
