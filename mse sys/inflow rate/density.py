import csv
import generate_time
from matplotlib import pyplot as plt

time=generate_time.getime(20180117)

#统计一天24小时，每个小时有多少访问量。
def repeat(L):   #列表去重，不改变原来的顺序
	L2=list(set(L))
	L2.sort(key=L.index)
	return L2

filename='TMdeck.csv'
rf=open(filename,'r')
reader=csv.reader(rf)

total=[]
lis=[]
count=0
for row in reader:
	for i in row[2:]:
		total.append(i)
	count+=1
	if count==12:
		total=repeat(total)
		lis.append(len(total))
		total.clear()
		count=0
	if row[0]=='20180117-07:55:01':
		break

for row in reader:
	for i in row[2:]:
		total.append(i)
	
	count+=1
	if count==60:
		total=repeat(total)
		lis.append(len(total))
		total.clear()
		count=0	

print(lis)
rf.close()
with open('density.text','w') as f:
	f.writelines(lis)
'''
x=range(24)
plt.figure("density")
plt.bar(x,lis,width =0.5)


for i in x:
	plt.text(i, lis[i]+1,str(lis[i]), ha='center')
plt.title('deck')
plt.savefig('density.png',dpi=200)
plt.show()
'''




