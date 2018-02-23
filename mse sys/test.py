import time
import datetime

date11='2012-08-16 01:26:33'
date22='2012-08-16 06:26:33'
date1=time.strptime(date11,'%Y-%m-%d %H:%M:%S') 
date2=time.strptime(date22,'%Y-%m-%d %H:%M:%S')

print(date1)
date3=datetime.datetime(date1[0],date1[1],date1[2],date1[3],date1[4],date1[5]) 
date4=datetime.datetime(date2[0],date2[1],date2[2],date2[3],date2[4],date2[5])

a=(date4-date3).seconds/60
print(a)