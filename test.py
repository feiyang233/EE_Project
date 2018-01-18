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

library4='https://api.ami-lab.org/api/v1/cisco/zone/KR-CCELIB/building/CCELIB-Central%20Library/floor/CCELIB-CL-04/devices?token=eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJpYXQiOjE1MTYyNDIwMzIsImF1ZCI6Ik5VUyBEYXRhIEFQSSIsImlzcyI6IkFNSSBMYWIsIE5VUyIsInN1YiI6ImUwMTc4MTgzIiwiZXhwIjoxNTE2MzI4NDMyfQ.XvscyODiBCm6aRxMY3zAnw7TCJqus15UGhMCnpnlbR6U52icJTXiBXH9YjleF6rfGfKc17fAiYWW6QxsUznHlFE3gM4Rto0h8-r9106pDilXs-5vSK7A3898-UEApizvzshiuTMcmgnAPKT4CEnF_Cb-f-Udzpt9B98FLP3P26poItN0qaIuoTx3DfRcF5j-CTJSDptvvZCpi3kLj3_jQugszpTflCoWF5LVsAUxpLExjbF7ckmcOymq7ECircODpeLRCUn3Q0oKz2DWXDPTDf7iZofFlolNN_UoYPRoCMq94--p6xCxoTy3O44q1phVtH7OlWvQWDQ3AuPN9ZOdlg'

def online(url):
	u=urlopen(url,timeout=10)
	resp=json.loads(u.read().decode('utf-8'))
	time=resp[0]['Statistics']['currentServerTime'][11:-9]
	num=len(resp)
	return time,num

plt.ion()
x=0
while(x<10):
	a,b=online(library4)
	plt.bar(x,b,width = 0.5)
	plt.text(x, b+1, str(b), ha='center')
	x+=1
	plt.pause(0.1)
	time.sleep(5)







