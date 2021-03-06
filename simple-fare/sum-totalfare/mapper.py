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
        pickup_time = time.strptime(values[3], '%Y-%m-%d %H:%M:%S')
        day = pickup_time.tm_yday
        agg[day] = agg.get(day, 0) + float(values[10].strip())

    for item in agg.iteritems():
        print '%s\t%s' % item

if __name__=='__main__':
    mapper()
