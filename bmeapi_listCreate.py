#Create a new contact list.
from BMEApi import *
import config

client = BMEApi(config.USERNAME,config.PASSWORD,config.APIURL)
if client.isLogin:
	# Login Successful
	listName = 'List From Python'
	result = client.listCreate(listName)
	if client.isOk:
		print result
	else:
		print "A fault occurred"
		print "Fault code: ", client.faultCode
		print "Fault string: ", client.faultString		
else:
	# an error occurred while logging in
	print "A fault occurred"
	print "Fault code: ", client.faultCode
	print "Fault string: ", client.faultString