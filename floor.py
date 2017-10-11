from PIL import Image
import matplotlib  
import matplotlib.pyplot as plt  
import csv
import numpy

border=[[103.770745,1.29908],[103.770745,1.298114],[103.771467,1.29812],[103.771467,1.299074]] 
f=open('test.csv','r')
img=Image.open('floor.jpg')

bias1=border[1][1]-border[0][1]
bias2=border[3][0]-border[0][0]
#print(bias1,bias2)
snap1=bias2/595 
snap2=bias1/487 
n=0
#print(img.size)
plt.figure("floor")
plt.imshow(img)
reader = csv.reader(f)
for row in reader:
	y=(row[2::2])
	x=(row[3::2])
	ary=numpy.array(y,dtype='float64')
	arx=numpy.array(x,dtype='float64')
	ary=ary-1.29908
	arx=arx-103.77095
	seq1=arx/snap1
	seq2=ary/snap2
	print(seq1)
	print(seq2)
	plt.scatter(seq1,seq2,marker='^') 
	plt.savefig(str(row[0][5::])+'.png')
	plt.close()
	break
f.close()




