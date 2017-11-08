import csv   #总表，行为device，列为时间

def repeat(L):   #列表去重，不改变原来的顺序
	L2=list(set(L))
	L2.sort(key=L.index)
	return L2
#一列删除功能
def delete(y_):
	for i in range(Row):
		del list_2d[i][y_]

filename='2017-11-01.csv'

rf = open(filename,'r') 
reader = csv.reader(rf)
test=open('overall'+filename,'w')
writer=csv.writer(test)
Mac=[]
time=[]
for row in reader:
	time.append(row[0])
	Mac.append(row[1])	

Mac=repeat(Mac)
time=repeat(time)

time.insert(1,'individual_time')
Mac.insert(0,'TIME')
Mac.insert(1,len(Mac))
line1=len(Mac)

for i in range(2,2*line1,2):
	Mac.insert(i,'first\last')

Row=len(time)
line=len(Mac)

list_2d=[['' for i in range(line)] for i in range(Row)] #创建二维list
list_2d[0]=Mac     #mac放进2维数据
list_2d[1]=[0 for i in range(line)]

n=0
for i in time:    #时间放进2维数组
	
	list_2d[n][0]=i #放时间
	list_2d[n][1]=0 #统计这一时刻有多少device
	n=n+1


rf.seek(0)
for row in reader:
	x=time.index(row[0])
	y=Mac.index(row[1])  #这里报错，是由于后面的覆盖导致的，所有当有错的时候，记得看之前的每一步，尤其是后面的循环。
	location=row[16]+'\\'+row[17]  
	fltime=row[14][5:19]+'\\'+row[15][5:19]
	list_2d[x][y]=location
	list_2d[x][y+1]=fltime
	count=int(list_2d[x][1])+1
	list_2d[x][1]=count 
	if x<98:
		in_time=int(list_2d[1][y])+5  #统计每个device出现的时间一共是多少，8点前
	else:
		in_time=int(list_2d[1][y])+1  #8点后的
	list_2d[1][y]=in_time

list_2d[0][1]=line1-3 #设备统计修正

for i in range(3): #  first\last  latitude\longitude  LocatedTime\ocatedTime

	delete(2)       #多余的三行


for row in list_2d:
	writer.writerow(row)


rf.close()
test.close()




	


