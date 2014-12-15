#!/usr/bin/env python
import itertools, operator, sys
from ast import literal_eval

def parseInput():
    for line in sys.stdin:
        yield line.strip('\n').split('\t')

def reducer():
    agg = {}
    for key, values in itertools.groupby(parseInput(), operator.itemgetter(0)):
        key = literal_eval(key)
        tip = 0
        total = 0
        count = 0
    	for val in values:
            stats = literal_eval(val[1])
            tip += float(stats[0])
            total += float(stats[1])
            count += int(stats[2])

        print '%s,%s,%s,%s,%s' % (key[0],key[1],str(tip),str(total),str(count))

if __name__=='__main__':
    reducer()