# STS WEB APPLICATION :computer:
###### *Developed by - Sneha Sabu - Student ID: 51987943, Ruilin Wang - Student ID: 51986323, Barkavi Sundararajan - Student ID: 51989442, Bowen Zhang - Student ID: 51987570*
### About the application:
STS Application is a Python based application developed on the Django framework. It is a database-driven application for Fendercare Ship-to-Ship process which provides a platform to access the operational status of services being provided, and to manage information and logistics of the operations.


## Deployed application
The live application has been deployed on Microsoft Azure and can be accessed through the following link:  
https://sts-app.azurewebsites.net/

* You can use these account details to log in to the STS Application as an Admin user:   
Username - admin  
Password - stsjf2020 

## System Requirements 
#### This application has the following system dependencies:
* Python version  - '3.6'
* Django version  - '2.2.9'
* MongoDB version - '4.0.19'
* Djongo version  - '1.2.36'

____

# MAINTENANCE MANUAL
## Configuration and running the application
Listed below are the requirements to configure the application: (All commands are as per how they are to be written in the terminal. If requested to add something to a folder it will be specificly written):
The STS Web Application has been implemented on the Python based Django Framework using a NoSQL Mongo Database. 

### Installing and running the Application on a Local machine:
1. Download the STS application code from the Github link or take a clone of the repository on a local machine using the following git command:  
git clone https://github.com/UoA-CS5942/team_charlie_2020.git
2. After taking a clone of the code, download the executable installer of Python version 3.6 from the following link:  
https://www.python.org/downloads/release/python-360/
3. Run the executable file to install Python on your machine.
4. After the installation has successfully been completed, open your command prompt and **cd** into the folder where the STS code has been downloaded as shown in the following screenshot:
![Image1](https://github.com/UoA-CS5942/team_charlie_2020/blob/master/static/images/deployment.jpg?raw=true)
5. Once that’s installed, you’ll have Python’s package manager, pip, included by default. Through pip, we’ll want to add a package called virtualenv to create a virtual environment for your project:  
**pip install virtualenv**
6. Using the **virtualenv** package, create a virtual environment called **venv** for the Django project, which will allow you to isolate the setup from the actual system itself. Run the following command to do so:  
**virtualenv venv**  
After you run this command, you will notice a **venv** folder created inside your current directory. 
7. Now activate the virtual environment your created using the following command (on a windows system)  
**venv\Scripts\activate.bat**  
**Note:** Remember, each time you want to run the application through the command line, you need to activate your virtual environment to do so. 
8. There are certain packages that need to be installed in order to run the application with all the implemented functionalities. Navigate inside the **'team_charlie_2020'** directory where the **manage.py** file of the code is stored and run the following pip commands one by one:  
```
pip install Django==2.2.9  
pip install djongo==1.2.36  
pip install sqlparse==0.2.4  
pip install Pillow==7.2.0  
pip install django-filter==2.3.0
pip install django-jquery==3.1.0  
pip install django-multiselectfield==0.1.12  
pip install django-simple-history==2.11.0  
pip install django-user-sessions==1.7.1  
pip install dnspython==1.16.0  
pip install selenium==3.141.0  
pip install xhtml2pdf==0.2.4  
pip install reportlab==3.5.46  
pip install six==1.15.0  
pip install html5lib==1.1  
pip install PyPDF2==1.26.0  
pip install urllib3==1.25.9  
pip install webencodings==0.5.1 
```
9. Now that the packages have been installed, download MongoDB installation file from the following link in order to create a database for the application on your local machine:  
https://www.mongodb.com/try/download/community    
After downloading, complete the installation of MongoDB.
10. Once MongoDB has been installed, download MongoDB Compass which is an interactive GUI to view your database collections and documents from the following website:  
https://www.mongodb.com/try/download/compass  
Install MongDB compass by running the downloaded installation file.
11. Once the MongoDB and MongoDB Compass have been installed on the local machine, open the MongoDB Compass software and create a new connection with the following details and then click the **'Connect'** button  
![Image2](https://github.com/UoA-CS5942/team_charlie_2020/blob/master/static/images/deployment2.jpg?raw=true)

12. Once you have connected to your local MongoDB, the database collections of the STS application need to be migrated on your newly setup MongoDB. In order to do so run the following two commands in a sequence:  
**python manage.py makemigrations  
python manage.py migrate**  
After running these two commands, all the required collections of the application will be created in your local MongoDB. You can view them by refreshing the view on MongoDB Compass. You will see your newly created database called **'STS2'**.
13. Now that both Python, Django and MongoDB installations have been completed, a superuser account needs to be created in order to login to the website. Run the following command to create a superuser:  
**python manage.py createsuperuser**
Enter a username, email id and password for the account as shown in the following image.  
![Image3](https://github.com/UoA-CS5942/team_charlie_2020/blob/master/static/images/deployment3.jpg?raw=true)

14. Now that all the installations and setup have been done, run the application by entering the following command on the terminal window:  
**python manage.py runserver**
15. After running the server, you can access the website on the following link:  
http://localhost:8000/
16. Upon entering the above link, a login form will be displayed. Enter the superuser account username and password you created in Step 13.
17. After logging in you will be redirected to a page with the following message:
![Image4](https://github.com/UoA-CS5942/team_charlie_2020/blob/master/static/images/deployment4.jpg?raw=true)  
This is because the code defines two groups of users: **Admin and Users** to whom the webpages are accessible. Therefore, the next step is to create these two groups from the admin panel.
18. Navigate to the following url in order to create the 'Admin' and 'Users' groups:  
http://localhost:8000/admin
19. Now click on the **'Groups'** link and click on the **'Add Group'** button on the top right corner. 
20. Create a group for admin users called **'admin'** as shown in the following image and save the group. (Note: the name is case-sensitive so save the name with a small 'a' not a capital 'A'.)
![Image5](https://github.com/UoA-CS5942/team_charlie_2020/blob/master/static/images/deployment5.jpg?raw=true)  

21. Create a group for normal users called **'users'** as shown in the following image and save the group. (Note: the name is case-sensitive so save the name with a small 'u' not a capital 'U'.)  
![Image6](https://github.com/UoA-CS5942/team_charlie_2020/blob/master/static/images/deployment6.jpg?raw=true)  

22. In order to make the webpages accessible to any user on the STS application, the user needs to be assigned into either the **'admin'** group or the **'users'** group. For example, since you have created a superuser on the website during the setup, you can try and assign that user to the admin group to check whether you can view the web pages of the STS application. In order to assign your created account to the **'admin'** group navigate to the following link:  
http://localhost:8000/admin/auth/user/
23. Now click on your username as displayed in the image below:  
![Image7](https://github.com/UoA-CS5942/team_charlie_2020/blob/master/static/images/deployment7.jpg?raw=true)  

24. Scroll down to the groups section as displayed in the image below and select the admin group and click on the arrow to assign the **'admin'** group for your account:
![Image8](https://github.com/UoA-CS5942/team_charlie_2020/blob/master/static/images/deployment8.jpg?raw=true)  

25. Scroll down on the page to **Save** the changes and navigate to the following link to access the Analytics Dashboard and remaining pages of the website displayed on the Navbar:  
http://localhost:8000/
26. You should now be able to view the pages of the website as displayed in the image below:  
![Image9](https://github.com/UoA-CS5942/team_charlie_2020/blob/master/static/images/deployment9.jpg?raw=true)  
**Note:** Each time a new user account is created on the admin panel, the account needs to be assigned to either the **'admin'** or the **'users'** group to make the view pages accessible to the user.


### Deploying the Application on Microsoft Azure using MongoDB Atlas Cluster
1. Download the STS application code from the Github link or take a clone of the repository on a local machine using the following git command:  
git clone https://github.com/UoA-CS5942/team_charlie_2020.git
2. After taking a clone of the code, download the executable installer of Python version 3.6 from the following link:  
https://www.python.org/downloads/release/python-360/
3. Run the executable file to install Python on your machine.
4. After the installation has successfully been completed, open your command prompt and **cd** into the folder where the STS code has been downloaded as shown in the following screenshot:
![Image1](https://github.com/UoA-CS5942/team_charlie_2020/blob/master/static/images/deployment.jpg?raw=true)

5. Once that’s installed, you’ll have Python’s package manager, pip, included by default. Through pip, we’ll want to add a package called virtualenv to create a virtual environment for your project:  
**pip install virtualenv**
6. Using the **virtualenv** package, create a virtual environment called **venv** for the Django project, which will allow you to isolate the setup from the actual system itself. Run the following command to do so:  
**virtualenv venv**  
After you run this command, you will notice a **venv** folder created inside your current directory. 
7. Now activate the virtual environment your created using the following command (on a windows system)  
**venv\Scripts\activate.bat**  
**Note:** Remember, each time you want to run the application through the command line, you need to activate your virtual environment to do so. 
8. There are certain packages that need to be installed in order to run the application with all the implemented functionalities. Navigate inside the **'team_charlie_2020'** directory where the **manage.py** file of the code is stored and run the following pip commands one by one:  
```
pip install Django==2.2.9  
pip install djongo==1.2.36  
pip install sqlparse==0.2.4  
pip install Pillow==7.2.0  
pip install django-filter==2.3.0
pip install django-jquery==3.1.0  
pip install django-multiselectfield==0.1.12  
pip install django-simple-history==2.11.0  
pip install django-user-sessions==1.7.1  
pip install dnspython==1.16.0  
pip install selenium==3.141.0  
pip install xhtml2pdf==0.2.4  
pip install reportlab==3.5.46  
pip install six==1.15.0  
pip install html5lib==1.1  
pip install PyPDF2==1.26.0  
pip install urllib3==1.25.9  
pip install webencodings==0.5.1 
```
5. Now that you have installed Python and Django on your machine, login to your Microsoft Azure account and go to the following link in order to create a resource:  
https://portal.azure.com/#create/hub
6. Click on the **Web App** option to create a new application.
7. Choose the subscription, resource group, runtime stack **(Python 3.6)**, operating system **(Linux)** and region as displayed in the image below:  
![Image10](https://github.com/UoA-CS5942/team_charlie_2020/blob/master/static/images/deployment10.jpg?raw=true)  

8. Click on the **Review+create** button and finally click on the Create button to create your web application.
9. You will see the following message on doing so:  
![Image11](https://github.com/UoA-CS5942/team_charlie_2020/blob/master/static/images/deployment11.jpg?raw=true)  

10. Once your web application is created, you will be able to access it in the **'Resources'** section or at the following link:  
https://portal.azure.com/#blade/HubsExtension/BrowseAll
11. In order to deploy the STS application onto the newly created web application resource on Microsoft Azure you will have to upload the code onto your Github account. Therefore, create a new repository on Github and upload all the application code files on it.
12. Now create a MongoDB Atlas account on the following link:  
https://www.mongodb.com/try
13. After creating an account on MongoDB Atlas, create an organization as displayed in the image below:    
![Image12](https://github.com/UoA-CS5942/team_charlie_2020/blob/master/static/images/deployment12.jpg?raw=true)  

14. Once the organization is created, create a Project within the organization as displayed below:  
![Image13](https://github.com/UoA-CS5942/team_charlie_2020/blob/master/static/images/deployment13.jpg?raw=true)  

15. After creating a Project on MongoDB Atlas, create a new cluster within the project with Azure as the cloud provider as displayed in the image below:  
![Image14](https://github.com/UoA-CS5942/team_charlie_2020/blob/master/static/images/deployment14.jpg?raw=true)  

16. After the cluster has been created, click on the **'Database Access'** section as displayed in the image below to create a new Database user for your cluster and remember the password for this user. While entering the details, also assign **'Atlas admin'** role to the user:
![Image15](https://github.com/UoA-CS5942/team_charlie_2020/blob/master/static/images/deployment15.jpg?raw=true)  

17. In order to allow the deployed application to interact with the MongoDB Atlas cluster, go to the **'Properties'** section of your deployed application on Microsoft Azure and copy all the outbound IP addresses. Now on the MongoDB Atlas account click on the **'Network Access'** section to configure network access from the outbound IP addresses of the deployed application. Click on the **'IP Whitelist'** section and add each outbound IP address entry one after the other to allow access from all the outbound IP addresses of the deployed application as displayed in the screenshot below:  
![Image16](https://github.com/UoA-CS5942/team_charlie_2020/blob/master/static/images/deployment16.jpg?raw=true)  

18. Now that you have created a cluster, database user and configured the network access of your cluster, you can click on the **'Connect'** button as displayed in the image below and then click on **'Connect your application'** to copy the connection details to your MongoDB cluster which will be required to connect your deployed Azure site with your MongoDB Atlas cluster:  
![Image17](https://github.com/UoA-CS5942/team_charlie_2020/blob/master/static/images/deployment17.jpg?raw=true)  

19. On selecting the **'Connect your application'** button, the following screen will be displayed where you will need to select **'Python'** as the driver and **'3.6 or later'** as the version. After selecting these two values, you will notice a connection string value as displayed in the image below, copy the string:
![Image18](https://github.com/UoA-CS5942/team_charlie_2020/blob/master/static/images/deployment18.jpg?raw=true)  

20. Open the **'settings.py'** file located inside the STS folder and go to the DATABASES section of the file. Replace the NAME value with the database username you created on MongoDB Atlas, PASSWORD value with the password of your database user and HOST value with the connection string which you copied in Step 19. Do this for both default and test database as displayed in the following screenshot.  
![Image19](https://github.com/UoA-CS5942/team_charlie_2020/blob/master/static/images/deployment19.jpg?raw=true)  

21. In order for the static files to load on Microsoft Azure server, the following additional modifications need to be made in the **'settings.py'** file:
* Above the **'STATIC_URL**' line, add the following line:  
**STATIC_ROOT = os.path.join(BASE_DIR, 'static')**  
* In the **'STATICFILES_DIRS'** line, remove the following code:
**os.path.join(BASE_DIR, 'static')**  
After making the above two modifications the **'settings.py'** file should look like this:  
```
STATIC_ROOT = os.path.join(BASE_DIR, 'static')  
STATIC_URL = '/static/'  
STATICFILES_DIRS = [  
    ("admin", "/static/admin/css"),  
]  
MEDIA_URL = '/images/'  
MEDIA_ROOT = os.path.join(BASE_DIR, 'static/images')
```
22. Now that the MongoDB account and Microsoft Azure account have been setup, the next step is to integrate Microsoft Azure with your Github account. On your local machine download Git from the following link in order to push any file changes to your STS Github repository from your local machine:   
https://git-scm.com/downloads 
23. Create a new repository in your Github account.  
24. After downloading and installing Git on your local machine, activate your virtual **'venv'** environment, **'cd'** into the STS code repository where the **'manage.py'** file is located and run the following commands to initialize a new Git repository and upload the STS code files onto your Github repository (Replace the link with the link of your github repository in the second command):  
``` 
git init  
git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO  
git pull origin master  
git add -A  
git commit -m "Initial commit"   
git push origin master
```
25. Now all the STS code files should be uploaded onto your Github account.
26. Next step is to connect your Azure account to your Github account. In your Microsoft Azure account click on the newly created web application. You will notice a **'Deployment Center'** option on the left sidebar. Click on that option. It will display 3 options on the screen as shown below:  
![Image20](https://github.com/UoA-CS5942/team_charlie_2020/blob/master/static/images/deployment20.jpg?raw=true)  

27. Click on **'Deploy through Github'**  then click **'Use the App Service build service'** and then configure with your Github account repo and branch details of the STS application.  
28. You should now be able to access your deployed website through the **Browse** section on the **Overview** tab of the left sidebar. However, it will display an error message since there is one more step to be completed.
29. In order to complete the deployment on Microsoft Azure, an additional file with a list of all the packages to be installed and their versions needs to be created in order for the application to work with all the functionalities. This file needs to be called **'requirements.txt'** and needs to be saved into the root project folder on your local machine along with the **'manage.py'** file. Any new packages that are installed within the application need to be mentioned in this file along with their versions in order for them to be installed on the Azure deployed site. The file should look like this:  
![Image21](https://github.com/UoA-CS5942/team_charlie_2020/blob/master/static/images/deployment21.jpg?raw=true)  

30. If you don't have a '**requirements.txt'** file within your STS code repository create it as described in step 29 and push it to your github account. If it already exists skip to the next step.
31. Now that your Microsoft Azure account is connected to your Github repository and MongoDB Atlas Cluster, the database collections of the STS application need to be migrated on your newly setup MongoDB Atlas account. In order to do so open a command prompt on your local machine and **'cd'** into the working directory of the STS application. Run the following two commands in a sequence:  
**python manage.py makemigrations**  
**python manage.py migrate**  
After running these two commands, all the required collections of the application will be created in your MongoDB Atlas cluster as displayed in the image below:  
![Image22](https://github.com/UoA-CS5942/team_charlie_2020/blob/master/static/images/deployment22.jpg?raw=true)  

32. You can view the database collections by clicking on the **'Collections'** tab on your MongoDB Atlas cluster as displayed in the image below:  
![Image23](https://github.com/UoA-CS5942/team_charlie_2020/blob/master/static/images/deployment23.jpg?raw=true)  

33. Now that both Microsoft Azure and MongoDB Atlas setup has been completed, a superuser account needs to be created in order to login to the website. Run the following command in the command prompt on your local machine to create a superuser:  
**python manage.py createsuperuser**  
Enter a username, email id and password for the account as shown in the following image.  
![Image24](https://github.com/UoA-CS5942/team_charlie_2020/blob/master/static/images/deployment24.jpg?raw=true)  

34. Your STS application should now be accessible on the deployed link on the Microsoft Azure account.
35. Access the link of the site by clicking on the **'Browse'** option present on the **'Overview'** tab on the Azure account as displayed below:  
![Image25](https://github.com/UoA-CS5942/team_charlie_2020/blob/master/static/images/deployment25.jpg?raw=true)  

36. Upon entering the above link, a login form will be displayed. Enter the superuser account username and password you created in Step 33.
37. After logging in you will be redirected to a page with the following message:  
![Image26](https://github.com/UoA-CS5942/team_charlie_2020/blob/master/static/images/deployment26.jpg?raw=true)  
This is because the code defines two groups of users: **Admin** and **Users** to whom the webpages are accessible. Therefore, the next step is to create these two groups from the admin panel.  

38. Navigate to admin page in order to create the **'Admin'** and **'Users'** groups:  
http://linkofthewebsite/admin/  
Replace **linkofthewebsite** with the url of your deployed site.
39. Now click on the **'Groups'** link and click on the **'Add Group'** button on the top right corner. 
40. Create a group for admin users called **'admin'** as shown in the following image and save the group. (Note: the name is case-sensitive so save the name with a small 'a' not a capital 'A'.)
![Image27](https://github.com/UoA-CS5942/team_charlie_2020/blob/master/static/images/deployment27.jpg?raw=true)  

41. Create a group for normal users called **'users'** as shown in the following image and save the group. (Note: the name is case-sensitive so save the name with a small **'u'** not a capital **'U'**.)  
![Image28](https://github.com/UoA-CS5942/team_charlie_2020/blob/master/static/images/deployment28.jpg?raw=true)  

42. In order to make the webpages accessible to any user on the STS application, the user needs to be assigned into either the **'admin'** group or the **'users'** group. For example, since you have created a superuser on the website during the setup, you can try and assign that user to the admin group to check whether you can view the web pages of the STS application. In order to assign your created account to the **'admin'** group navigate to the following link:  
http://linkofthewebsite/admin/auth/user/  
Replace **linkofthewebsite** with the url of your deployed site.
43. Now click on your username as displayed in the image below:  
![Image29](https://github.com/UoA-CS5942/team_charlie_2020/blob/master/static/images/deployment29.jpg?raw=true)  

44. Scroll down to the groups section as displayed in the image below and select the admin group and click on the arrow to assign the **'admin'** group for your account:  
![Image30](https://github.com/UoA-CS5942/team_charlie_2020/blob/master/static/images/deployment30.jpg?raw=true)  

45. Scroll down on the page to Save the changes and navigate to the following link to access the Analytics Dashboard and remaining pages of the website displayed on the Navbar:  http://linkofthewebsite/  
Replace **linkofthewebsite** with the url of your deployed site.
46. In order for some static css files of the admin panel to load, you will need to run one final command on the **SSH terminal** of the STS web application. In the App service of your application, select the **'SSH'** option from the left sidebar in order to open the SSH terminal of your web application and cd into the **/site/wwwroot** directory as displayed in the image below: 
![Image30-1](https://github.com/UoA-CS5942/team_charlie_2020/blob/master/static/images/staticfiles.jpg?raw=true)  

47. Run the following pip commands one by one on the **SSH terminal**:  
```
pip install Django==2.2.9  
pip install djongo==1.2.36  
pip install sqlparse==0.2.4  
pip install Pillow==7.2.0  
pip install django-filter==2.3.0
pip install django-jquery==3.1.0  
pip install django-multiselectfield==0.1.12  
pip install django-simple-history==2.11.0  
pip install django-user-sessions==1.7.1  
pip install dnspython==1.16.0  
pip install selenium==3.141.0  
pip install xhtml2pdf==0.2.4  
pip install reportlab==3.5.46  
pip install six==1.15.0  
pip install html5lib==1.1  
pip install PyPDF2==1.26.0  
pip install urllib3==1.25.9  
pip install webencodings==0.5.1 
```

48. Now run the following command on the **SSH Terminal** to collect the static files to be served on the production site:
**python manage.py collectstatic**

49. You should now be able to view the pages of the website as displayed in the image below:  
![Image31](https://github.com/UoA-CS5942/team_charlie_2020/blob/master/static/images/deployment31.jpg?raw=true)  
**Note:** Each time a new user account is created on the admin panel, the account needs to be assigned to either the **'admin'** or the **'users'** group to make the view pages accessible to the user.

## Unit and Integration Testing of the Application 
* Unit testing using Python's unittest library to verify the behavior of individual components
* Selenium based Integration testing to test behavior of Web pages. Series of functional test cases written to verify the correctness of each functionality, verify how different components work together and to simulate a real user's interactions with multiple pages and functionalities on the STS application.

### Running the Tests of the Application on a Local Machine
1. In order for some integration tests to function, make sure you have a user named **'Bob'** stored within the database who is not blacklisted. The purpose of the test is to ensure the correctness of the blacklist functionality after 3 incorrect password attempts of the user. In order to create a user named **'Bob'**, go to the following link to create a user:  
http://localhost:8000/admin/auth/user/add/
2. In order for some integration tests to function, make sure you have a user named **'admin'** stored within the database with the password **'stsjf2020'**. The purpose of the test is to ensure the correctness of the search filter on the Users page. In order to create the user, go to the following link:  
http://localhost:8000/admin/auth/user/add/
3. In order for some integration tests to function, make sure you have a user named **'user'** stored within the database with the password **'stsjf2020'**. The purpose of the test is to ensure the correctness of the login redirection for normal users. In order to create the user, go to the following link:  
http://localhost:8000/admin/auth/user/add/
4. In order for some integration tests to function, make sure you have a location named **'Maldives'** stored within the database. The purpose of the test is to ensure the correctness of the search filter on the Locations page. In order to create the location, go to the following link:  
http://localhost:8000/admin/accounts/entry/add/
5. In order for some integration tests to function, make sure you **don't** have a user named **'Alice'** stored within the database. The purpose of the test is to ensure the admin can create a new user account on the admin panel. In order to check whether the user account doesn't exist, go to the following link:  
http://localhost:8000/admin/auth/user/  
6. In order to run the tests on the local machine, you will need to open two command prompts. One to run the localhost server and the other to run the tests. Therefore **'cd'** into the working directory of the STS application on your local machine on both the terminals. 
7. On terminal window 1 run the server using the **python manage.py runserver** command.
8. Now to run the tests on terminal window 2 run the following command:  
**python manage.py test accounts**
9. Upon running the tests, you should see the following message displayed in the image:  
![Image32](https://github.com/UoA-CS5942/team_charlie_2020/blob/master/static/images/testing.jpg?raw=true)  


### Running the Tests of the Deployed Application on a local machine
1. In order for some integration tests to function, make sure you have a user named **'Bob'** stored within the database who is not blacklisted. The purpose of the test is to ensure the correctness of the blacklist functionality after 3 incorrect password attempts of the user. In order to create a user named **'Bob'**, go to the following link to create a user:  
https://linkofthewebsite/admin/auth/user/add/  
Replace **linkofthewebsite** with the url of your deployed site.
2. In order for some integration tests to function, make sure you have a user named **'admin'** stored within the database with the password **'stsjf2020'**. The purpose of the test is to ensure the correctness of the search filter on the Users page. In order to create the user, go to the following link:  
https://linkofthewebsite/admin/auth/user/add/  
Replace **linkofthewebsite** with the url of your deployed site.
3. In order for some integration tests to function, make sure you have a user named **'user'** stored within the database with the password **'stsjf2020'**. The purpose of the test is to ensure the correctness of the login redirection for normal users. In order to create the user, go to the following link: 
https://linkofthewebsite/admin/auth/user/add/  
Replace **linkofthewebsite** with the url of your deployed site.
4. In order for some integration tests to function, make sure you have a location named **'Maldives'** stored within the database. The purpose of the test is to ensure the correctness of the search filter on the Locations page. In order to create the location, go to the following link:  
https://linkofthewebsite/admin/accounts/entry/add/  
Replace **linkofthewebsite** with the url of your deployed site. 
5. In order for some integration tests to function, make sure you **don't** have a user named **'Alice'** stored within the database. The purpose of the test is to ensure the admin can create a new user account on the admin panel. In order to check whether the user account doesn't exist, go to the following link:  
https://linkofthewebsite/admin/auth/user/  
Replace **linkofthewebsite** with the url of your deployed site. 
6. Open the **'tests.py'** file located on the working directory of the STS application present on your local machine. It is stored inside the **team_charlie_2020/accounts** directory.
7. In the **'tests.py'** file, replace all occurrences of **'http://127.0.0.1:8000/login/'** with the login link of your Azure deployed site.
8. In the **'tests.py'** file, within **'def test_redirect_home_if_not_logged_in(self)'** replace **'response = self.client.get('/')'** with **'response = self.client.get('https://linkofthewebsite/')'**.
9. In the **'tests.py'** file, within **'def test_redirect_locations_if_not_logged_in(self)'** replace **'response = self.client.get('/locations/')'** with **'response = self.client.get('https://linkofthewebsite/locations/')'**.
10. In the **'tests.py'** file, within **'def test_redirect_auditlogs_if_not_logged_in(self)'** replace **'response = self.client.get('/auditlogs/')'** with **'response = self.client.get('https://linkofthewebsite/auditlogs/')'**
11. In the **'tests.py'** file, within **'def test_redirect_users_if_not_logged_in(self)'** replace **'response = self.client.get('/users/')'** with **'response = self.client.get('https://linkofthewebsite/users/')'**
12. In order to run the tests on the local machine, **'cd'** into the working directory of the STS application on your local machine. 
13. Now to run the tests, run the following command on the terminal:  
**python manage.py test accounts**
14. Upon running the tests, you should see the following message displayed in the image:  
![Image33](https://github.com/UoA-CS5942/team_charlie_2020/blob/master/static/images/testing.jpg?raw=true)  


 ### MongoDB Atlas Charts
 1. In order to create MongoDB Charts and embed them on the STS application, login to your MongoDB Atlas account.
 2. After logging in go to the MongoDB cluster you have created for the STS application and click on the **'Charts'** tab as displayed in the image given below:
 ![Image34](https://github.com/UoA-CS5942/team_charlie_2020/blob/master/static/images/charts.jpg?raw=true)  
 
 3. Now click on the **'Add Dashboard'** button to create a new dashboard for the charts.
 4. After a Dashboard has been created, you need to specify a Data source to load the data from the database onto the charts. Click on the **'Data Source'** button in the left sidebar as displayed in the image below:
 ![Image35](https://github.com/UoA-CS5942/team_charlie_2020/blob/master/static/images/charts2.jpg?raw=true)  

 5. On the **Data source** section click on the **'Add Data Source'** button to add your database as the source. On clicking the button you will see the following popup window with a list of your clusters. Click on the cluster with your STS Database and then click on the **'Next'** button. 
 ![Image36](https://github.com/UoA-CS5942/team_charlie_2020/blob/master/static/images/charts3.jpg?raw=true)  
 
 6. Select the **'STS'** checkbox to load the collections of the database and click on the **'Finish'** button.
 7. Now that the data source and collections have been added to your dashboard, the next step is to create and configure charts. Click on the **'Dashboards'** button on the left sidebar to go back to the dashboard page.
 8. On this page, click on your Dashboard as displayed in the image below:
  ![Image37](https://github.com/UoA-CS5942/team_charlie_2020/blob/master/static/images/charts4.jpg?raw=true)  
 
 9. On this screen click on the **'Add Chart'** button on the top right corner to add your first chart to your dashboard which is now also connected to your MongoDB STS database.
 10. On the top right corner, click on the **'Choose a Data Source'** dropdown to select the collection you want to create a graph for. As displayed in the image given below we have selected the **'STS.accounts_entry'** collection which stores the data of all the STS locations.
 ![Image38](https://github.com/UoA-CS5942/team_charlie_2020/blob/master/static/images/charts5.jpg?raw=true)  
 
11. Select a chart type from the **'Chart Type'** dropdown and drag fields from the **'Fields'** list onto the **'X Axis'** and **'Y Axis'** as displayed in the image below to load the chart with the data from the selected collections:
 ![Image39](https://github.com/UoA-CS5942/team_charlie_2020/blob/master/static/images/charts6.jpg?raw=true)  

12. You can click on the **'Customize'** button to customize the label names of the **'X and Y axes'**.
13. Once the chart has been created and finalized, click on the **'Save and Close'** button to save the chart.
14. After saving the chart you will be redirected to the **'Charts'** page with the newly created chart. Click on the **'Embed Chart'** option of the chart as displayed in the image given below:
 ![Image40](https://github.com/UoA-CS5942/team_charlie_2020/blob/master/static/images/charts7.jpg?raw=true)  

15. On the popup window, click on **'Enable Unauthenticated Access'** as displayed in the image given below:
![Image41](https://github.com/UoA-CS5942/team_charlie_2020/blob/master/static/images/charts8.jpg?raw=true)  

16. Click on the **'Iframe button'** and copy the embed code as displayed in the image below:
![Image42](https://github.com/UoA-CS5942/team_charlie_2020/blob/master/static/images/charts9.jpg?raw=true)  

17. Paste the embed code in any html page of the STS application where you would want to display the charts. (Currently charts are displayed on the status.html template file present inside the templates directory of the STS code repository)

### Maps
This application uses Mapbox with a marker for displaying locations of each STS Location.


## Github Commands

#### To update your working branch, you need to follow these steps:
```
1. cd into your project
2. git branch name - to create a working branch
7. git pull - to update working branch before making changes 
8. git add - A  to add all changes made 
9. git commit -m "comment"- to commit the changes made 
10. git push - to push the change from working branch to master branch
11. Open GitHub and create a pull request
12. Review changes and merge it 
```

## Security Measures
1. Storing encrypted passwords - Django stores encrypted passwords instead of plain-text passwords. The components used to store a User's password include a hashing algorithm, a random salt and a resulting password hash. By default Django uses a PBKDF2 algorithm with a SHA256 hash which is secure and would require a lot of computing time to break.
2. Password Lockout functionality - A flag based blacklist functionality for the login form to check incorrect login attempts of users. Upon each incorrect login attempt a flag is set to true. After 3 incorrect login attempts the user is added to the blacklist. 

___

# USER MANUAL OF STS APPLICATION

The user manual is intended to facilitate users of STS web application to understand the features and functionalities and able to use the STS application with ease.

In order to provide the operational status of Fendercare STS transfer process, the web application is developed with the help of NoSQL Mongo database that has embedded all the related data in a single collection called Entry. This Entry collection allows admin users of the STS web application to add the STS details for each location through a superuser login which has been granted with all available permissions, so that the admin users can effectively manage the information and logistics of the STS operations online without any manual processes. There is a separate login for normal users who have limited permissions only to view certain pages of the STS application.

## 1. Authentication and Authorization for admin users

Django’s default configuration serves most of the common authentication and authorization process required for the administration of web application. Below are the basic authentication processes available for the people who interact with the STS web application and also highlights the steps to be followed by the users who manages the administration.

### 1.1 Running migrations

After setting up the Mongodb account and installation requirements as mentioned in the maintenance manual, the admin user can open the command prompt on the local machine and ‘cd’ into the working directory of the STS application. Run the following commands in a sequence.

```
python manage.py makemigrations
python manage.py migrate
```
After running these two commands, all the required collections of the application will be created in your MongoDB Atlas cluster by **running migrations**.

![Image43](https://github.com/UoA-CS5942/team_charlie_2020/blob/master/static/images/screenshot1.png?raw=true)

                                             

### 1.2 Creating superuser

Superusers are initially created by the developer for the admin users using _**python manage.py createsuperuser**_ command by entering the username as ‘admin’, password and email id.

![Image44](https://github.com/UoA-CS5942/team_charlie_2020/blob/master/static/images/screenshot2.png)

After running the server using _**python manage.py runserver**_ command, enter the superuser credentials to login to the web application. However, you will be redirected to the following **Value error while accessing home page without any user group creation**.  

![Image45](https://github.com/UoA-CS5942/team_charlie_2020/blob/master/static/images/screenshot3.png)


This is because the code defines two groups of users: **Admin** and **Users** to whom the webpages are accessible. Therefore, it is important for the superuser to create these two groups from the admin panel and accordingly grant permissions for each category of users.

### 1.3 Creating user groups

The superuser can navigate to the admin page to create the below two types of user groups using **http://linkofthewebsite/admin/**. The linkofthewebsite can be replaced with the url of the deployed site. 

•	**Admin** – this category of user has been allocated with all the available permissions for this application. Therefore, this user can delete, change and view all the available data as well as add any new data to STS web application. The superuser account created in section 2.1 should be added to the admin group category.

•	**Users** – this user by default has been allocated to only view the locations of the STS processed data supplied by the admin users. 

Following are the step by step procedure with screenshots for creating two user groups, users and to access the home page of the website:

**i.**	Click on the **‘Groups’** link and click on the **‘Add Group’** button on the top right corner. 
**ii.**	Create a group for admin users called **‘admin’** as shown in the following image and save the group. (Note: the name is case-sensitive so save the name with a small 'a' not a capital ‘A’.)
***iii.***	Choose all the permissions for **admin user group** and save it.

![Image46](https://github.com/UoA-CS5942/team_charlie_2020/blob/master/static/images/screenshot4.png)


**iv.**	Then, create another group for normal users called **‘users’** as shown in the following image and save the group. (Note: the name is **case-sensitive** so save the name with a small ‘u’ not a capital ‘U’.)
**v.**	It is recommended to save this **‘users’** group with no permissions to avoid any permission conflicts as mentioned in section 2.4. Although you can choose limited permissions to provide restricted access to the admin panel, it is better to grant the restricted permissions individually to each user in the next step.

![Image47](https://github.com/UoA-CS5942/team_charlie_2020/blob/master/static/images/screenshot5.png)


### 1.4 Assigning admin user and adding other users to the defined user group

In order to make the webpages accessible to any user on the STS application, the user needs to be assigned into either the **‘admin’** group or the **‘users’** group. For example, since you have created a superuser on the website during the setup, you can try and assign that user to the admin group to check whether you can view the web pages of the STS application. 

**vi.**	Assign your created superuser account to the **‘admin’** group by navigating to the following link: http://linkofthewebsite/admin/auth/user/ and replace linkofthewebsite with the url of your deployed site for **assigning admin user to ‘admin’ user group**.

![Image48](https://github.com/UoA-CS5942/team_charlie_2020/blob/master/static/images/screenshot6.png)


**vii.**	After saving the changes, the admin user should now be able to view the **dashboard page view** of the website as displayed in the below image.

![Image49](https://github.com/UoA-CS5942/team_charlie_2020/blob/master/static/images/screenshot7.png)


**viii.**	Click on the Users link and click on the **‘Add User’** button on the top right corner. 
**ix.**	Add username and password credentials to **create a new user** which will then be redirected to http://linkofthewebsite/admin/auth/user/2/change/ where you can fill the personal details and assign this user to **‘users’** group as mentioned in the screenshot. Save these changes and add as many users as you wish by following the same step.

![Image50](https://github.com/UoA-CS5942/team_charlie_2020/blob/master/static/images/screenshot8.png)


**x.**	The newly created user can now login to his account and will have access to the below **dashboard page of the default user account without any permissions to the admin page**.

![Image51](https://github.com/UoA-CS5942/team_charlie_2020/blob/master/static/images/screenshot9.png)


### 1.5 Permissions available in STS

The built-in permissions of Django admin page for the **‘admin’** group of users has access to view, add, change or delete permissions for the different category of objects created in the Models and for the functionalities available in the Django admin panel. STS web application currently has 104 permissions.

By default, the normal users allocated to **‘users’** group will not have access to the admin page view and will receive the below **error message if they try to access the admin page**.

![Image52](https://github.com/UoA-CS5942/team_charlie_2020/blob/master/static/images/screenshot10.png)

Having said that, the superuser will have an option to assign some users to admin page by explicitly allowing permission to access some of the admin pages available in STS application as mentioned in the below steps.

### Steps to be followed by Superuser to assign restricted admin rights permissions to the normal user 

**i.** Select the **'users'** from the 'Authentication and Authorization' section of the admin page and enter the name of the user in the search bar whom you would like to allow permissions.

**ii.**	It displays the personal information and the already available permissions for that particular user. In permissions section, the **‘staff status’** checkbox is not selected by default. The admin shall first select the **‘staff status’ to authorize the admin page view for the normal user** as mentioned below.

**iii.** Ensure that **‘superuser status’ checkbox is not selected for the normal user** because this option will allow any normal user to have the complete superuser rights in the admin page.

![Image53](https://github.com/UoA-CS5942/team_charlie_2020/blob/master/static/images/screenshot11.png)

**iv.**	Then, the superuser can select the required user permissions to this user to allow access to admin page and perform the allowed actions alone. 

![Image54](https://github.com/UoA-CS5942/team_charlie_2020/blob/master/static/images/screenshot12.png)


**v.** After being granted with the above **restricted user permissions**, the normal user will now be able to navigate to the admin page and perform the authorized actions alone as mentioned in the following image.

![Image55](https://github.com/UoA-CS5942/team_charlie_2020/blob/master/static/images/screenshot13.png)

In this way, the superuser can assign restricted permissions to the admin page for individual users by selecting the staff status. 

**Following points should be taken into consideration by the superuser while managing the user group and users:**

•	In order to avoid any conflicts in the restricted permissions, it is important not to allow any **‘User permissions’** to the **‘users’** group as mentioned in the initial steps of group creation.

•	This is because the **group permissions always supersede any other permissions assigned to each individual user**. For instance, if the admin user assigns different user permissions to ‘users’ group and different permissions to individual users belonging to the same ‘users’ group, it will lead to conflict. So, it is **recommended not to assign any permissions to the ‘users’ group**.

•	Allowing **restricted ‘User permissions’ for individual users** facilitates the superuser for better control and management of accounts.

### 1.6 Users page

User page will provide the summary of the complete list of users created to access the STS web application. Super user can select **‘delete selected user’** from the Action dropdown to delete any of the users and also edit any permissions or user groups by clicking the individual users name. Below image represents the **normal user who can perform the allowed user permissions in the admin page**.

![Image56](https://github.com/UoA-CS5942/team_charlie_2020/blob/master/static/images/screenshot14.png)

### 2. FEATURES AND FUNCTIONALITIES

Below sections highlights the key features and functionalities of STS application for both admin and normal users.

### 2.1 ADMIN USERS

### 2.1.1 Adding STS location details from Admin page

Select **‘Entrys’** from the Accounts section of the admin page and then click **‘add entry’** to store STS process data for a new location. Below are some of the important points to consider while entering the location details.

**i.** Follow the **help text specified below the text fields** carefully and fill each of the field values in the mentioned format to view this information in the **‘viewlocations’** page without any issues. Some of the possible scenarios for errors are as follows.

• Below image highlights the **error when the latitude or longitude minutes or seconds values are not entered**.

![Image57](https://github.com/UoA-CS5942/team_charlie_2020/blob/master/static/images/screenshot15.png)

• Another possible error specified below highlights when the user provides **decimal values in the latitude or longitude degrees, minutes and seconds**.

![Image58](https://github.com/UoA-CS5942/team_charlie_2020/blob/master/static/images/screenshot16.png)

• In addition to the integer value for the latitude and longitude position, the admin user should **enter negative degree value for the south or west direction** to display the appropriate map in the **‘viewlocations’** page. For instance, the below image shows the negative degree value for **Richards Bay** location.

![Image59](https://github.com/UoA-CS5942/team_charlie_2020/blob/master/static/images/screenshot17.png)

**ii.** When the admin user tries to copy paste the special characters such as comma(,) , hifen (-), bullet points (•) etcetera from other documents or online, it saves the location fields as mentioned below but the user will not be able to generate the PDF from the **'viewlocations'** page and will therefore receive the error unicode message as highlighted in the subsequent image.

![Image60](https://github.com/UoA-CS5942/team_charlie_2020/blob/master/static/images/screenshot18.png)


• **unicode error message**
 
![Image61](https://github.com/UoA-CS5942/team_charlie_2020/blob/master/static/images/screenshot19.png)

• Such special characters will have to be manually replaced by the admin user as mentioned in the below screenshot.

![Image62](https://github.com/UoA-CS5942/team_charlie_2020/blob/master/static/images/screenshot20.png)

• By manually replacing the special characters from QWERTY keyboard, it can generate the PDF of the location information successfully from the **'viewlocations'** page for both admin and normal users.

![Image63](https://github.com/UoA-CS5942/team_charlie_2020/blob/master/static/images/screenshot21.png)



### 2.1.2 Blacklist functionality

As web security is vital for managing the confidential information of the company and personal details of the users, STS web application is enabled with the lockout functionality when the user try to login with three incorrect password attempts. 

**i.** The user will receive the below message when he tries to login with **incorrect password in the first attempt**. The admin can also validate the Mongo atlas account by verifying the flag value in **accounts_blacklist collection**. First flag value will be set to true in the Mongo database.

![Image64](https://github.com/UoA-CS5942/team_charlie_2020/blob/master/static/images/screenshot22.png)

**ii.** Below is the error message when he tries to login using **incorrect password in the second attempt**. Second flag value will be set to true in the Mongo database.
![Image65](https://github.com/UoA-CS5942/team_charlie_2020/blob/master/static/images/screenshot23.png)

**iii.* Below is the last error message when the user tries to login with **incorrect password in the third attempt and will be automatically blacklisted**. Third flag value will also be set to true in the Mongo database. The blacklist will be automatically released from the database after 6 hours of the lock out. Therefore, the user can either the right password after 6 hours or shall request admin via email to the provide the access immediately.

![Image66](https://github.com/UoA-CS5942/team_charlie_2020/blob/master/static/images/screenshot24.png)

**iv.** The login form has **Request access** button where the blacklisted user can send an email to the admin to retrieve the access to his account at the earliest.

![Image67](https://github.com/UoA-CS5942/team_charlie_2020/blob/master/static/images/screenshot25.png)

**v.** After receiving email from the user, the **admin can validate the blacklisted users list** from 'Blacklists' link of the admin page by selecting the username and clicking **delete selected blacklists** from the 'Actions' dropdown to remove the blacklist. 

![Image68](https://github.com/UoA-CS5942/team_charlie_2020/blob/master/static/images/screenshot26.png)

**vi.** Upon final confirmation from the admin, the blacklist will be removed. 

![Image69](https://github.com/UoA-CS5942/team_charlie_2020/blob/master/static/images/screenshot27.png)

### 2.1.3 Audit logs

Admin user can audit the changes made by the admin users by clicking the ‘Audit logs’ page. It has three categories of logs such as user logs, location entry logs and blacklisted user logs. 

**i.** Location entry logs**

Location entry logs displays all the saved changes made by admin users for updating the location fields in the entry. 

![Image70](https://github.com/UoA-CS5942/team_charlie_2020/blob/master/static/images/screenshot28.png)

View modifications allows you to verify the detailed changes made by the user. Each version of the changes made by any admin user will be stored in this log with the list of relevant modifications made during the change. You can revert to any of the saved changes by clicking ‘view’ button from the ‘location entry logs’.

![Image71](https://github.com/UoA-CS5942/team_charlie_2020/blob/master/static/images/screenshot29.png)

**ii. Blacklisted user logs**

Blacklisted user logs shows the list of the blacklisted users with the date, time and modifications made in each activity. Clicking the **view link** will provide the **Flag status** of the blacklisted user and allows to revert to that particular version of the change.

![Image72](https://github.com/UoA-CS5942/team_charlie_2020/blob/master/static/images/screenshot30.png)


**iii. User logs**

User logs comprises of both the changes made to the **location** fields in **entrys** as well as the **account management changes** made by the superuser.  

![Image73](https://github.com/UoA-CS5942/team_charlie_2020/blob/master/static/images/screenshot31.png)

**iv. Download PDF** 

Additionally, the **Audit logs page** allows the admin user to generate the PDF of all the available log details offline for any further validation. This page is available only for the admin users and will not be accessible for normal users.


### 2.1.4 Dashboard

The **dashboard page** available for the admin users displays some of the basic graphs such as 'Number of sessions', 'Number of locations' and 'Cargoes permitted category for all locations' that has been generated from MongoDb Atlas and embedded to STS web application. In the future, such graphs can be made available using this feature from MongoDb for any specific requirements.

![Image74](https://github.com/UoA-CS5942/team_charlie_2020/blob/master/static/images/screenshot32.png)

### 2.1.5 User page

This page displays the list of users who have access to the STS web application with their personal details. As the number of users would tend to increase, pagination has been enabled currently with 4 users per page and shall be modified according to the need of the client.

![Image75](https://github.com/UoA-CS5942/team_charlie_2020/blob/master/static/images/screenshot33.png)

### 2.2 COMMON FUNCTIONALITIES FOR BOTH ADMIN AND NORMAL USERS 

Below are some of the common functionalities available for both admin and normal users.

### 2.2.1 View Regions

As Fendercare marine provides STS services regions worldwide for more than 55 locations, STS application has region based location filter to view the locations from each of the region according to their convenience. All of the available regions has been updated in the dropdown of the **'Regions'** page.

![Image76](https://github.com/UoA-CS5942/team_charlie_2020/blob/master/static/images/screenshot34.png)

### 2.2.2 View all locations

In order to have both options, the users can also go to the **'All locations'** page to view all the location stored in the database. Pagination has been currently enabled in this page with 4 locations per page but this number can be increased in the future.

![Image77](https://github.com/UoA-CS5942/team_charlie_2020/blob/master/static/images/screenshot35.png)

### 2.2.3 View specific location

In **'All locations'**, the user can select the locations from the location filter irrespective of any region.

![Image78](https://github.com/UoA-CS5942/team_charlie_2020/blob/master/static/images/screenshot36.png)

### 2.2.4 FAQs for admin users

Based on the common problems experienced by the users of the STS application, FAQs has been made available to both the admin and normal users for their respective functionalities.

**i.** Admin users can click the **'FAQs for admin page'** to identify a quick solution for the common problems faced by them.

![Image81](https://github.com/UoA-CS5942/team_charlie_2020/blob/master/static/images/screenshot39.png)

Although the **FAQs for users** is available in the dropdown, the admin cannot view this page as mentioned below.

![Image79](https://github.com/UoA-CS5942/team_charlie_2020/blob/master/static/images/screenshot37.png)

### 2.2.5 FAQs for normal users

**ii.** In the same way, the normal users can also click **'FAQs for users'** to quickly clarify their queries. Normal users cannot see FAQs for admin users in the FAQs dropdown.

![Image80](https://github.com/UoA-CS5942/team_charlie_2020/blob/master/static/images/screenshot38.png)

#### References:
1. Ivy, D., 2020. Django (3.0) Crash Course Tutorials | Customer Management App. [video] Available at: <https://www.youtube.com/playlist?list=PL-51WBLyFTg2vW-_6XBoUpE7vpmoR3ztO> [Accessed 1 June 2020].





**James Fisher 2020 © Copyright**
**Under Terms and Agreements of University of Aberdeen and Software distribution**

