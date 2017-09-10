import csv
test=open('test.csv','r')
reader=csv.reader(test)
T='2017-09-02T00:00:04'
for row in reader:
	T=row[0][-8:]
	print(T)
test.close()

