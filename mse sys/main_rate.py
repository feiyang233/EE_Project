import time_mac
import csv
import os
import pymysql

def rate(name):
	time_mac.time_mac(name)
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

	db = pymysql.connect("localhost","root","feiyang","feiyang" )

	# 使用 cursor() 方法创建一个游标对象 cursor
	cursor = db.cursor()
	# 使用 execute() 方法执行 SQL，如果表存在则删除
	cursor.execute("DROP TABLE IF EXISTS rate")
	 
	# 使用预处理语句创建表
	try:
		sql = "CREATE TABLE rate (Time DATETIME,Inflow int, Outflow int)" #leave 居然是关键字
		cursor.execute(sql) 
	except pymysql.InternalError as e:
		code, message = e.args
		print (">>>>>>>>>>>>>", code, message)

	liscome=[]
	lisleave=[]
	temp=next(reader) #begin header
	cursor.execute("insert into rate (Time,Inflow,Outflow) values (%s,%s,%s)",([temp[0],0,0]))
	db.commit()

	for row in reader:
		come,leave=rate(temp[1:],row[1:])
		temp=row
		list1=[row[0],come,leave]
		cursor.execute("insert into rate (Time,Inflow,Outflow) values (%s,%s,%s)",(list1))
	db.commit()
	rf.close()
	print('Calculate rate success')
	os.remove(name)



