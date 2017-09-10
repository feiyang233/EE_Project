#encoding:utf-8
#__Author__ = Search__
#_PlugName_ = YouDaoDict

import urllib.request
import urllib.parse
import time
import random
import hashlib
import json

headers = {}
headers['Referer']='http://fanyi.youdao.com/'
headers['User-Agent']='Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.108 Safari/537.36 2345Explorer/8.7.0.16013'

timestamp = int(time.time() * 1000) + random.randint(0,10)

content = input('请输入您需要翻译的内容：')

u = "fanyideskweb"
d = content
f = str(timestamp)
c = "rY0D^0'nM0}g5Mm1z%1G4"

sign = hashlib.md5((u + d + f + c).encode('utf-8')).hexdigest()

data = {
    'i': content,
    'from': 'AUTO',
    'to': 'AUTO',
    'smartresult': 'dict',
    'client': 'fanyideskweb',
    'salt': timestamp,
    'sign': sign,
    'doctype': 'json',
    'version': '2.1',
    'keyfrom': 'fanyi.web',
    'action': 'FY_BY_CLICK',
    'typoResult': 'true'
}

data = urllib.parse.urlencode(data).encode('utf-8')
request = urllib.request.Request(url='http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule&sessionFrom=https://www.google.com/',method='POST',data=data,headers=headers)
response = urllib.request.urlopen(request)
result_str = response.read().decode('utf-8')
result_dict = json.loads(result_str)
print (result_dict["translateResult"][0][0]['tgt'])
