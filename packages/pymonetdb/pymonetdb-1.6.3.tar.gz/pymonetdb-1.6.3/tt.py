#!/usr/bin/env python3

# import sys

# print(sys.version_info)
# print(pymonetdb.__path__)
# assert 'src/pymonetdb' in pymonetdb.__path__[0]

# from pymonetdb import control

import time
import pymonetdb.control

start_time = time.time()

def get_now():
	global start_time
	return time.time() - start_time

# reproduce the behaviour of test_create

def may_fail(desc, function):
	print(f"RUN {desc}", end="", flush=True)
	t0 = time.time()
	try:
		function()
		print("  OK", end="", flush=True)
		return True
	except pymonetdb.OperationalError as e:
		print(f"  ERR {str(e)!r}", end="", flush=True)
		return False
	finally:
		t1 = time.time()
		d = t1 - t0
		print(f"   [{d:.2f}s]")

def must_not_fail(desc, function):
	print(f"RUN {desc}", end="", flush=True)
	t0 = time.time()
	ret = function()
	print("  OK", end="", flush=True)
	t1 = time.time()
	d = t1 - t0
	print(f"   [{d:.2f}s]")
	return ret

DBNAME = 'demo'

#control = must_not_fail("create control", lambda: pymonetdb.control.Control(hostname='localhost', passphrase='testdb'))
control = must_not_fail("create control", lambda: pymonetdb.control.Control())

# # in setup:
may_fail("stop demo", lambda: control.stop(DBNAME))
may_fail("destroy demo", lambda: control.destroy(DBNAME))
may_fail("destroy demo", lambda: control.destroy(DBNAME))
may_fail("destroy demo", lambda: control.destroy(DBNAME))
may_fail("destroy demo", lambda: control.destroy(DBNAME))
must_not_fail("create demo", lambda: control.create(DBNAME))

# # in test_create
# DBNAME2 = 'banana'
# may_fail("destroy banana", lambda: control.destroy(DBNAME2))
# must_not_fail("create banana", lambda: control.create(DBNAME2))
# ok = may_fail("create banana again", lambda: control.create(DBNAME2))
# assert not ok
# may_fail("destroy banana", lambda: control.destroy(DBNAME2))

# # in tear down
# may_fail("stop demo", lambda: control.stop(DBNAME))
# may_fail("destroy demo", lambda: control.destroy(DBNAME))
