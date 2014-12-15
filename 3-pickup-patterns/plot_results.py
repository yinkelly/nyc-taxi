import matplotlib, sys
matplotlib.use('Agg')
import matplotlib.pyplot as m_plot
from ast import literal_eval
from math import sqrt

if __name__=='__main__':
    
    neighborhoods = {}
    # read edit distance data
    data = []
    with open(sys.argv[1], 'r') as f_count:
        for line in f_count:
            values = line.strip().split(',')
            # exclude bad data
            if values[4] != 'nan' and values[4] != '0.0':
                data.append(values)
                neighborhoods[values[2]] = neighborhoods.get(values[2],0) + 1

    # data
    neighborhoods = neighborhoods.items()
    neighborhoods = sorted(neighborhoods, key=lambda x: x[1],reverse=True)
    neighborhoods = neighborhoods[:10]
    modvr = [item[1] for item in data]
    dist = [item[3] for item in data]
    modvr = map(float,modvr)
    dist = map(float,dist)
    
    fig = m_plot.figure(figsize=(15, 7))

    ax = fig.add_subplot(2,2,1)
    ax.hist(modvr, 50, normed=1, facecolor='blue', alpha=0.5)
    ax.spines['top'].set_visible (False)
    ax.spines['right'].set_visible(False)
    ax.get_xaxis().tick_bottom()
    ax.get_yaxis().tick_left()
    ax.set_ylabel('frequency')  
    ax.set_xlabel('variance from the mode')  

    ax = fig.add_subplot(2,2,2)
    ax.hist(dist, 50, normed=1, facecolor='blue', alpha=0.5)
    ax.spines['top'].set_visible (False)
    ax.spines['right'].set_visible(False)
    ax.get_xaxis().tick_bottom()
    ax.get_yaxis().tick_left()
    ax.set_ylabel('frequency')  
    ax.set_xlabel('average distance')  

    ax = fig.add_subplot(2,2,3)
    names, values = zip(*neighborhoods)
    yticks = map(lambda x: len(neighborhoods)-x-0.5,range(len(names)))
    ax.barh(yticks, values, align='center',alpha=0.5)
    ax.set_yticks(yticks, minor=False)
    ax.set_yticklabels(names, fontdict=None, minor=False)
    ax.spines['top'].set_visible (False)
    ax.spines['right'].set_visible(False)
    ax.get_xaxis().tick_bottom()
    ax.get_yaxis().tick_left()
    ax.set_ylabel('neighborhoods')  
    ax.set_xlabel('mode frequency')  

    ax = fig.add_subplot(2,2,4)
    ax.scatter(modvr, dist, c='b', edgecolors='none',alpha=0.5)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.get_xaxis().tick_bottom()
    ax.get_yaxis().tick_left()
    ax.set_ylabel('average distance')  
    ax.set_xlabel('variance from mode')  
    ax.set_xlim([0.01,1])
    ax.set_ylim([0,55])


    fig.tight_layout()
    fig.savefig(sys.argv[2])

