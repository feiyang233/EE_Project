import csv
from collections import Counter

rf=open('OverallTech.csv','r')
reader=csv.reader(rf)
wf=open('text.csv','w')
writer=csv.writer(wf)

h=next(reader)
length=0
sumtime=0
for row in reader:
	row1=[n for n in row[85:] if n!='']
	word_counts = Counter(row1)
	top_three = word_counts.most_common(3)
	temp=top_three.copy()
	for i in temp:
		if i[1]<3 or i[1]>60:
			top_three.remove(i)
	for j in top_three:
		length+=1
		sumtime+=j[1]
	top_three.insert(0,row[0])
	writer.writerow(top_three)
	

print(sumtime/length)
rf.close()
wf.close()

#h[85]='20180117-07:00:01'

