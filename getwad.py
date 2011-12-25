#!/usr/bin/env python3

import io, os, sys, zipfile
from urllib.request import urlopen
from urllib.error   import HTTPError

BASENAME = os.path.basename(sys.argv[0])
USAGE = "{} <pk3> [dest]".format(BASENAME)

def errorExit(reason):
    print("{}: error: {}".format(BASENAME, reason))
    sys.exit(1)

def usageExit(reason):
    print("{}: error: {}".format(BASENAME, reason))
    print(USAGE)
    sys.exit(128)


def main(file, dest):
    try:
        url = urlopen("http://wadhost.fathax.com/files/{}".format(file))
    except HTTPError:
        print("\"{}\" could not be retrieved".format(file), file=sys.stderr)
        return
    
    if file.lower().endswith(".zip"):
        urlB = io.BytesIO(url.read())
        z    = zipfile.ZipFile(urlB)
        
        print("files in \"{}\": {}".format(file, " ".join(z.namelist())))

        z.extractall(dest)
    else:
       print("hi")
       end = open(file, "wb").write(url.read())

if __name__ == "__main__":
    if len(sys.argv) < 2:
        
        while True:
            try:
                file = input()
            except EOFError:
                break

            if file: main(file, ".")
    else:
        file = sys.argv[1]
        dest = sys.argv[2:3] or "."

        main(file, dest)
