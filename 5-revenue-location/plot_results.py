import matplotlib, sys
matplotlib.use('Agg')
import matplotlib.pyplot as m_plot
from ast import literal_eval
from math import sqrt

if __name__=='__main__':
    
    airports = [('081', '071600'),('081', '033100')]

    countyfp = {
        'Brooklyn': '047',
        'Bronx':    '005',
        'Manhattan':'061',
        'Queens':   '081',
        }

    colors = {'061': 'b',
               '047': 'r',
               '005':'y',
               '081':'g'}

    # read in census data
    incomes = {}
    households = {}
    with open(sys.argv[2],'r') as f_census:
        for text in f_census:
            lines = text.split('\r')
            for l in lines:
                values = l.split(',')
                if values[0] != 'Borough':
                    incomes[(countyfp[values[0]],values[1])] = values[3]
                    households[countyfp[values[0]],values[1]] = values[2]

    # read taxi revenue data
    data = []
    with open(sys.argv[1], 'r') as f_count:
        for line in f_count:
            values = line.strip().split(',')
            # exclude airports and locations with revenue in specified range
            if (values[0],values[1]) not in airport and 5000<float(values[3])<100000:
                data.append(values)

    # create figure
    fig = m_plot.figure(figsize=(15, 10))
    ylabels = ('tip','total fare')
    xlabels = ('income','households')

    axisnum = 0
    for i in range(0,2):
        axisnum += 1
        points = [(item[2+i],incomes[(item[0],item[1])],item[0]) for item in data if (item[0],item[1]) in incomes]
        values = zip(*points)
        ax = fig.add_subplot(2,2,2*i+1)
        ax.set_title('income v %s' % ylabels[i])
        ax.scatter(values[1], values[0], c=[colors[b] for b in values[2]], edgecolors='none')
        ax.set_ylabel('revenue from %s' % ylabels[i])
        ax.set_xlabel('median household income')
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
        ax.get_xaxis().tick_bottom()
        ax.get_yaxis().tick_left()
        ax.set_xlim([0,max(list(map(int,values[1])))])
        ax.set_ylim([0,max(list(map(float,values[0])))])

        points = [(item[2+i],households[(item[0],item[1])],item[0]) for item in data if (item[0],item[1]) in households]
        values = zip(*points)
        ax = fig.add_subplot(2,2,2*i+2)
        ax.set_title('households v %s' % ylabels[i])
        ax.scatter(values[1], values[0], c=[colors[b] for b in values[2]],edgecolors='none')   
        ax.set_ylabel('revenue from %s' % ylabels[i])  
        ax.set_xlabel('total households')   
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
        ax.get_xaxis().tick_bottom()
        ax.get_yaxis().tick_left()
        # ax.set_xlim([0,max(list(map(float,values[1])))]) # unfiltered
        ax.set_xlim([100,5000])
        ax.set_ylim([0,max(list(map(float,values[0])))])

    fig.tight_layout()
    fig.savefig(sys.argv[3])

