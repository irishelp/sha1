# -*- coding: utf-8 -*-
# version python 3.5

import hashlib
import json
import sys

def	requestsign( message,signKey):
#    print (message)
	message1=json.dumps(message,sort_keys=True)
	
	message2 = json.loads(message1)

	requestkey=[]
	
	for key in message2:
		requestkey.append(key)
	
#	对请求报文参数进行排序
	requestkey.sort()	  

#	组签名字符串stringSignTemp
	stringSignTemp=''
	for lenth in requestkey:
		if lenth!='sign':
#			print (type(lenth))
#			print (type(message2[lenth]))
			stringSignTemp += lenth + '=' + message2[lenth] + '&'
#			print (stringSignTemp)
		else:
			print ("跳过sign参数拼接")

#	去掉尾部的&符号
	stringSignTemp1 = stringSignTemp[:-1]

#   拼接签名密钥
	stringSignTemp1 += signKey
#	print (stringSignTemp1)

	sha1 = hashlib.sha1()
	sha1.update(stringSignTemp1.encode('utf-8'))
	signvalue = sha1.hexdigest()
	print ("签名1加密结果：", signvalue )
	
	if message2['sign']==signvalue:
		print ('签名验证通过：pass')
		return (json.dumps(message2))
	else:
		print ('签名验证失败：fail')
		message2['sign']=signvalue
		print ('更新签名字段为最新的值:')
		print (message2['sign'])
		return (json.dumps(message2))

		
if __name__ == '__main__':
	
	signKey='zsdfyreuoyamdphhaweyrjbvzkgfdycs'
	message= {
	"txndir":"Q",
	"busicd":"VOID",
	"inscd":"10134001",
	"mchntid":"402077158140001",
	"txamt":"000000000495",
	"orderNum":"201710250018",
	"origOrderNum":"201710250008",
	"sign":"4b44f647367082d0d6d8e46a8ae929788fd6b5d8"
	}
	requestsign(message,signKey)
#	if len(sys.argv)==3:
#		print (sys.argv[1])
#		print (sys.argv[2])
#		requestsign(sys.argv[1],sys.argv[2])
#	else:
#		print ('参数不对')
	
	
	