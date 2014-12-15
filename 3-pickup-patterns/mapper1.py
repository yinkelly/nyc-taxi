#!/usr/bin/env python
import sys
sys.path.append('.')
import matplotlib
matplotlib.use('Agg')
from matplotlib.path import Path
from rtree import index as rtree
import numpy, shapefile, time

def findNeighborhood(location, index, neighborhoods):
    match = index.intersection((location[0], location[1], location[0], location[1]))
    for a in match:
        if any(map(lambda x: x.contains_point(location), neighborhoods[a][1])):
            return a
    return -1

def readNeighborhood(shapeFilename, index, neighborhoods):
    sf = shapefile.Reader(shapeFilename)
    for sr in sf.shapeRecords():
        if sr.record[1] not in ['New York', 'Kings', 'Queens', 'Bronx']: continue
        paths = map(Path, numpy.split(sr.shape.points, sr.shape.parts[1:]))
        bbox = paths[0].get_extents()
        map(bbox.update_from_path, paths[1:])
        index.insert(len(neighborhoods), list(bbox.get_points()[0])+list(bbox.get_points()[1]))
        neighborhoods.append((sr.record[3], paths))
    neighborhoods.append(('UNKNOWN', None))

def parseInput():
    for line in sys.stdin:
        line = line.strip('\n')
        values = line.split(',')
        if len(values)>1 and values[0]!='medallion': 
            yield values

def mapper():
    index = rtree.Index()
    neighborhoods = []
    readNeighborhood('ZillowNeighborhoods-NY.shp', index, neighborhoods)
    agg = {}
    for vals in parseInput():
         # add if statement to filter, 5am-5pm, 5pm-5am
        if (0<int(vals[7])<7) and (120<int(vals[8])<7200) and (0.1<float(vals[9])<20) and (vals[10]!='0') and (vals[11]!='0'):
            pickup_location = (float(vals[10]), float(vals[11]))
            pickup_neighborhood = findNeighborhood(pickup_location, index, neighborhoods)
            if pickup_neighborhood!=-1:
                pickup_time = time.strptime(vals[5], '%Y-%m-%d %H:%M:%S')
                day = pickup_time.tm_yday
                key = (vals[1],day) # driver,day
                value = (vals[5],neighborhoods[pickup_neighborhood][0])
                print '%s\t%s' % (key,value) 


if __name__=='__main__':
    mapper()
