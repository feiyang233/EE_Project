#!/usr/bin/env python3
# -*- coding: utf-8 -*-

########## prepare ##########
import csv
import pymysql
import os

# 打开数据库连接
def mysqlwrite(filename,loca):
	db = pymysql.connect("localhost","root","feiyang","MSE" )
	rf=open(filename,'r') 
	reader=csv.reader(rf)

	# 使用 cursor() 方法创建一个游标对象 cursor
	cursor = db.cursor()
	# 使用 execute() 方法执行 SQL，如果表存在则删除
	cursor.execute("DROP TABLE IF EXISTS test")
	 
	# 使用预处理语句创建表
	try:
		sql = "CREATE TABLE test (time DATETIME,mac varchar(50), location varchar(20),latitude FLOAT, longitude FLOAT)" #leave 居然是关键字
		cursor.execute(sql) 
	except pymysql.InternalError as e:
		code, message = e.args
		print (">>>>>>>>>>>>>", code, message)


	#db.commit()
	h=next(reader)
	for row in reader:
		lis=[row[0],row[1],loca,row[-2],row[-1]]
		cursor.execute("insert into test (time, mac, location,latitude, longitude) values (%s,%s,%s,%s,%s)",(lis))

	db.commit() 
	# 关闭数据库连接
	db.close()
	rf.close()
	os.remove(filename)
	print('success write MySQL')

#mysqlwrite('2017-09-07.csv','E1')
