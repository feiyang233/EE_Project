from urllib.request import urlopen
import json
from pprint import pprint
from matplotlib import pyplot as plt

Library4='https://api.ami-lab.org/api/v1/cisco/zone/KR-CCELIB/building/CCELIB-Central%20Library/floor/CCELIB-CL-04/devices?token=eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJpYXQiOjE1MTYyNDIwMzIsImF1ZCI6Ik5VUyBEYXRhIEFQSSIsImlzcyI6IkFNSSBMYWIsIE5VUyIsInN1YiI6ImUwMTc4MTgzIiwiZXhwIjoxNTE2MzI4NDMyfQ.XvscyODiBCm6aRxMY3zAnw7TCJqus15UGhMCnpnlbR6U52icJTXiBXH9YjleF6rfGfKc17fAiYWW6QxsUznHlFE3gM4Rto0h8-r9106pDilXs-5vSK7A3898-UEApizvzshiuTMcmgnAPKT4CEnF_Cb-f-Udzpt9B98FLP3P26poItN0qaIuoTx3DfRcF5j-CTJSDptvvZCpi3kLj3_jQugszpTflCoWF5LVsAUxpLExjbF7ckmcOymq7ECircODpeLRCUn3Q0oKz2DWXDPTDf7iZofFlolNN_UoYPRoCMq94--p6xCxoTy3O44q1phVtH7OlWvQWDQ3AuPN9ZOdlg'
Library5='https://api.ami-lab.org/api/v1/cisco/zone/KR-CCELIB/building/CCELIB-Central%20Library/floor/CCELIB-CL-05/devices?token=eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJpYXQiOjE1MTYyMzg4MzYsImF1ZCI6Ik5VUyBEYXRhIEFQSSIsImlzcyI6IkFNSSBMYWIsIE5VUyIsInN1YiI6ImUwMTc4MTgzIiwiZXhwIjoxNTE2MzI1MjM2fQ.ruX9KugMknYtyLui5tPHeKPTF4rsHwz4xhbOj6Npeqhn3GqwWb9j1qXtzywJbaTT5owFGpilh6AWMyv2DgACXk9KT40B1yOzW_zzxp34zYlZbjhyBP_pGFTD4qrikBMalcnD4khC64ZD3Zb-HYrKbr5asT2o0j2ncYZ-e849rWF9Og45N3VhcsaUV0KFULXJi8-pN1zFgZe-zJMzTNBOH9mgvLzVmx7lFS3jVTPRtPHiRe_feJr9OLtPQfHNikkZt_3bjPunF1CxyGZ5DayFDVOi4mca0HJuvHoLhiXQGMc_e0TiRZJ70okP42nR94SZlIcIfp4NZnCRx7xKn_094w'
I3='https://api.ami-lab.org/api/v1/cisco/zone/KR-FBALAW/building/FBALAW-I3/floor/FBALAW-I3-02/devices?token=eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJpYXQiOjE1MTYyNDIwMzIsImF1ZCI6Ik5VUyBEYXRhIEFQSSIsImlzcyI6IkFNSSBMYWIsIE5VUyIsInN1YiI6ImUwMTc4MTgzIiwiZXhwIjoxNTE2MzI4NDMyfQ.XvscyODiBCm6aRxMY3zAnw7TCJqus15UGhMCnpnlbR6U52icJTXiBXH9YjleF6rfGfKc17fAiYWW6QxsUznHlFE3gM4Rto0h8-r9106pDilXs-5vSK7A3898-UEApizvzshiuTMcmgnAPKT4CEnF_Cb-f-Udzpt9B98FLP3P26poItN0qaIuoTx3DfRcF5j-CTJSDptvvZCpi3kLj3_jQugszpTflCoWF5LVsAUxpLExjbF7ckmcOymq7ECircODpeLRCUn3Q0oKz2DWXDPTDf7iZofFlolNN_UoYPRoCMq94--p6xCxoTy3O44q1phVtH7OlWvQWDQ3AuPN9ZOdlg'
allurl=[Library4,Library5,I3]
'''
def online(url):
	u=urlopen(url)
	resp=json.loads(u.read().decode('utf-8'))
	time=resp[0]['Statistics']['currentServerTime'][11:-9]
	num=len(resp)
	return time,num
num=[]

for i in allurl:
	a,b=online(i)
	num.append(b)
x=range(len(allurl))
y=num
plt.bar(x,y)
lable=['L4','L5','I3']
i=0
for xx, yy in zip(x,y):
	plt.text(xx, yy+1, str(yy), ha='center')
	plt.text(xx, -30,lable[i],ha='center',color='green')
	i+=1
plt.show()
'''


u=urlopen(Library5,timeout=5)
resp=json.loads(u.read().decode('utf-8')) #type=list[dict]
time=resp[0]['Statistics']['currentServerTime'][11:-9]
num=len(resp)



for i in resp:
	if 'ipAddress' in i:
		if i['ipAddress']==['172.17.60.181']:
			print(i)
		
# my iphone mac='d33ec540eb6b725326b2e351ee9328aa7c1deecb'

