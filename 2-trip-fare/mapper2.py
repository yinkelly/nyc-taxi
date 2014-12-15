#!/usr/bin/env python
import sys, time

def parseInput():
    for line in sys.stdin:
        line = line.strip('\n').strip('\t')
        values = line.split(',')
        if len(values)>1 and values[0]!='medallion': 
            yield values

# TODO 
def mapper():
    agg = {}
    for values in parseInput():
        driver = values[0]
        agg[driver] = [x+y for x,y in zip(agg.get(driver,[0,0,0,0,0,0]),map(float,values[1:])+[1])]

    for item in agg.iteritems():
        print '%s\t%s' % item

if __name__=='__main__':
    mapper()
