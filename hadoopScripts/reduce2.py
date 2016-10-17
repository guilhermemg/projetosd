#!/usr/bin/env python

from operator import itemgetter
import sys

current_rating = None
current_count = 0
rating = None

for line in sys.stdin:
    line = line.strip()

    rating, count = line.split('\t', 1)

    if current_rating == rating:
        current_count += int(count)
    else:
        if current_rating:
            print '%s\t%s' % (current_rating, current_count)
        current_count = int(count)
        current_rating = rating

if current_rating == rating:
    print '%s\t%s' % (current_rating, current_count)
