#This Example shows how to create a new Email
from BMEApi import *
import config

client = BMEApi(config.USERNAME,config.PASSWORD,config.APIURL)
if client.isLogin:
	# Login Successful
	result = client.listGet("", 1, 1, "", "")
	listID = result[0]['id']
	
	emailDetails = {
		'fromName': 'Steve',
		'fromEmail': 'useremail_@_.com',
		'emailName': 'Email From Python',
		'replyEmail': 'useremail_@_.com',
		'subject': 'Email From Python',
		'templateContent': '<html><body> <b> Hello World From Python</b> </body></html>',
		'webpageversion': 'true',
		'toListID': int(listID)
    }
	
	result = client.emailCreate(emailDetails)	
		
	if client.isOk:
		print "New Email ID: ",result
			
	else:
		print "A fault occurred"
		print "Fault code: ", client.faultCode
		print "Fault string: ", client.faultString		
else:
	# an error occurred while logging in
	print "A fault occurred"
	print "Fault code: ", client.faultCode
	print "Fault string: ", client.faultString