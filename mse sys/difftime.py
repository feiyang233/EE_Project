import time
import datetime

def difftime(begintime,endtime):
	date1=time.strptime(begintime,'%Y-%m-%d %H:%M:%S') 
	date2=time.strptime(endtime,'%Y-%m-%d %H:%M:%S')

	date3=datetime.datetime(date1[0],date1[1],date1[2],date1[3],date1[4],date1[5]) 
	date4=datetime.datetime(date2[0],date2[1],date2[2],date2[3],date2[4],date2[5])

	minutes=(date4-date3).seconds/60

	return minutes
