# -*- coding: utf-8 -*-
# File download utility
# Python 2.7

__author__ = 'Ruslanas Balčiūnas'

import urllib2
import sys
    
buf_size = 1024
    
def main():
    
    if len(sys.argv) < 2:
        print 'Usage: python pget.py <url>'
        sys.exit(2)
    
    url = sys.argv[1]
    
    try:
        response = urllib2.urlopen(url)
    except ValueError as e:
        print e.message
        sys.exit(1)
    except urllib2.HTTPError as e:
        print 'HTTP error: %d' % e.code
        sys.exit(1)
    except urllib2.URLError:
        print 'URL error'
        sys.exit(1)
            
    meta = response.info()
    
    print str(meta)
    
    fname = meta.getheaders('Content-Disposition')
    
    if len(fname):
        fname = fname[0]
    else:
        fname = url.split('/')[-1]
        fname = fname.split('?')[0]
        
        if not len(fname):
            print 'Not enaugh imagination to create file name'
            sys.exit(1)
    
    f = open(fname, 'wb')
    
    progress = 0
    buffer = response.read(buf_size)
    while buffer:
        progress += len(buffer)
        sys.stdout.write('\r%d bytes loaded. ' % progress)
        sys.stdout.flush()
        f.write(buffer)
        buffer = response.read(buf_size)
    
    f.close()
    print 'Done!'

if __name__ == '__main__':
    main()
