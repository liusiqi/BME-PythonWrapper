#This Example shows how to delete an existing Email
from BMEApi import *
import config

client = BMEApi(config.USERNAME,config.PASSWORD,config.APIURL)
if client.isLogin:
	# Login Successful
	result = client.emailGet("", "-1", 1, 5, "", "")
	emailID = result[0]['id']
		
	result = client.emailDelete(emailID)	
		
	if client.isOk:
		print "Email Deleted : ",result
			
	else:
		print "A fault occurred"
		print "Fault code: ", client.faultCode
		print "Fault string: ", client.faultString		
else:
	# an error occurred while logging in
	print "A fault occurred"
	print "Fault code: ", client.faultCode
	print "Fault string: ", client.faultString