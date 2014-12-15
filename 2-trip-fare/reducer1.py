#!/usr/bin/env python
import itertools, operator, sys
from ast import literal_eval

def parseInput():
    for line in sys.stdin:
        yield line.strip('\n').split('\t')
					
def reducer():
    for key, values in itertools.groupby(parseInput(), operator.itemgetter(0)):
        data = list(itertools.chain.from_iterable(sorted(map(literal_eval, zip(*values)[1]), key=lambda tup:len(tup))))
        if len(data) == 5:
        	print '%s,%s,%s,%s,%s,%s' % (literal_eval(key)[0], data[0], data[1], data[2], data[3], data[4])

if __name__=='__main__':
    reducer()

