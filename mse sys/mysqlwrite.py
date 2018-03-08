#!/usr/bin/env python3
# -*- coding: utf-8 -*-

########## prepare ##########
import csv
import pymysql
import os
import difftime
# 打开数据库连接
def mysqlwrite(filename,loca):
	db = pymysql.connect("localhost","root","feiyang","feiyang" )
	rf=open(filename,'r') 
	reader=csv.reader(rf)

	# 使用 cursor() 方法创建一个游标对象 cursor
	cursor = db.cursor()
	# 使用 execute() 方法执行 SQL，如果表存在则删除
	cursor.execute("DROP TABLE IF EXISTS test")
	 
	# 使用预处理语句创建表
	try:
		sql = "CREATE TABLE test (Time DATETIME,Firstime DATETIME,Dwell FLOAT,User varchar(50),Type varchar(10), Location varchar(20),Latitude FLOAT, Longitude FLOAT)" #leave 居然是关键字
		cursor.execute(sql) 
	except pymysql.InternalError as e:
		code, message = e.args
		print (">>>>>>>>>>>>>", code, message)


	db.commit()
	h=next(reader)
	for row in reader:
		dwelltime=difftime.difftime(row[14],row[0])
		lis=[row[0],row[14],dwelltime,row[1],row[6],loca,row[-2],row[-1]]
		cursor.execute("insert into test (Time,Firstime,Dwell, User, Type,Location,Latitude, Longitude) values (%s,%s,%s,%s,%s,%s,%s,%s)",(lis))

	db.commit() 
	# 关闭数据库连接
	db.close()
	rf.close()
	#os.remove(filename) 等速度计算后删除
	print('success write MySQL')

#mysqlwrite('2017-09-07.csv','E1')
