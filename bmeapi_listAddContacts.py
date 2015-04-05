#This Example shows how to Add the contact details to the given contact list.
#Multiple contacts would be added if the details has more than one items.
from BMEApi import *
import config

client = BMEApi(config.USERNAME,config.PASSWORD,config.APIURL)
if client.isLogin:
	# Login Successful
	
	result = client.listGet("", 1, 1, "", "")
	listID = result[0]['id']
	contacts = [ {"email":'sanketsawant@gmail.com', "firstname":'Peter', "lastname":'Parker'},{"email":'sawant.sanket@yahoo.com', "firstname":'Bruce', "lastname":'Banner'}	]
	result = client.listAddContacts(listID,contacts)
	if client.isOk:
		print "Total Contacts: ", result
	else:
		print "A fault occurred"
		print "Fault code: ", client.faultCode
		print "Fault string: ", client.faultString		
else:
	# an error occurred while logging in
	print "A fault occurred"
	print "Fault code: ", client.faultCode
	print "Fault string: ", client.faultString