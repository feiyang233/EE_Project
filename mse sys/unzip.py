import zipfile,os

zipFile = zipfile.ZipFile(os.path.join(os.getcwd(), '2018_week02.zip'))

print(zipFile.namelist())
'''
for file in zipFile.namelist():
    zipFile.extract(file)
    '''
zipFile.extract('2018-01-09.csv')
zipFile.close()