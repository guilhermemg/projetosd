#!/usr/bin/env python

import sys

for line in sys.stdin:

    line = line.strip()

    movie = line.split('\t')[1]
    rating = line.split('\t')[2]

    print '%s\t%s' % (movie, rating)
    
