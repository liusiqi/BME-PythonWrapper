#This Example shows how to schedule an existing Email
from BMEApi import *
from datetime import date
import config

client = BMEApi(config.USERNAME,config.PASSWORD,config.APIURL)
if client.isLogin:
	# Login Successful
	result = client.emailGet("", "-1", 1, 5, "", "")
	emailID = result[0]['id']
	d  = date.today()	
		
	result = client.emailSchedule(emailID,d.strftime("%d %b %Y %H:%M:%S"))	
		
	if client.isOk:
		print "Email Sent : ",result
			
	else:
		print "A fault occurred"
		print "Fault code: ", client.faultCode
		print "Fault string: ", client.faultString		
else:
	# an error occurred while logging in
	print "A fault occurred"
	print "Fault code: ", client.faultCode
	print "Fault string: ", client.faultString