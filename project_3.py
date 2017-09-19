import csv 
def repeat(L):   #去重
	L2=list(set(L))
	L2.sort(key=L.index)
	return L2
#删除功能，待完成
def delete(y_):
	for i in range(Row):
		del list_2d[i][y_]

rf = open('2017-09-02.csv','r') 
reader = csv.reader(rf)
test=open('info.csv','w')
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
	
	list_2d[n][0]=i
	list_2d[n][1]=0
	n=n+1


rf.seek(0)
for row in reader:
	x=time.index(row[0])
	y=Mac.index(row[1])
	location=row[16]+'\\'+row[17]  
	fltime=row[14][5:19]+'\\'+row[15][5:19]
	list_2d[x][y]=location
	list_2d[x][y+1]=fltime
	count=int(list_2d[x][1])+1
	list_2d[x][1]=count 
	if x<98:
		in_time=int(list_2d[1][y])+5
	else:
		in_time=int(list_2d[1][y])+1
	list_2d[1][y]=in_time

list_2d[0][1]=line1-3

for i in range(3):
	delete(2)


for row in list_2d:
	writer.writerow(row)


rf.close()
test.close()




	


