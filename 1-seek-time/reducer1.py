#!/usr/bin/env python
import itertools, operator, sys, time
from ast import literal_eval

def parseInput():
    for line in sys.stdin:
        yield line.strip('\n').split('\t')

def reducer():
    agg = {}
    for key, values in itertools.groupby(parseInput(), operator.itemgetter(0)):
        for val in values:
        	# sort list of pickup and dropoff times in chronological order
        	val = sorted(literal_eval(val[1]))
        	for index,times in enumerate(val):
        		if index+1 < len(val):
        			# calculate wait time by subtracting dropoff time by next trip's pickup time
	        		do_time = time.strptime(times[1], '%Y-%m-%d %H:%M:%S')
	        		pu_time = time.strptime(val[index+1][0], '%Y-%m-%d %H:%M:%S')
	        		wait = (time.mktime(pu_time) - time.mktime(do_time))/60

	        		# aggregate by weekday and hour 
	        		time_tuple = (do_time.tm_wday,do_time.tm_hour)

	        		# define boundaries for wait time	        		
	        		if wait>0 and wait<120:
	        			if time_tuple in agg: 
	        				agg[time_tuple]['total_wait'] += wait
	        				agg[time_tuple]['count'] += 1
	        			else:
	        				agg[time_tuple] = {'total_wait':wait, 'count':1}

    for item in agg.iteritems():
    	# prints weekday, hour, wait time, count
        print '%s,%s,%s,%s' % (item[0][0],item[0][1],str(item[1]['total_wait']),item[1]['count'])

if __name__=='__main__':
    reducer()
