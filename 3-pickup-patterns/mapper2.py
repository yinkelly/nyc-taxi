#!/usr/bin/env python
import sys, time
from ast import literal_eval

def parseInput():
    for line in sys.stdin:
        line = line.strip('\n')
        values = line.split('\t')
        if len(values)>1: 
            yield values

def mapper():
    for values in parseInput():
        driver = literal_eval(values[0])[0]
        print '%s\t%s' % (driver,values[1]) 

if __name__=='__main__':
    mapper()
