import uniform
import time_mac
import csv
import copy


# copy(date,location)
date='20180215'
location='E1-06'

name=copy.copy(date,location)
uniform.unify(name)
time_mac.time_mac(name)
date=name[0:4]+name[5:7]+name[8:10]
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
wf=open(date+location+'rate.csv','w')
writer=csv.writer(wf)
list1=['time','come','leave']

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


