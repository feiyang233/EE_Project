import csv
import os

def unify(filename):

	rf1 = open(filename,'r') 
	reader1=csv.reader(rf1)

	newfilename='new'+filename
	wf1=open(newfilename,'w')
	writer1=csv.writer(wf1)

	head1=next(reader1)
	writer1.writerow(head1)
	for row in reader1: #unify the time 末位秒
		time=row[0]
		if time[-1:]!=1:
			row[0]=time[:-1]+'1'
		time=row[0]
		row[0]=time[0:4]+'-'+time[4:6]+'-'+time[6:8]+' '+time[9:] 
		#数据库的时间格式YYYY-MM-DD HH:MM:SS
		if row[6]=='NUS_STU' or row[6]=='NUS_STU_2-4GHz':
			row[6]='student'
		elif row[6]=='NUS' or row[6]=='NUS_2-4GHz':
			row[6]='staff'
		else:
			row[6]='other'
		firsttime=row[14]
		row[14]=firsttime[0:10]+' '+firsttime[11:19]
		writer1.writerow(row)
		
	rf1.close()
	wf1.close()

	os.remove(filename)
	os.renames(newfilename,filename)
	print('unify success')
