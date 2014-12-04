#!/usr/bin/env python
import itertools, operator, sys
from ast import literal_eval

def parseInput():
    for line in sys.stdin:
        yield line.strip('\n').split('\t')

def reducer():
    agg = {}
    for key, values in itertools.groupby(parseInput(), operator.itemgetter(0)):
        day = int(key)
        totalfare = 0
        totaltip = 0
        count = 0

        for val in values:
        	val = literal_eval(val[1])
        	totalfare += val[0]
        	totaltip += val[1]
        	count += val[2]

        print '%s,%s,%s,%s' % (day, totalfare, totaltip, count)

if __name__=='__main__':
    reducer()
