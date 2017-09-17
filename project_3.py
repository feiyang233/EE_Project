import csv 
def repeat(L):   #去重
	L2=list(set(L))
	L2.sort(key=L.index)
	return L2

rf = open('2017-09-07.csv','r') 
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
row=len(time)+2
line=len(Mac)+2

list_2d=[['' for i in range(line)] for i in range(row)] #创建二维list
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
	list_2d[x][y]=location
	count=int(list_2d[x][1])+1
	list_2d[x][1]=count 
	
	in_time=int(list_2d[1][y])+1
	list_2d[1][y]=in_time




for row in list_2d:
	writer.writerow(row)
	

rf.close()
test.close()




	


