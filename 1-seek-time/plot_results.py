import matplotlib, sys
matplotlib.use('Agg')
import matplotlib.pyplot as m_plot

if __name__=='__main__':
    data = []
    with open(sys.argv[1], 'r') as f:
        for line in f:
            data.append(map(float, line.strip().split(',')))

    fig = m_plot.figure(figsize=(14, 7))
    fig.suptitle('Seek time vs Hour', fontsize=20)

    colors = ('b','g','r','c','m','y','k')
    weekdays = ('Mon', 'Tues','Wed','Thurs','Fri','Sat','Sun')
    for i in range(0,7):
        hr_ave_by_wkday = [(h,s/c) for w,h,s,c in data if w==i]
        hr_ave_by_wkday.sort()
        values = zip(*hr_ave_by_wkday)

        ax = fig.add_axes([.1,.1,.7,.7])
        ax.plot(values[0], values[1], color=colors[i], label=weekdays[i])
        
    ax.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
    ax.set_xlim([0,23])
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.get_xaxis().tick_bottom()
    ax.get_yaxis().tick_left()
    ax.set_ylabel('seek time')
    ax.set_xlabel('hour of day')
    fig.savefig(sys.argv[2])
