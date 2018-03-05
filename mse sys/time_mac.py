import csv
import generate_time
import os
def time_mac(filename):
	date=filename[0:10]
	time=generate_time.getime(date)

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
	h=next(reader) #跳过第一行 time, mac. 写入的全是数据
	for row in reader:
		X=time.index(row[0])
		list_2d[X].append(row[1])

	for row in list_2d:
		row.insert(1,len(row)-1)
		writer.writerow(row)

	rf.close()
	wf.close()
	os.remove(filename)
	os.renames(creatfile,filename)
	print('time-mac success')