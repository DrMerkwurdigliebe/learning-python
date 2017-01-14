import sys

def check_version_info():
    vi = sys.version_info
    print "You're running %s" % vi
    raise SystemExit('calibre requires python >= 2.7.9 and < 3. Current python version: %s' % vi)

check_version_info()
