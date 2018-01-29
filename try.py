'''
import numpy as np
import matplotlib.pyplot as plt
plt.axis([0, 100, 0, 1])
plt.ion()
for i in range(100):
    y = np.random.random()
    plt.bar(i, y)
    plt.pause(0.1)
'''
	
from urllib.request import urlopen
import json
from pprint import pprint
from matplotlib import pyplot as plt
import time
from urllib.error import HTTPError

library4='https://api.ami-lab.org/api/v1/cisco/zone/KR-AKIENG/building/AKIENG-ENGINE%20CANTEEN/floor/AKIENG-ENGINE%20CANTEEN/devices?token=eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJpYXQiOjE1MTY2MTAwODUsImF1ZCI6Ik5VUyBEYXRhIEFQSSIsImlzcyI6IkFNSSBMYWIsIE5VUyIsInN1YiI6ImUwMTc4MTgzIiwiZXhwIjoxNTE2Njk2NDg1fQ.UDlYNTZMjMV2eZ1BuCn3YzEXAbALrW1wY6HKzTBpEIBwNNs_QZPERGB8bKe6-oY4jWgjBSqgPLTfCVDKb2clKbEPtLAoYgojlQX0Z6EzoAyI7OlkK6QdtS8cjZqEVWOo1EuEcE9xio9jHHdvH3Sg1tNzgDRuu8QHcPqqDfR-roZg2gkh8vR0KPtNJWrJ0ebFoQrDKr5Wq8hDmOQqgiPsKIrWcWp4CBJTJ9ALq7tCPSgT3tdwj6eiDjF2oIsEuIyJSWDD2twX0PLYMx1QXdpFCB0ByBhrEBg1UXR_WeeJvMs3dwtzxt8mPJJ47l5hCSRmK-PvH6u2PJRQQcUhusLFTg'
def online(url):
	try:
		u=urlopen(url,timeout=10)
		resp=json.loads(u.read().decode('utf-8'))
		time=resp[0]['Statistics']['currentServerTime'][11:-9]
		num=len(resp)
		return time,num
	except HTTPError as e:
		print('error')
	return (0,0)

plt.figure("floor")
plt.ion()
x=0
while(x<10):
	a,b=online(library4)
	plt.bar(x,b,width = 0.5)
	plt.text(x, b+1, str(b), ha='center')
	x+=1
	plt.pause(0.1)
	time.sleep(1)
plt.title(a)
#plt.savefig('flow.png')
plt.close()