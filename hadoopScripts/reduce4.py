#!/usr/bin/env python

from operator import itemgetter
import sys

current_movie = None
rating_list = []
movie = None

faixa1_2 = 0
faixa2_3 = 0
faixa3_4 = 0
faixa4_5 = 0

for line in sys.stdin:
    line = line.strip()

    movie, rating = line.split('\t', 1)

    if current_movie == movie:
        rating_list.append(float(rating))
    else:
        if current_movie:
            media = sum(rating_list)/len(rating_list)
            if media >= 1 and media < 2:
                faixa1_2 += 1
            if media >= 2 and media <3:
                faixa2_3 += 1
            if media >= 3 and media < 4:
                faixa3_4 += 1
            if media >=1  and media <= 5:
                faixa4_5 += 1
        rating_list = [float(rating)]
        current_movie = movie

if current_movie == movie:
    media = sum(rating_list)/len(rating_list)
    if media >= 1 and media < 2:
        faixa1_2 += 1
    if media >= 2 and media <3:
        faixa2_3 += 1
    if media >= 3 and media < 4:
        faixa3_4 += 1
    if media >=1  and media <= 5:
        faixa4_5 += 1

print '%s\t%s' % ('faixa1_2',faixa1_2)
print '%s\t%s' % ('faixa2_3',faixa2_3)
print '%s\t%s' % ('faixa3_4',faixa3_4)
print '%s\t%s' % ('faixa4_5',faixa4_5)
