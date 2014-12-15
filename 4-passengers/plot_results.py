import matplotlib, sys
matplotlib.use('Agg')
import matplotlib.pyplot as m_plot
from ast import literal_eval
from math import sqrt

if __name__=='__main__':
    data = []

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

    # read in data
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

    with open(sys.argv[1], 'r') as f_count:
        for line in f_count:
            # exclude airports and locations with revenue in specified range
            values = line.strip().split('\t')
            if str((values[0],values[1])) not in airports and 1000<float(values[1])<100000:
                data.append(values)

    # create figure
    fig = m_plot.figure(figsize=(15, 7))

    # passengers v income 
    points_income = [(item[1],incomes[literal_eval(item[0])],literal_eval(item[0])[0]) for item in data if literal_eval(item[0]) in incomes ]
    values_income = zip(*points_income)
    ax = fig.add_subplot(1,2,1)
    ax.set_title('passengers v income')
    ax.scatter(values_income[1], values_income[0], c=[colors[b] for b in values_income[2]], edgecolors='none')
    ax.set_ylabel('passengers picked up')
    ax.set_xlabel('median household income')
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.get_xaxis().tick_bottom()
    ax.get_yaxis().tick_left()
    ax.set_xlim([0,max(list(map(float,values_income[1])))])
    ax.set_ylim([0,max(list(map(float,values_income[0])))])

    # passenger v household
    points_households =  [(item[1],households[literal_eval(item[0])],literal_eval(item[0])[0]) for item in data if literal_eval(item[0]) in households]
    values_households = zip(*points_households)
    ax = fig.add_subplot(1,2,2)
    ax.set_title('passengers v households')
    ax.scatter(values_households[1], values_households[0], c=[colors[b] for b in values_households[2]], edgecolors='none')
    ax.set_ylabel('passengers picked up')
    ax.set_xlabel('number households')
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.get_xaxis().tick_bottom()
    ax.get_yaxis().tick_left()
    ax.set_xlim([0,max(list(map(float,values_households[1])))])
    ax.set_ylim([0,max(list(map(float,values_households[0])))])


    fig.savefig(sys.argv[3])

    # calculate correlation coefficients
    n = float(len(values_households[0]))
    sum_passengers = float(sum(map(int,values_households[0])))
    # print(values_income[1])

    sum_income = float(sum(map(int,values_income[1])))
    sum_household = float(sum(map(int,values_households[1])))
    sq_passengers = float(sum([int(i)*int(i) for i in values_households[0]]))
    sq_income = float(sum([int(i)*int(i) for i in values_income[1]]))
    sq_household = float(sum([int(i)*int(i) for i in values_households[1]]))
    housepass = float(sum([int(x)*int(y) for x,y in zip(values_households[0],values_households[1])]))
    incomepass = float(sum([int(x)*int(y) for x,y in zip(values_households[0],values_income[1])]))

    cor_coef_house = (n*housepass - sum_household*sum_passengers)/( (sqrt(n*sq_household - sum_household*sum_household)*sqrt(n*sq_passengers - sum_passengers*sum_passengers) ))
    cor_coef_income = (n*incomepass - sum_income*sum_passengers)/( (sqrt(n*sq_income - sum_income*sum_income)*sqrt(n*sq_passengers - sum_passengers*sum_passengers) ))

    print 'correliation coeff between household and service: %f' % cor_coef_house
    print 'correliation coeff between income and service: %f' % cor_coef_income
