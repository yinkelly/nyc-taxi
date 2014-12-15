#!/usr/bin/env python

# FINAL VERSION

import sys, time

def parseInput():
    for line in sys.stdin:
        values = line.strip('\n').split(',')

        # trip data, ignore missing geolocation
        if len(values)==14 and values[0]!='medallion' and int(values[8])!=0 and float(values[9])!=0.0:
        	# returns hack, pickup datetime, passenger count, trip-time-in-secs,trip-dist
        	yield [values[1],values[5],values[7],values[8],values[9]]

    	# fare data, ignore fares with $0 total
        if len(values)==11 and values[0]!='medallion' and float(values[10])!= 0.0:
        	# return hack, pickup datetime, tip, fare
        	yield [values[1],values[3], values[8], values[5]]


def mapper():
    for values in parseInput():
    	# key: pickup datetime and license, value: selected attributes
		print '%s\t%s' % ((values[0], values[1]),tuple(values[2:]))

if __name__=='__main__':
    mapper()
