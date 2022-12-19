# Gold_Sales_Manger_pythonApp
An application that would allow users to add their Sales daily while it is organized for them daily and monthly while keeping track of their total sold and daily currency exchange rate and gold exchange rate. 




![image](https://user-images.githubusercontent.com/92942235/208384551-f0597a4c-86c3-480b-8793-abb4f0527f56.png)






CSE0408 Programming 3 Project Report
Sales Manager for Gold Sellers


Prepared by: Walid Abdul Hakim
Student no: 1900000480







Table of Contents 

1.	Abstract									 	 pg. 1 
2.	Introduction 									 pg. 1
2.1.	Background 									 pg. 1
2.2.	Project Brief 									 pg. 1
3.	Application Details 									 pg. 2
	3.1 Libraries
3.2 Implementations                       							 
4.	References















1.	Abstract 
For this project, I chose to create an Android application for use on Computers. The purpose of the application was to provide users with the ability to add their sales with a name, product name, weight and price, then use then adds it to the excel sheet while also adding the most current gold price as well as the currency exchange rate between USD and TRY.
2.	Introduction
This report aims to provide a detailed look at how the application was made using python languages with the help of resources from the internet and course materials.
2.1	Background
At the beginning of the project, I had very little experience on python language, so a large portion of time was dedicated to investigating, understanding, and testing smaller bits of functionality, as well as looking at alternative implementations to figure out what I thought worked best. Ultimately, I would end up having to teach myself python application development, mostly relying on my ability to apply the knowledge I accumulated over the class and the internet. As a result, small amount of the code in the application has been inspired by the internet - mostly from answers provided in StackOverflow, as well as various other tutorial sites/videos. I have tried to keep a record for this in the code itself by including comments. 
2.2	Project Brief
 The main goal of this project was to create an application that would allow users to add their Sales daily while it is organized for them daily and monthly while keeping track of their total sold and daily currency exchange rate and gold exchange rate. This application will create a excel file(xlsx) where it would store all the required information. The project will also have a simple UI as it is a simple project.






3.	Application Details
3.1 Libraries 
The libraries that were used in the program are as follows:
1.	Xlsxwriter
This library is used to edit xlsx files as it is need for this project.
2.	Tkinter
His library is used to make the GUI of the app so that it could become usable
3.	Openpyxl
Openpyxl is a Python library that is used to read from an Excel file or write to an Excel file.
4.	Datetime
Is a python library that is used to get the current date and time.

5.	Os
The OS module in python provides functions for interacting with the operating system. OS comes under Python's standard utility modules. This module provides a portable way of using operating system dependent functionality.

6.	Re
The re module provides a set of powerful regular expression facilities, which allows you to quickly check whether a given string matches a given pattern (using the match function), or contains such a pattern (using the search function).

7.	Urllib.request
The urllib. request module defines functions and classes which help in opening URLs (mostly HTTP) in a complex world
8.	Openexchangerate
This is a simple python client implementation of https://openexchangerates.org web service
3.2 Implementation
At the start of the project, we needed to be able to open a xlsx file for adding Sales and its name should be Sales.xlsx and if there were not any it should be able to create one with specific parameters which was handled by the libraries Os and openyxl. I used the write function to change the names of the columns to what was required and also use the set_column function to change the width of the columns to fit the values that were going to be added after the program had taken all the input

 ![image](https://user-images.githubusercontent.com/92942235/208384298-035becae-a790-4328-b487-407399ba0c92.png)



Then we needed to check for the date file which would be used to check the last date the program was used which would influence the program in its next steps. And if there were none it should be able to create the file with the help of the libraries OS and the default python library and store the current date.
 
![image](https://user-images.githubusercontent.com/92942235/208384324-a52db460-67db-4e73-beee-31fdc29fe47c.png)


When both above files are available the program then opens the date file reading it and then checks the xlsx file where if a month had passed or a year it would add the total sold and total weight that was sold and update the date file and lastly it would create a new worksheet with specific parameters. 

![image](https://user-images.githubusercontent.com/92942235/208384343-eaf3f0ff-b968-4847-b451-cbbb83189fc2.png)


Then we would need a function where if the done button were clicked it would take the input of the user check for any error and add it to the xlsx file, it would also add the live gold rate in USD and the currency exchange between USD and TRY.
 
 ![image](https://user-images.githubusercontent.com/92942235/208384369-4f552213-fbe1-4b6d-85e4-2176cd0c05c9.png)

 
When adding the sales, we would also like to get the live gold price and as well as the exchange rate for Turkish Lira were I used a reference and an API to complete this job as it wouldn’t have been completed without them. (functions.py line 1-36) he value I used to get was an ounce of gold where I had to edit a small part and make it into gram.
 
![image](https://user-images.githubusercontent.com/92942235/208384388-e1cacb8e-0a05-43c3-880c-fb5bcf435a01.png)


![image](https://user-images.githubusercontent.com/92942235/208384431-c16f255e-b0ab-4e67-8f70-607ca55233d3.png)


And not to forget the GUI which I had made by trials and errors using the library tkinter where it contained 4 txt boxes to get the user input and one button to add call the clicked function where it would add the required inputs to the xlsx file.








4.	References

a.	https://github.com/Nirajkashyap/live_stock_price/blob/5d226e23fad285d0303838dcf4d46249674ca06a/gold.py
b.	GitHub
c.	YouTube
d.	Stack Overflow - Where Developers Learn, Share, & Build Careers







