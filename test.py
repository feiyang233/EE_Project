from numpy import *  
import matplotlib  
import matplotlib.pyplot as plt  
import csv
#border=[103.770745	1.29908;103.770745	1.298114;103.771467	1.29812;103.771467	1.299074];  
f=open('test.csv','r')
martix=[]
n=0
reader = csv.reader(f)
for row in reader:
	if n%50==0:
		x=row[2::2]
		y=row[3::2]
		x_1=[1.298963,1.298285]
		y_1=[103.770916,103.771237]
		x_2=[1.298285,1.298361]
		y_2=[103.771237,103.771388]
		x_3=[1.298361,1.299036]
		y_3=[103.771388,103.771069]
		x_4=[1.299036,1.298963]
		y_4=[103.771069,103.770916]
		plt.figure(str(n))
		plt.plot(x_1, y_1, marker='^')
		plt.plot(x_2, y_2, marker='^')
		plt.plot(x_3, y_3, marker='^')
		plt.plot(x_4, y_4, marker='^') 
		plt.scatter(x,y) 
		plt.savefig(str(n)+'test.png')
		
	n=n+1
	x=[]
	y=[]
print(n)




