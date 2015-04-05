import xmlrpc.client
class BMEApi(object):	
	def __init__(self,username,password,ApiURL):
                # --------variables----------
		BMEApi.isOk = True	
		BMEApi.isLogin = True	
		BMEApi.server = xmlrpc.client.Server(ApiURL) #calls Server method from xmlrpclib.py file
		# ---------------------------------------

		try:
			BMEApi.isLogin = True
                        #login(): logs into a Benchmark Email account, the token returned will be stored in the MainBME class variable "token"  
                        #       Pre-requisites: Must have a valid Benchmark Email account to log into 
                        #       @param userName: The user name for a Benchmark Email account
                        #       @param password: The password that belongs to the Benchmark Email username
                        #       @Return: the API key associated with the specified Benchmark Email account
			BMEApi.token = BMEApi.server.login(username, password)
			#print "Token : ", token
		except xmlrpclib.Fault as err: #catch up with connection error such as wrong username or password
			BMEApi.isLogin = False
			BMEApi.faultCode = err.faultCode
			BMEApi.faultString = err.faultString				
	
	def getToken(self): 
		return BMEApi.token #the method of getting a token

	# __getattr__ is used to handle the scenario that an attribute is not found. For example:
	# class foo:
	#       a = 0
	#       def __getattr__(self,name):
	#	        return "%s:DEFAULT"%name
	#>>> i.c
        #'c:DEFAULT'
	#
	# 1) Usually, Object.NotFoundMethod(argument) will return an error. If we define __getattr__, it will return whatever is defined in __getattr__
	# 2) In this case, you see inside the __getattr__ function, there is another function calls the getattr(object, name) function.
	# 3) The getattr(object, name) function is like creating a new method object.name which is not originally defined in the class.
	# 4) So object.name is a run-time created method, we could assign it argument(s) or not.
	# 5) Then getattr(object, name)(AnotherObject, entry) is the same as object.name(AnotherObject, entry).
	# 6) The arguments of the new created method include the access token and the entry of whatever the user wants.
	# 7) If the server accepts what the method is doing such as sending new API call or new query, it responses what is asked to send back.
	def __getattr__(self, method_name):
			def get(self, *args, **kwargs):								
				try:
					result  =  getattr(BMEApi.server,method_name,None)(BMEApi.token,*args)
					BMEApi.isOk = True
					return result
				except xmlrpc.client.Fault as err:					
					BMEApi.isOk = False
					BMEApi.faultCode = err.faultCode
					BMEApi.faultString = err.faultString					
					return ""	
			
			return get.__get__(self)	
