# CRUD operations by using fast api

CRUD = Create , Read , Update , Delete

In this project , i have used fastapi to implement CRUD operations on addressbook with sqlite(ORM) database to store the address along with the coordinates 
i.e latitude and longitude of the user address .
i have used fastapi swagger doc for implementing and checking the CRUD operations
Inside the projects , coordinates are also validated by using the logic i.e ( -90 > latitude < +90 and -180 > longitude < +180 )
There is another route in this project where we can get all the coordinates with in a given distance from the given coordinates by using haversine formula which 
you can find in distance file
you can find the table and colummn structure in models used to create table in sql database

you should have python 3.7 and pip installed to run the project locally

To start or run the project:
=> After cloning the respository into local machine first run the command "pip install -r requirements.txt" . this will install all requirements needed to run the 
   project locally
=> Next start the server by using the command "uvicorn main:app --reload" . Here main is the name of main file , app is the name of instance of fastapi created in 
   main file and --reload is using so that server restarts automatically for any changes
=> Now open the localhost:8000/docs on your browser and you should see the CRUD operation ..Try them out play with it  
