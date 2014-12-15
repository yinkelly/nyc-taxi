#!/usr/bin/env python
import sys, time

def parseInput():
    for line in sys.stdin:
        line = line.strip('\n').strip('\t')
        values = line.split(',')
        if len(values)>1: 
            yield values

def mapper():
    agg = {}
    for values in parseInput():
        # define key as weekday and hour
        key = (values[0], values[1])

        # aggregate total wait and trip count by key
        if key in agg:
            agg[key][0] += float(values[2])
            agg[key][1] += int(values[3])
        else:
            agg[key] = [float(values[2]),int(values[3])]
            
    for item in agg.iteritems():
        print '%s\t%s' % (item[0],tuple(item[1]))

if __name__=='__main__':
    mapper()
