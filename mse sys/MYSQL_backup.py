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
	tbn=loca[0:2]+loca[3:5]+'_'+filename[0:4]+filename[5:7]+filename[8:10]
	# 使用 cursor() 方法创建一个游标对象 cursor
	cursor = db.cursor()
	# 使用 execute() 方法执行 SQL，如果表存在则删除
	sqld="DROP TABLE IF EXISTS "+tbn 
	print(sqld)
	cursor.execute(sqld)
	# 使用预处理语句创建表
	sqlc = "CREATE TABLE "+ tbn +" (time DATETIME,mac varchar(50), location varchar(20),latitude FLOAT, longitude FLOAT)" #leave 居然是关键字
	cursor.execute(sqlc) 

	#db.commit()
	h=next(reader)
	for row in reader:
		lis=(row[0],row[1],loca,row[-2],row[-1])
		sql="insert into "+ tbn +"(time, mac, location,latitude, longitude) values (%s,%s,%s,%s,%s)"
		cursor.execute(sql,lis)

	db.commit() 
	# 关闭数据库连接
	db.close()
	rf.close()
	os.remove(filename)
	print('success write MySQL')

#mysqlwrite('2018-02-03.csv','E1-06')






