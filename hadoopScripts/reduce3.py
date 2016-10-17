#!/usr/bin/env python

from operator import itemgetter
import sys

current_movie = None
rating_list = []
movie = None

for line in sys.stdin:
    line = line.strip()

    movie, rating = line.split('\t', 1)

    if current_movie == movie:
        rating_list.append(float(rating))
    else:
        if current_movie:
            print '%s\t%.2f' % (current_movie, sum(rating_list)/len(rating_list))
        rating_list = [float(rating)]
        current_movie = movie

if current_movie == movie:
    print '%s\t%.2f' % (current_movie, sum(rating_list)/len(rating_list))
