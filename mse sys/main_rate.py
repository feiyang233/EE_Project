import time_mac
import csv
import os
def rate(name):
	time_mac.time_mac(name)
	def rate(L1,L2):
		come=0
		leave=0
		for i in L2:
			if i not in L1:
				come+=1
		for i in L1:
			if i not in L2:
				leave+=1
		return come,leave

	rf=open(name,'r')
	reader=csv.reader(rf)
	wf=open('rate.csv','w')
	writer=csv.writer(wf)
	list1=['Time','Inflow','Outflow']

	writer.writerow(list1)
	liscome=[]
	lisleave=[]
	temp=next(reader) #begin header
	for row in reader:
		come,leave=rate(temp[1:],row[1:])
		temp=row
		list1=[row[0],come,leave]
		writer.writerow(list1)

	rf.close()
	wf.close()
	print('Calculate rate success')
	os.remove(name)


