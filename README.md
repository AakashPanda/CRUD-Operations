# CRUD-Operations
CRUD (create, read, update and delete) created in python with Django framework developed by Aakash Panda

CRUD operations:

CRUD operations are widely used in many applications that are supported by underlying relational databases. 
These four basic CRUD functions are incredibly versatile in how they can support a variety of important functions
across different business models and industry verticals. Let's look at an example of how CRUD is implemented.

This project is Converted in .exe file:
follow the steps:
process is given below:
------------------------------------------------------------------------------------------------------------
step 1

first install pyinstaller by using this commend :
-> pip install pyinstaller 

step 2 

There are two way to convert django project to exe file:
1) pyinstaller --onefile -w manage.py

2) pyinstaller project_name
-> eg : pyinstaller manage.py       -> like this

  {

	It wil create 2 folders and 1 file of spec for you:
	-> build
	-> dist
	-> file.spec

	after creating this type second commend 
	-> pyinstaller manage.spec 

	then Go in dist folder -> in this folder you see 2 things
	-> manage folder
	-> manage.exe

	go in manage folder :
	-> then open cmd 

	in cmd write this commends 

	-> manage.exe runserver --noreload

  }
----------------------------------------------------------------------------------------------------------------------

Or you can take text file:

[converting_to_exe_file.txt](https://github.com/AakashPanda/CRUD-Operations/files/9138395/converting_to_exe_file.txt)

-----------------------------------------------------------------------------------------------------------------------

Lets see the outputs of crud operation:

![image](https://user-images.githubusercontent.com/72156701/179689150-00d2b21b-5792-4e20-8617-a96578eb0915.png)

Here we are adding some details in our table let see : create -

![image](https://user-images.githubusercontent.com/72156701/179690237-49519d34-134d-42ab-9cbf-58555f124412.png)

![image](https://user-images.githubusercontent.com/72156701/179690726-54704418-037c-4145-b148-dc689767e2a5.png)

Now, Update it..

![image](https://user-images.githubusercontent.com/72156701/179691060-f76d644c-5605-4951-a763-490fa2707ee8.png)

![image](https://user-images.githubusercontent.com/72156701/179691289-43ac294f-1a66-4e06-9bde-5ff3258a9568.png)

![image](https://user-images.githubusercontent.com/72156701/179691396-4a0a254e-225b-4098-84c2-61bd1ad8ba9a.png)

Now, Delete it...

![image](https://user-images.githubusercontent.com/72156701/179691847-73bc0ce6-3351-4762-8099-22e4ca4817a9.png)

![image](https://user-images.githubusercontent.com/72156701/179692412-329089ad-ad1a-45a8-81bf-a1158b7fdf5c.png)

![image](https://user-images.githubusercontent.com/72156701/179692563-77147ee1-8646-4768-b184-0d8e83fad3f3.png)


thanks for reading it...











