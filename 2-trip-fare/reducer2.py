#!/usr/bin/env python
import itertools, operator, sys
from ast import literal_eval

def parseInput():
    for line in sys.stdin:
        yield line.strip('\n').split('\t')

def reducer():
    for key, values in itertools.groupby(parseInput(), operator.itemgetter(0)):
    	l = map(literal_eval,zip(*values)[1])
    	print '%s,%s,%s,%s,%s,%s' % tuple([sum(i) for i in zip(*l)])

if __name__=='__main__':
    reducer()
