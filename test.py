from numpy import *  
import matplotlib  
import matplotlib.pyplot as plt  
import csv
  
f=open('test.csv','r')
reader = csv.reader(f)
for row in reader:
	x=row[2::2]
	y=row[3::2]
	break
f1 = plt.figure(1)  
 
plt.scatter(x,y) 

plt.show()

