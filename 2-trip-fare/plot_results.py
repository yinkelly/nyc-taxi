import matplotlib, sys
matplotlib.use('Agg')
import matplotlib.pyplot as m_plot

if __name__=='__main__':
    data = []
    with open(sys.argv[1], 'r') as f:
        for line in f:
            data.append(map(float, line.strip().split(',')))

    fig = m_plot.figure(figsize=(15, 7))
    # fig.suptitle('', fontsize=20)

    colors = ('b')
    weekdays = ('Mon', 'Tues','Wed','Thurs','Fri','Sat','Sun')
    ylabels = ('tip','fare')
    xlabels = ('passengers','time','distance','distance/time')
    xlims = ([1,6],[0,160],[0,30],[0,.0003])
    axisnum = 0
    for i in range(0,2):
        for j in range(0,4):
            axisnum += 1

            # calculate the averate for each attribute in tuple
            # values are filtered by average distance and time. Those with ave dist over 20mi or length over 150min are ignored
            if j == 3:
                # distance/time
                points = [(item[i]/item[5],(item[4]/item[3])/60) for item in data if ((item[4]/item[5]<30) and (item[3]/60/item[5]<150)) ]
            elif j == 1:
                # time
                points = [(item[i]/item[5],(item[2+j]/item[5])/60) for item in data if ((item[4]/item[5]<30) and (item[3]/60/item[5]<150)) ]
            else:
                points = [(item[i]/item[5],item[2+j]/item[5]) for item in data if ((item[4]/item[5]<30) and (item[3]/60/item[5]<150)) ]
            
            values = zip(*points)
            ax = fig.add_subplot(2,4,axisnum)
            ax.set_title('%s v %s' % (xlabels[j],ylabels[i]))
            # ax = fig.add_axes([.1,.1,.7,.7])
            ax.plot(values[1], values[0], linestyle='None',marker='.', color='b', label=weekdays[i])
            
            ax.set_xlim(xlims[j])
            ax.spines['top'].set_visible(False)
            ax.spines['right'].set_visible(False)
            ax.get_xaxis().tick_bottom()
            ax.get_yaxis().tick_left()

    fig.tight_layout()
    fig.savefig(sys.argv[2])