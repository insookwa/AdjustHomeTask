# AdjustHomeTask
This is a system to serve data through a dynamic API . Link to task: https://gist.github.com/kotik-adjust/4883e33c439db6de582fd0986939045c

## About the API 
The API has one end point but with  multiple functionalities . You can choose what you want to do by changing the operation and oher variables acoording to the documentation 

### Uploading a csv file 
uploading a file handld by data app . the endpoint to upload a file is http://127.0.0.1:8000/data/upload/

### Filter by Date Range 
Please indicate the start date and the end date in the API  . the endpoint to filter by date range is for example   http://127.0.0.1:8000/adjust/?operation=filterByDater&fromDate=2017-05-17&toDate=2017-05-20 . The operation variable is 'filterByDater', start date variable  is fromDate and end date variable is toDate. 

### Filter by Date 
This is to get data of a according to a given date .  the endpoint to filter by date is fo example   http://127.0.0.1:8000/adjust/?operation=filterByDate&date=2017-05-17 . The operation variable is filterByDate . the date variable indicates the date for the desired data. 









