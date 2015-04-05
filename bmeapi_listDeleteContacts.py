#Unsubscribe the contacts from the given contact list.
from BMEApi import *
import config

client = BMEApi(config.USERNAME,config.PASSWORD,config.APIURL)
if client.isLogin:
	# Login Successful
	result = client.listGet("", 1, 1, "", "")
	listID = result[0]['id']
	
	result = client.listGetContacts(listID,"", 1, 100, "", "")	
		
	if client.isOk:
		contacts = ""
		for index, item in enumerate(result):
			contacts = contacts + result[index]['id'] + ","		
		contacts = contacts.rstrip(",")
		if contacts != "":
			retval = client.listDeleteContacts(listID,contacts);
			print retval," Contacts Deleted"	
		else:
			print "Contacts Not Found"	
			
	else:
		print "A fault occurred"
		print "Fault code: ", client.faultCode
		print "Fault string: ", client.faultString		
else:
	# an error occurred while logging in
	print "A fault occurred"
	print "Fault code: ", client.faultCode
	print "Fault string: ", client.faultString