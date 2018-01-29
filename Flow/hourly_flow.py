import csv
import generate_time
from matplotlib import pyplot as plt
date=20180128
time=generate_time.getime(date)
import os


filename='2018-01-28.csv'
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
def repeat(L):   #列表去重，不改变原来的顺序
	L2=list(set(L))
	L2.sort(key=L.index)
	return L2

filename=creatfile
rf=open(filename,'r')
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
	if row[0]==str(date)+'-07:55:01':
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

print(lis)
rf.close()
x=range(24)
plt.figure("density")
plt.bar(x,lis,width =0.5)

for i in x:
	plt.text(i, lis[i]+1,str(lis[i]), ha='center')
plt.title('DECK'+str(date))
plt.savefig(str(date)+'DECK.png',dpi=200)
plt.show()

os.remove(creatfile)

