import csv
import matplotlib.pyplot as plt

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


filename='TMTech.csv'
rf=open(filename,'r')
reader=csv.reader(rf)
wf=open('rate.csv','w')
writer=csv.writer(wf)
list1=['time','come','leave']

writer.writerow(list1)
liscome=[]
lisleave=[]
temp=next(reader) #begin header
for row in reader:
	come,leave=rate(temp[1:],row[1:])
	temp=row
	list1=[row[0][9:],come,leave]
	writer.writerow(list1)
	#liscome.append(come)
	#lisleave.append(leave)

rf.close()
wf.close()

plt.title('rate')    
plt.xlabel('time')    
plt.ylabel('people')    
x=range(len(liscome))
plt.bar(x,liscome, label='come')    
plt.bar(x,lisleave,label='leave')    
plt.show()

