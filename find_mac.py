from urllib.request import urlopen
import json
from pprint import pprint
from matplotlib import pyplot as plt

Library4='https://api.ami-lab.org/api/v1/cisco/zone/KR-CCELIB/building/CCELIB-Central%20Library/floor/CCELIB-CL-04/devices?token=eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJpYXQiOjE1MTYyNDIwMzIsImF1ZCI6Ik5VUyBEYXRhIEFQSSIsImlzcyI6IkFNSSBMYWIsIE5VUyIsInN1YiI6ImUwMTc4MTgzIiwiZXhwIjoxNTE2MzI4NDMyfQ.XvscyODiBCm6aRxMY3zAnw7TCJqus15UGhMCnpnlbR6U52icJTXiBXH9YjleF6rfGfKc17fAiYWW6QxsUznHlFE3gM4Rto0h8-r9106pDilXs-5vSK7A3898-UEApizvzshiuTMcmgnAPKT4CEnF_Cb-f-Udzpt9B98FLP3P26poItN0qaIuoTx3DfRcF5j-CTJSDptvvZCpi3kLj3_jQugszpTflCoWF5LVsAUxpLExjbF7ckmcOymq7ECircODpeLRCUn3Q0oKz2DWXDPTDf7iZofFlolNN_UoYPRoCMq94--p6xCxoTy3O44q1phVtH7OlWvQWDQ3AuPN9ZOdlg'
Library5='https://api.ami-lab.org/api/v1/cisco/zone/KR-CCELIB/building/CCELIB-Central%20Library/floor/CCELIB-CL-05/devices?token=eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJpYXQiOjE1MTg0OTM3ODgsImF1ZCI6Ik5VUyBEYXRhIEFQSSIsImlzcyI6IkFNSSBMYWIsIE5VUyIsInN1YiI6ImUwMTc4MTgzIiwiZXhwIjoxNTE4NTgwMTg4fQ.L0J4k9117H5pkJ-hvwVKb87tw3nCtpUZ9iNO75s56PLpKdLphNOxYSL5j5Mzj8HFDjMLS0L30fqTS0aL-BrzzlPPEUfNGIeQY2wpvUP2at8TOKnf-ZF1vgzpW3z1IeyQzCNHxFRawuhG06ete8mJCpAcD4YBw-Bh9YGty9jslutgHZBHG5lH3z6ZR2YUVzAfhUzYVMMR-uZmhBDPYpSF-JlK705vttDVUEmkx7tatfY0sE_OUahRfRy5rbDa5oAnoVOw0A8tSvTpH9uWVOXnQcNHPBSCb_qB1A2nBiBnNu4fiLXigwkqG9rDiVer6YGdzWKRrGAdUkngItBDLoLa3Q'
#allurl=[Library4,Library5,I3]
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


u=urlopen(Library5,timeout=10)
resp=json.loads(u.read().decode('utf-8')) #type=list[dict]
time=resp[0]['Statistics']['currentServerTime'][11:-9]
num=len(resp)
pprint(resp)


for i in resp:
	if 'ipAddress' in i:
		if i['ipAddress']==['172.17.61.174']:
			print('------------')
			print(i)
		
# my iphone mac='d33ec540eb6b725326b2e351ee9328aa7c1deecb' 1/18
# 'd33ec540eb6b725326b2e351ee9328aa7c1deecb' 1/19
# 'd33ec540eb6b725326b2e351ee9328aa7c1deecb' 1/22
# 'd33ec540eb6b725326b2e351ee9328aa7c1deecb' 2/5
