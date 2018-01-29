import csv   #总表，行为device，列为时间
import generate_time
import uniform
from collections import Counter
import os
time=generate_time.getime(20180128)

def repeat(L):   #列表去重，不改变原来的顺序
	L2=list(set(L))
	L2.sort(key=L.index)
	return L2

filename='2018-01-28.csv' 
uniform.uniform(filename)

rf = open(filename,'r') 
reader = csv.reader(rf)
test=open('Overall'+filename,'w')
writer=csv.writer(test)

Mac=[]
h=next(reader)
for row in reader:
	Mac.append(row[1])	

Mac=repeat(Mac)

time.insert(0,'time')
Mac.insert(0,'Mac')

line=len(time)
Row=len(Mac)

list_2d=[['' for i in range(line)] for i in range(Row)] #创建二维list
list_2d[0]=time     #mac放进2维数据

n=0
for i in Mac:    #时间放进2维数组
	list_2d[n][0]=i #放时间
	n=n+1

rf.seek(0)
h=next(reader)
for row in reader:
	y=time.index(row[0])
	x=Mac.index(row[1])  #这里报错，是由于后面的覆盖导致的，所有当有错的时候，记得看之前的每一步，尤其是后面的循环。
	list_2d[x][y]=row[14]
	
for row in list_2d:
	writer.writerow(row)

rf.close()
test.close()

#-------------------------------------------
rf=open('Overall'+filename,'r')
reader=csv.reader(rf)
#wf=open('text.csv','w')
#writer=csv.writer(wf)

h=next(reader)
length=0
sumtime=0
for row in reader:
	row1=[n for n in row[85:] if n!='']
	word_counts = Counter(row1)
	top_three = word_counts.most_common(3)
	temp=top_three.copy()
	for i in temp:
		if i[1]<3 or i[1]>60:
			top_three.remove(i)
	for j in top_three:
		length+=1
		sumtime+=j[1]
	#top_three.insert(0,row[0])
	#writer.writerow(top_three)
	

print(sumtime/length)
rf.close()
#wf.close()

os.remove('Overall'+filename)	


