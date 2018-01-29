import csv
import generate_time

date=20180127
time=generate_time.getime(date)
import os


filename='2018-01-27.csv'
rf=open(filename,'r')
reader=csv.reader(rf)

creatfile='TM'+filename
wf=open(creatfile,'w')
writer=csv.writer(wf)

Row=len(time)
list_2d=[['']for i in range(Row)] #创建二维list

n=0
for i in time:    #时间放进2维数组
	list_2d[n][0]=i #放时间
	n=n+1

lis=[]
i=0
h=next(reader)
for row in reader:
	X=time.index(row[0])
	list_2d[X].append(row[1])

for row in list_2d:
	row.insert(1,len(row)-1)
	writer.writerow(row)


rf.close()
wf.close()
#-----------------------------------

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


filename=creatfile
rf=open(filename,'r')
reader=csv.reader(rf)
wf=open('rate.csv','w')
writer=csv.writer(wf)
list1=['time','come','leave']

writer.writerow(list1)
for row in reader:
	if row[0]==str(date)+'-06:50:01':
		break

liscome=[]
lisleave=[]
temp=next(reader) #begin header
for row in reader:
	come,leave=rate(temp[1:],row[1:])
	temp=row
	list1=[row[0][9:],come,leave]
	writer.writerow(list1)
	#liscome.append(come)
	#lisleave.append(leave)
	if row[0]==str(date)+'-19:00:01':
		break

rf.close()
wf.close()
os.remove(creatfile)

