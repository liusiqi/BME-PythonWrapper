#Get the contact lists in your account.
from BMEApi import *
import config

client = BMEApi(config.USERNAME,config.PASSWORD,config.APIURL)
if client.isLogin:
	# Login Successful
	emailAddress = "sanketdsawant@gmail.com"
	result = client.listSearchContacts(emailAddress)
	
	if client.isOk:
		print "sequence | id | listname\n"
		for index, item in enumerate(result):
			print result[index]['sequence']," | ",result[index]['id']," | ",result[index]['listname'],"\n"			
	else:
		print "A fault occurred"
		print "Fault code: ", client.faultCode
		print "Fault string: ", client.faultString		
else:
	# an error occurred while logging in
	print "A fault occurred"
	print "Fault code: ", client.faultCode
	print "Fault string: ", client.faultString