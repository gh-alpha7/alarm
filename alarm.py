import os
import datetime


xy=list()
a=("year","month","date","hour","minute","second")
x=6
for i in range(int(x)):
    n=input(a[i]+" ")
    xy.append(int(n))


settime=datetime.datetime(xy[0],xy[1],xy[2],xy[3],xy[4],xy[5])
now=datetime.datetime.now()
while settime>now:
    now=datetime.datetime.now()

os.startfile('c:/Users/Alpha/Documents/ehsa.wma','open')

#os.system('start c:/Users/Alpha/Documents/ehsa.')


exit()
