#!/usr/bin/env python

import sys

for line in sys.stdin:

    line = line.strip()

    user = line.split('\t')[0]

    print '%s\t%s' % (user, 1)
    
