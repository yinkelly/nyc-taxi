#!/usr/bin/env python
import itertools, operator, sys, time
from ast import literal_eval

def parseInput():
    for line in sys.stdin:
        yield line.strip('\n').split('\t')

def reducer():
    agg = {}
    for key, values in itertools.groupby(parseInput(), operator.itemgetter(0)):
    	# aggregates total wait and count by weekday and hour
        key = literal_eval(key)
        total = 0
        count = 0
        for val in values:
        	tup_val = literal_eval(val[1])
        	total += float(tup_val[0])
        	count += int(tup_val[1])

        print '%s,%s,%s,%s' % (key[0],key[1],str(total),count)

if __name__=='__main__':
    reducer()
