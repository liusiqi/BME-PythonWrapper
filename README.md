BME-PythonWrapper
=================
##Description

Welcome python developers! If you're looking to use or learn how to use Benchmark Email's python wrapper to integrate with our API then you've come to the right place. The purpose of these files is to help you hit the ground running and start developing using our API quickly and effectively. This project will showcase how to:
- Create a new mailing list
- Prepare an array of contacts to add into a mailing list
So whether you're new to python or an experienced software dev, let our example project give you a running start on integrating with Benchmark Email. Good luck!

##Prerequisites
In order to be able to run this example project you must have the following:
- Python 2.7.9 (Attention: don’t download python 3.0.0 or above)  https://www.python.org/downloads/release/python-279/
- Choose the right version of Python 2.7.9 for your machine, download it, and install it.
- No money, our free and paid plans allow you to use our API at no cost. So follow the link and sign up for a free account to receive your API token: https://ui.benchmarkemail.com/Register
- 
##Open a python file

After downloading and installing python, you will see an ![Python Icon]()  icon on the start menu (or on your desktop). It is called IDLE(Python GUI):
- To open a new python file:
 1) Click on IDLE(Python GUI), it will pop up a window called Python 2.7.9 Shell ![python shell]()
 2) Choose File → New File to create a new python. Then at the new pop up window, 
    choose File → Save to save it at wherever you want and whatever name you want.And now you can start coding on it. In this example, let’s save it as “Hello World!” 
![python window]()
 
3) Now type “ print “Hello World!” “ inside the python window ![print()
 
4) Click “Run” on the menu bar and select “Run module” or press F5 on the keyboard. The result will be shown on the shell related the python window. ![print out]()
 
##Configuring the Project for Python

In order to run this project, please follow these steps: 
- Download the repository
○ Go to https://github.com/Benchmark-Email/bmepythonwrapper
○ Click on the "Download ZIP" button located on the right hand side
- Once the download is finished, extract the zip file (possibly to your desktop for easy access) ![wrapper folder]()  
- There are three python files inside the unzipped folder: CreateList&AddContacts.py, BMEApi.py, and xmlrpclib.py. ![three files]() 

Their relationships are:
 
- The xmlrpclib.py contains all basic setups for the other two files. Try not to change anything in it.
- The BMEApi.py file calls methods from the xmlrpclib.py file. Its purpose is to establish a connection to the given URI based on the given username and password. Try not to change anything if and only if there is a necessary.
- The xmlrpclib.py file creates a client by using the BEMApi class. The client can then do many thing by using different methods from the benchmark Email API Documentation. In this assignment, the project calls the listCreate method to create a new list, then calls listAddContacts method to add contacts into the created new list.
- 
##Running the Project

 Right click on the CreateList&AddContacts.py file and select “Edit with IDLE”. When the window appears, press F5 or click “Run” → “Run module” ![run]()
 
The result of prints will show on a python shell popping up. ![result]()
 
Now, you can login to your Benchmark account to see if a new list with two new contacts are add to your list menu.

##Contact Info

- Visit our API page to view our other wrappers and documentation:
- http://www.benchmarkemail.com/API/Library

##Licensing

Copyright (c) 2014 BenchmarkEmail, released under the MIT license
Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
