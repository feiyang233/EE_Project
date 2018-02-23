import csv
import os
import generate_time
date=''
time=generate_time.getime(date)

filename=''
rf1 = open(filename,'r') 
reader1=csv.reader(rf1)

newfilename='new'+filename
wf1=open(newfilename,'w')
writer1=csv.writer(wf1)

head1=next(reader1)
writer1.writerow(head1)
for row in reader1: #unify the time
	time=row[0]
	if time[-1:]!=1:
		row[0]=time[:-1]+'1'
	writer1.writerow(row)
	
rf1.close()
wf1.close()

os.remove(filename)
os.renames(newfilename,filename)

#--------------------------------

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
#-------------------------------

def repeat(L):   #列表去重，不改变原来的顺序
	L2=list(set(L))
	L2.sort(key=L.index)
	return L2


rf=open(creatfile,'r')
reader=csv.reader(rf)

total=[]
lis=[]
count=0
for row in reader:
	for i in row[2:]:
		total.append(i)
	count+=1
	if count==12:
		total=repeat(total)
		lis.append(len(total))
		total.clear()
		count=0
	if row[0]==date+'-07:55:01':
		break

for row in reader:
	for i in row[2:]:
		total.append(i)
	
	count+=1
	if count==60:
		total=repeat(total)
		lis.append(len(total))
		total.clear()
		count=0	
rf.close()
print(lis)