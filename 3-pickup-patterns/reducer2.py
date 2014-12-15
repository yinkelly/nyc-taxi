#!/usr/bin/env python
import itertools, operator, sys
from ast import literal_eval
import numpy as np

def parseInput():
    for line in sys.stdin:
        yield line.strip('\n').split('\t')

#http://en.wikibooks.org/wiki/Algorithm_Implementation/Strings/Levenshtein_distance#Python
def levenshtein(source, target):
    if len(source) < len(target):
        return levenshtein(target, source)
 
    # So now we have len(source) >= len(target).
    if len(target) == 0:
        return len(source)
 
    # We call tuple() to force strings to be used as sequences
    # ('c', 'a', 't', 's') - numpy uses them as values by default.
    source = np.array(tuple(source))
    target = np.array(tuple(target))
 
    # We use a dynamic programming algorithm, but with the
    # added optimization that we only need the last two rows
    # of the matrix.
    previous_row = np.arange(target.size + 1)
    for s in source:
        # Insertion (target grows longer than source):
        current_row = previous_row + 1
 
        # Substitution or matching:
        # Target and source items are aligned, and either
        # are different (cost of 1), or are the same (cost of 0).
        current_row[1:] = np.minimum(
                current_row[1:],
                np.add(previous_row[:-1], target != s))
 
        # Deletion (target grows shorter than source):
        current_row[1:] = np.minimum(
                current_row[1:],
                current_row[0:-1] + 1)
 
        previous_row = current_row
    return previous_row[-1]

def reducer():
    agg = {}
    for key, values in itertools.groupby(parseInput(), operator.itemgetter(0)):
        sequences = map(literal_eval,zip(*values)[1])

        # calc average edit distance
        distances = []
        counts = {}
        # find min edit sequence

        # taxi drive must have worked over 50 shifts
        if len(sequences)>3: #50:
            for i,s1 in enumerate(sequences):
                # filter by number of picks per sequence(day)
                if len(s1) > 5:
                    for j,s2 in enumerate(sequences[i+1:]):
                        if len(s2) > 5:
                            distances.append(levenshtein(s1,s2))

                    # for each sequence hash locations
                    for neighborhood in s1:
                        counts[neighborhood] = counts.get(neighborhood,0) + 1

                    # calc mean dist
                    mean_dist = np.mean(distances)
                    std_dist = np.std(distances)

                    # calc modvr
                    fm = max(counts.iteritems(), key=operator.itemgetter(1))
                    modvr = 99*(1-(fm[1]/float(sum(counts.values()))))/float(98)

            print '%s,%s,%s,%s,%s' % (key, modvr, fm[0], mean_dist, std_dist)

if __name__=='__main__':
    reducer()
