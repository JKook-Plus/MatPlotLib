from datetime import datetime
import matplotlib.pyplot
import matplotlib.dates







templist = []





while True:
    
    
    
    x1 = input("What Is The Temp Now? ")
    
    if x1 == "":
        break

    
    
    else:
        x1num = int(x1)
        timestamp = datetime.now()
        templist.append((x1num,timestamp))
    
    





print (templist)
k,v=zip(*templist)
print (k)
print (v)

matplotlib.pyplot.style.use('dark_background')

dates = matplotlib.dates.date2num(v)
matplotlib.pyplot.plot_date(dates, k)
matplotlib.pyplot.gcf().autofmt_xdate()
#plt.plot(v,k)
matplotlib.pyplot.show()
