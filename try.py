
from urllib.request import urlopen
import json
from matplotlib import pyplot as plt
import time
from urllib.error import HTTPError


library4='https://api.ami-lab.org/api/v1/cisco/zone/KR-AKIENG/building/AKIENG-ENGINE%20CANTEEN/floor/AKIENG-ENGINE%20CANTEEN/devices?token=eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJpYXQiOjE1MTY2MTAwODUsImF1ZCI6Ik5VUyBEYXRhIEFQSSIsImlzcyI6IkFNSSBMYWIsIE5VUyIsInN1YiI6ImUwMTc4MTgzIiwiZXhwIjoxNTE2Njk2NDg1fQ.UDlYNTZMjMV2eZ1BuCn3YzEXAbALrW1wY6HKzTBpEIBwNNs_QZPERGB8bKe6-oY4jWgjBSqgPLTfCVDKb2clKbEPtLAoYgojlQX0Z6EzoAyI7OlkK6QdtS8cjZqEVWOo1EuEcE9xio9jHHdvH3Sg1tNzgDRuu8QHcPqqDfR-roZg2gkh8vR0KPtNJWrJ0ebFoQrDKr5Wq8hDmOQqgiPsKIrWcWp4CBJTJ9ALq7tCPSgT3tdwj6eiDjF2oIsEuIyJSWDD2twX0PLYMx1QXdpFCB0ByBhrEBg1UXR_WeeJvMs3dwtzxt8mPJJ47l5hCSRmK-PvH6u2PJRQQcUhusLFTg'
library5='https://api.ami-lab.org/api/v1/cisco/zone/KR-CCELIB/building/CCELIB-Central%20Library/floor/CCELIB-CL-05/devices?token=eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJpYXQiOjE1MTgwNTE2MzMsImF1ZCI6Ik5VUyBEYXRhIEFQSSIsImlzcyI6IkFNSSBMYWIsIE5VUyIsInN1YiI6ImUwMTc4MTgzIiwiZXhwIjoxNTE4MTM4MDMzfQ.jTSMzxwvp0BjTuHRpph2O-WQ-hsSnCMp8vHf6nFVkv8zxorYiZ3YSaCRF25gM0VHwRFZp_BjeLni3bWRCB0k_OrmpfN0Qq2gBtE91LPbE2FSy10nA7ORn2JvZxXjT5xczeB9-4mrrfxK6CXk7s0nm8L_28Ti_-KHOmDGfu6B3eavPQu2C1D13sjaW3HenII5O7wmDZhrkzRqwEOx8rGl5vPJRgbtU7CsuWRd5EwpVpdh8lIEutXAHQBXc_mPssnzQL42hkiDwgu7jzMHucgua1nnD0JD3OvblwdXCeBQshcM0CnXuZr22FSAKhxhIB4o41lJWKZdixIQHBreJO8XEQ'
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
'''
plt.figure("floor")
plt.ion()
x=0
while(x<10):
	a,b=online(library5)
	plt.bar(x,b,width = 0.5)
	plt.text(x, b+1, str(b), ha='center')
	x+=1
	plt.pause(0.1)
	time.sleep(1)
plt.title(a)
#plt.savefig('flow.png')
plt.close()

'''