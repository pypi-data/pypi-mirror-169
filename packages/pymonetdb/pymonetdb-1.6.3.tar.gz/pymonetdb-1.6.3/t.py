#!/usr/bin/env python3

# import sys

# print(sys.version_info)
# print(pymonetdb.__path__)
# assert 'src/pymonetdb' in pymonetdb.__path__[0]

# from pymonetdb import control

import pymonetdb.control

# This works
# ctrl = pymonetdb.control.Control(hostname='localhost', passphrase='testdb')
# print(ctrl.status('demo'))

# This doesn't
ctrl = pymonetdb.control.Control(passphrase='testdb')
print(ctrl.status('demo'))

