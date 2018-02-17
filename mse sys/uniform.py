import csv
import os

#2
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
		writer1.writerow(row)
		
	rf1.close()
	wf1.close()

	os.remove(filename)
	os.renames(newfilename,filename)
	print('unify success')
