#!/usr/bin/env python
import itertools, operator, sys, time
from ast import literal_eval

def parseInput():
    for line in sys.stdin:
        yield line.strip('\n').split('\t')

def reducer():
    driver = {}
    for key, values in itertools.groupby(parseInput(), operator.itemgetter(0)):
    	key = literal_eval(key)
    	pickups = map(literal_eval,zip(*values)[1])
    	pickups.sort()
    	pickup_time = time.strptime(pickups[0][0], '%Y-%m-%d %H:%M:%S')

    	# filter by shift, first pickup must be between 5am-9am
    	if 4<pickup_time.tm_hour<9:
	    	neighborhoods = [i[1] for i in pickups]
	        print '%s\t%s' % (key, neighborhoods)

if __name__=='__main__':
    reducer()
