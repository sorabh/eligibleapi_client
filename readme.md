testClient.py : From this file we will give all arguments resource Url and parameters to API. This script will create a object of class serviceClient and then call function of that object get_responce with all the parameters.return value of this funtion is a serviceListResponse object.now we can call Print method of class serviceListResponse to print the data.  

serviceClient.py : In this file we have class serviceClient which have function get_request.This function do a get request and extract the json data. and return a object of class serviceListResponse with arg json data.

serviceListResponse.py : this class cantain all the functions which we want to do with data. 
