import os
import os.path
import shutil  
from datetime import datetime
import zipfile

#1
def copy(date,location):
	date_csv=date[0:4]+'-'+date[4:6]+'-'+date[-2:]+'.csv'

	week = datetime.strptime(date,"%Y%m%d").strftime("%W")

	workdir='/Volumes/DATACOMM/weekly_archive/nuswifi/device_location/'
	filelist=os.listdir(workdir)
	
	subpath=''
	for i in filelist:
		if i.endswith(location):
			subpath=i+'/'
			print(subpath)
			break

	if subpath=='':
		print('no this location')
		return -1

	
	path_csv=workdir+subpath
	filename_zip=date[0:4]+'_week'+str(week)+'.zip'
	shutil.copyfile(path_csv+filename_zip,filename_zip)
	print('copy success')

	zipFile = zipfile.ZipFile(os.path.join(os.getcwd(), filename_zip))
	zipFile.extract(date_csv)
	zipFile.close()

	os.remove(filename_zip)
	print('unzip success')
	return date_csv
'''
workdir='/Volumes/DATACOMM/weekly_archive/nuswifi/device_location/'
filelist=os.listdir(workdir)
for i in filelist:
	if i.endswith('CCELIB-CL-06'):
		print(i)

'''

