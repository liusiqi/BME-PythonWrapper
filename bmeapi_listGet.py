#Get the contact lists in your account.
from BMEApi import *
import config

client = BMEApi(config.USERNAME,config.PASSWORD,config.APIURL)
if client.isLogin:
	# Login Successful
	
	result = client.listGet("", 1, 10, "", "")
	
	if client.isOk:
		print "sequence | listname | tid | tcontactcount | tcreatedDate | tmodifiedDate\n"
		for index, item in enumerate(result):
			print result[index]['sequence']," | ",result[index]['listname']," | ",result[index]['id']," | ",result[index]['contactcount']," | ",result[index]['createdDate']," | ",result[index]['modifiedDate'],"\n"			
	else:
		print "A fault occurred"
		print "Fault code: ", client.faultCode
		print "Fault string: ", client.faultString		
else:
	# an error occurred while logging in
	print "A fault occurred"
	print "Fault code: ", client.faultCode
	print "Fault string: ", client.faultString