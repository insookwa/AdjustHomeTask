# AdjustHomeTask
This is a system to serve data through a dynamic API . The main project file is name dispensor .  Link to task: https://gist.github.com/kotik-adjust/4883e33c439db6de582fd0986939045c


## About the API 
The API has one end point but with  multiple functionalities . You can choose what you want to do by changing the operation and oher variables acoording to the documentation 

### Uploading a csv file 
uploading a file handld by data app . the endpoint to upload a file is http://127.0.0.1:8000/data/upload/

### Filter by Date Range 
Please indicate the start date and the end date in the API  . the endpoint to filter by date range is for example   http://127.0.0.1:8000/adjust/?operation=filterByDater&fromDate=2017-05-17&toDate=2017-05-20 . The operation variable is 'filterByDater', start date variable  is fromDate and end date variable is toDate. 

### Filter by Date 
This is to get data of a according to a given date .  the endpoint to filter by date is fo example   http://127.0.0.1:8000/adjust/?operation=filterByDate&date=2017-05-17 . The operation variable is filterByDate . the date variable indicates the date for the desired data. 


### Filter by channel
This Gets data filtered by channel . The operation variable of this filterBychanne for example http://127.0.0.1:8000/adjust/?operation=filterBychannel&channel=adcolony . Indicate the desired channel by adding &channel=.

### Filter by countries 
Example : http://127.0.0.1:8000/adjust/?operation=filterBycountries&country=US <br>
operation variable : filterBycountries, <br>
country varable : country= , <br>

### Filter By Os 
Example : http://127.0.0.1:8000/adjust/?operation=filterbyOs&os=ios <br>
Operation variable : filterbyOs , <br>
os variable: os= , <br>

### Filter By Os 
Example : http://127.0.0.1:8000/adjust/?operation=groupbyChannel <br>
Operation : groupbyChannel <br>

### Filtter By by column in ascending or descending order 
Example: http://127.0.0.1:8000/adjust/?operation=sortColumn&sortBy=asc&orderBy=clicks <br>
Operation Variable : sortColumn <br>
filter by a given colum using the 'orderBy=' variable  <br>
State the arrangemnt order using 'sortBy=' variable.  'sortBy=asc' for ascending order and 'sortBy=dsc' for decending order <br>

### Show the number of impressions and clicks that occurred on a given date , broken down by channel and country, sorted by clicks in descending order
Example: http://127.0.0.1:8000/adjust/?operation=alpha&toDate=2017-05-22 <br>
Operation variable:alpha <br>
Date variable : toDate <br>

### Show the number of installs that occurred on a given date and OS , broken down by date, sorted by date in ascending order
Example: http://127.0.0.1:8000/adjust/?operation=beta&date=2017-05-17&os=ios <br>
Operation variable: beta,  <br>
Date Vaiable : date,  <br>
OS variable: os,  <br>

### Show revenue, earned a given date , country , broken down by operating system and sorted by revenue in descending order.

Example: http://127.0.0.1:8000/adjust/?operation=gamma&date=2017-05-17&country=US&os=ios <br>
Operation variable:gamma <br>
Date Variable : date , <br>
Country variable : country, <br>
OS variable : os  <br>

### Show CPI and spend for a given country  broken down by channel ordered by CPI in descending order. 
Operation Variable : omicron <br>
This is Still in development  <br>

## DEVELOPMENT PART 

### Techologies Used . 
The project is in Django framework and all the packages used are in the requirements.txt file . they can be installed with <pip install -r requirements.txt> <br>
The virtual environment file is name venv 
  
#### Database 
The syste is designed to work with mysql database . Please create a dataase called dispensor , and in the settings file , add the username and password for sucessfull database connection 

Start the server with python3 manage.py runserver , Use the API to upload the csv which is found here : https://gist.github.com/kotik/3baa5f53997cce85cc0336cb1256ba8b/#file-dataset-csv-L10
  
#### Models 
  
  
The System has two apps one called Data and the other handler <b>
data.models is the main model of the whole system , <b>

#### Views 

data.views had code that handles uploading the csv to the database<b>
handler.vews handles api calls and the rest of the operations<b>

#### Serializers 

data.serializers handles the serialization for uploading csv file to the system <b>
handler.serializer handles all serializing of all the api calls <b>


  


  
  
  
 
  













