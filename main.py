import dbhelper
from dbhelper import create, insert,remove_vehicle,drop_parking,exit_parking

while True:
    action = int(input("select an option \n1.Create an parking database \n2.Insert the vehicle information \n3.drop_parking \n4.exit_parking \n5.Remove the car from the parking slot \n6.exit \n ::"))
    if action == 1:
      create()
    elif action == 2:
       insert()
    elif action == 3:
       drop_parking()
    elif action == 4:
       exit_parking()
    elif action == 5:
       remove_vehicle()
    else:
       break

