#!/usr/bin/env python

from operator import itemgetter
import sys

current_user = None
current_count = 0
user = None

for line in sys.stdin:
    line = line.strip()

    user, count = line.split('\t', 1)

    if current_user == user:
        current_count += int(count)
    else:
        if current_user:
            print '%s\t%s' % (current_user, current_count)
        current_count = int(count)
        current_user = user

if current_user == user:
    print '%s\t%s' % (current_user, current_count)
