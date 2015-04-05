#Get the contacts from the contact list.
from BMEApi import *
import config

client = BMEApi(config.USERNAME,config.PASSWORD,config.APIURL)
if client.isLogin:
	# Login Successful
	result = client.listGet("", 1, 1, "", "")	
	listID = result[0]['id']
	
	filter =""
	pageNumber	 = 1
	pageSize = 10
	orderBy = ""
	sortOrder = ""
	result = client.listGetContacts(listID,filter,pageNumber,pageSize,orderBy,sortOrder)	
		
	if client.isOk:
		print "Sequence | ID | Email\n"
		for index, item in enumerate(result):
			print result[index]['sequence']," | ",result[index]['id']," | ",result[index]['email'],"\n"	
			
	else:
		print "A fault occurred"
		print "Fault code: ", client.faultCode
		print "Fault string: ", client.faultString		
else:
	# an error occurred while logging in
	print "A fault occurred"
	print "Fault code: ", client.faultCode
	print "Fault string: ", client.faultString