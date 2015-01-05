# is the comment symbol just like // in C++ and java

#This Example shows how to create a new contact list and how to Add the contact details to the created contact list.
#Multiple contacts would be added if the details has more than one items.

#Here 'import' is similar to 'using' of C# or 'include' of C++; and almost the same as 'import' of Java.
# The differet is if we use 'import BMEApi', then for every method that will be used, we have to have BMEApi.
# in the front. For example, if there is a method named getToken() in the BMEApi class. When we call it, we must
# type BMEApi.getToken().
#
#However, if we use 'from BMEApi import * ', we don't have to type BMEAPi. in front of every method need will be
# called. From last case, we can call getToken() directly.
#
#Generally, they both have advantages depends on the interests of developers. If you have long class names and want
# to save time, 'from classname import * ' is the better option. But the methods' name should be different. If you
# have methods with the same names in different classes or files, you should use 'import classname' instead to avoid
# confusions both on readers and the machines.

from BMEApi import *

# ----------- Enter you username and password---------------
USERNAME = "Please enter your username"
PASSWORD = "Please enter your password"
# ----------------------------------------------------------
# ----------- Constant ----------------------
APIURL = "http://api.benchmarkemail.com/1.0"
# -------------------------------------------

# personal information: the format of persons is called dictionary in python, which formed by key-value pairs
person1 = {"email":'sanketsawant@gmail.com', "firstname":'Peter', "lastname":'Parker'}
person2 = {"email":'sawant.sanket@yahoo.com', "firstname":'Bruce', "lastname":'Banner'}

# you can add more people, but make sure to follow the format and don't forget to add to list of contacts below.

# Here, a class named client is created as a BMEApi class. The reason we can do this is because 'from BMEApi import* '
client = BMEApi(USERNAME,PASSWORD,APIURL)
# For details, please take a look at the BMEApi.py file

if client.isLogin:
	# Login Successful
	listName = 'List From Python' # set up the new list name
	
	#listCreate(): Create the list in the Benchmark Email account
                #Pre-requisites: Must have a valid Benchmark Email account to log into 
        	# @param listName: The name of the list we are creating. Every list name must have its own unique name (BME does not allow duplicates) 
		# @Return: The list ID of the newly created list
	new_list_ID = client.listCreate(listName)

	#listGet(): Retrieve a list of mailing lists from the Benchmark Email account
		#@param filter: if you want to search for a specific list, type in the name here (filters the results by the string you pass in) 
		#@param pageNumber: the page of results that you want to view (for now we pass 1 to view the first page of results) 
		#@param pageSize: the number of mailing lists per page
		#@param orderBy: we have 3 options, either:
		# 1) name - alphabetical order
		# 2) date - by date created 
		# 3) "" empty (which defaults to by date) 
		# @param sortOrder: sort the results either by 3 options:
		# 1) asc - for ascending order (oldest mailing list first)
		# 2) desc - for descending order (latest created mailing list first)
		# 3) "" - defaults to descending order 
		# @Return: An array of mailing lists from the Benchmark Email account  
	result = client.listGet("", 1, 1, "", "")
	# in this case, it uses the first page's first list as a result
	
	listID = result[0]['id'] # listID is the first list's id

	contacts = [person1, person2] # this line stores persons into a python list

	#listAddContacts(): API method that will add our array of contacts to the specified mailing list 
                #Pre-requisites: Must have at least 1 mailing list in the associated Benchmark Email account to add contacts to
		#@param token: The API token associated to the Benchmark Email account we logged into 
		#@param tempListID: The mailing list ID we retrieved using the getListID() method 
		#@param contacts: Our array of contacts that contain the details of each contact we with to add
		#@Return : An integer notifying us how many contacts were successfully added 
	contact_number = client.listAddContacts(listID,contacts)
	
	if client.isOk: #isOk is a boolean variable of BMEApi class
		print new_list_ID # prints out list ID
		print "Total Contacts: ", contact_number # prints out number of contacts added to the list

	else: # an error occurred while at connection
		print "A fault occurred"
		print "Fault code: ", client.faultCode
		print "Fault string: ", client.faultString		
else:
	# an error occurred while logging in
	print "A fault occurred"
	print "Fault code: ", client.faultCode
	print "Fault string: ", client.faultString
