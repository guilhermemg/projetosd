#!/usr/bin/env python

import sys

for line in sys.stdin:

    line = line.strip()

    rating = line.split('\t')[2]

    print '%s\t%s' % (rating, 1)
    
