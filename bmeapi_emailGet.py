#This Example shows how to get the list of existing Emails
from BMEApi import *
import config

client = BMEApi(config.USERNAME,config.PASSWORD,config.APIURL)
if client.isLogin:
	# Login Successful
	
	result = client.emailGet("", "-1", 1, 50, "", "")
	
	if client.isOk:
		print "Email ID | Name | From Name | Subject | List ID | List Name | Status | Created Date | Modified Date\n"
		for index, item in enumerate(result):
			print result[index]['id']," | ",result[index]['emailName'].encode('utf-8')," | ",result[index]['fromName'].encode('utf-8')," | ",result[index]['subject'].encode('utf-8')," | ",result[index]['toListID']," | ",result[index]['toListName'].encode('utf-8')," | ",result[index]['status']," | ",result[index]['createdDate']," | ",result[index]['modifiedDate'],"\n"			
	else:
		print "A fault occurred"
		print "Fault code: ", client.faultCode
		print "Fault string: ", client.faultString		
else:
	# an error occurred while logging in
	print "A fault occurred"
	print "Fault code: ", client.faultCode
	print "Fault string: ", client.faultString