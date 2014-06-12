# -*- coding: utf-8 -*-
# Get HTTP header.
# Add PY to PATHEXT to run as executable
# Python 2.7
__author__ = 'Ruslanas Balčiūnas'

import urllib2
import sys, getopt

def main(argv):

    try:
        opts, args = getopt.getopt(argv, 'hf:', ['help', 'field='])
    except getopt.GetoptError as e:
        print e.msg
        sys.exit(1)
    
    fname = ''
    for opt, arg in opts:
        if opt in ('-h', '--help'):
            print 'Usage: hdr [--help] [--field name] <url>'
            sys.exit(1)
        if opt in ('-f', '--field'):
            fname = arg
    
    if len(args) < 1:
        print 'Try: python hdr.py --help'
        sys.exit(0)
    
    try:
        resp = urllib2.urlopen(args[0])
    except ValueError as e:
        print e.message
        sys.exit(1)
    except urllib2.HTTPError as e:
        print 'HTTP error: %d' % e.code
        sys.exit(1)
    except urllib2.URLError as e:
        print str(e)
        sys.exit(1)
    
    meta = resp.info()
    
    if not fname:
        print str(meta)
    else:
        field = meta.getheaders(fname)
        if len(field):
            print field[0]

if __name__ == '__main__':
    main(sys.argv[1:])
