#!/usr/bin/env python
import sys, time

def parseInput():
    for line in sys.stdin:
        line = line.strip('\n')
        values = line.split(',')
        if len(values)>1 and values[0]!='medallion': 
            yield values

def mapper():
    agg = {}
    for values in parseInput():
        # key:license, value: list of pickup and dropoff times
        if values[1] in agg:
            agg[values[1]].append((values[5],values[6]))
        else:
            agg[values[1]] = [(values[5],values[6])]

    for item in agg.iteritems():
        print '%s\t%s' % item

if __name__=='__main__':
    mapper()
