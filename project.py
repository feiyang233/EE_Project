import csv 
rf = open('2017-09-02.csv','r') 
reader = csv.reader(rf)
test=open('test.csv','w')
writer=csv.writer(test)
buffer1=["first line"]
last_time='0'
count=0          #计数器
for row in reader:
	time=row[13][0:19]
	if time!=last_time:
		last_time=time
		buffer1.insert(1,count)    #将个数放在第二位
		writer.writerow(buffer1)
		buffer1=[]
		count=0
		buffer1.append(time)
	MAC,APmac,lat,lon=row[1],row[8],row[16],row[17]
	buffer1.extend([MAC,APmac,lat,lon])
	count=count+1
rf.close()
test.close()



	


