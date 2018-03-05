import csv
import os

#2
def unify(filename):

	rf1 = open(filename,'r') 
	reader1=csv.reader(rf1)
	mac_stu=[]
	mac_staff=[]
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
			row[6]='Student'
			mac_stu.append(row[1])
		elif row[6]=='NUS' or row[6]=='NUS_2-4GHz':
			row[6]='Staff'
			mac_staff.append(row[1])
		else:
			
			if row[1] in mac_stu:
				row[6]='Student'
			elif row[1] in mac_staff:
				row[6]='Staff'
			else:
				row[6]='Other'

		firsttime=row[14]
		row[14]=firsttime[0:10]+' '+firsttime[11:19]
		writer1.writerow(row)
		
	rf1.close()
	wf1.close()
	os.remove(filename)
	os.renames(newfilename,filename)
	print('unify success')



