from urllib import request
import json
from pprint import pprint
from matplotlib import pyplot as plt
import time
from urllib.error import HTTPError

library4='https://api.ami-lab.org/api/v1/cisco/zone/KR-CCELIB/building/CCELIB-Central%20Library/floor/CCELIB-CL-04/devices?token=eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJpYXQiOjE1MTY2MDg1NTYsImF1ZCI6Ik5VUyBEYXRhIEFQSSIsImlzcyI6IkFNSSBMYWIsIE5VUyIsInN1YiI6ImUwMTc4MTgzIiwiZXhwIjoxNTE2Njk0OTU2fQ.AKMAc7FbdIzuxjM1NTAfCHh4GLl1lWQjbJ1xRb_2PEKP0oJIEYAT3PIo5jvUHtu-fqP7kDzZQvm56cQLrKeLY13ZNAlqgU41zPiHu5J104Po2Ll8vsWltEI7dc--Z_HFBzBqdPV-Y9fp2YVtTVBRB2Qj2lTWayOv3auuz_oIq6Z7lxhFuqlkC34Kx-xPXwlK1ZDCdjCYY7C8tp1GL48bqN6goYxpSwJ-mg7onIyw6anj4iySO0ffZQwjZclPCo57JilXrsESs3jxvfgttMkA8ofjBn_ehhDujTdQxhzOUQOAFsMEus6KLMkIcBnToGPLEK2o6mHY1dBjdoY1VizCGQ'
headers={
	'Referer':'https://datacommons.nus.edu.sg/DataStage',
	'Connection':'keep-alive',
	'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'
}

def online(url):
	req=request.Request(url,headers=headers)
	try:
		u=request.urlopen(req)
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

while(x<20):
	a,b=online(library4)
	plt.bar(x,b,width = 0.5)
	plt.text(x, b+1, str(b), ha='center')
	x+=1
	plt.pause(0.1)
	time.sleep(1)
plt.title(a)
plt.savefig('flow.png')
plt.close()






