<<<<<<< HEAD
import xmlrpclib
class BMEApi(object):	
	def __init__(self,username,password,ApiURL):
		BMEApi.isOk = True	
		BMEApi.isLogin = True	
		BMEApi.server = xmlrpclib.Server(ApiURL)

		try:
			BMEApi.isLogin = True
			BMEApi.token = BMEApi.server.login(username, password)
			#print "Token : ", token
		except xmlrpclib.Fault, err:
=======
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
>>>>>>> bb5e805c12105763743c0a475cd771394f3624aa
			BMEApi.isLogin = False
			BMEApi.faultCode = err.faultCode
			BMEApi.faultString = err.faultString				
	
<<<<<<< HEAD
	def getToken(self):
		return BMEApi.token
	
=======
	def getToken(self): 
		return BMEApi.token #the method of getting a token

	# This method is a little to understand, if you can't get it, it is totally fine.
	# The purpose of this method is when the token is created, it is set as one of the attributes of the server.
	# So that developers don't have to assign the token into a variable and use it at every method that needs the token. This method
	# already set the token as a attribute of the server. It is used under cover which is more safty. 
>>>>>>> bb5e805c12105763743c0a475cd771394f3624aa
	def __getattr__(self, method_name):
			def get(self, *args, **kwargs):								
				try:
					result  =  getattr(BMEApi.server,method_name,None)(BMEApi.token,*args)
					BMEApi.isOk = True
					return result
<<<<<<< HEAD
				except xmlrpclib.Fault, err:					
=======
				except xmlrpc.client.Fault as err:					
>>>>>>> bb5e805c12105763743c0a475cd771394f3624aa
					BMEApi.isOk = False
					BMEApi.faultCode = err.faultCode
					BMEApi.faultString = err.faultString					
					return ""	
			
<<<<<<< HEAD
			return get.__get__(self)	
=======
			return get.__get__(self)	
>>>>>>> bb5e805c12105763743c0a475cd771394f3624aa
