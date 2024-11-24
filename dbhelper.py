import datetime
import sqlite3
conn = sqlite3.connect("data2.db")
mycursor = conn.cursor()

def create():
    mycursor.execute(
    """
    create table parking_slot
    (
    vehicle_number integer primary key autoincrement,
    driver_name text,
    vehicle_type text not null,
    parking_start text not null,
    parking_exit text,
    price float
    ) 
     
       """)
    conn.commit()

def insert():
    this_name = input("Enter  drivers_name: ")
    while True:
        print("Enter Vehicle type: \n 1. Two wheeler \n 2. Four wheeler")
        type = int(input("The type Vehicle is :"))
        if type == 1:
              this_type = "Two wheeler"
              break
        elif type == 2:
              this_type = "Four wheeler"
              break
        else:
              print("Invalid Entry.")
    
    time = datetime.datetime.now()
    mycursor.execute("INSERT INTO parking_slot(driver_name,Vehicle_type,parking_start) values(?,?,?)",(this_name,this_type,time))
    conn.commit()
    id = input("Enter the vehicle number  :")
    mycursor.execute("select * from parking_slot where vehicle_number = ?",id)
    rows = mycursor.fetchall()
    file = input("Enter the name of the file with extension")
    ftr = open(file, "w")
    for row in rows:
                    ftr.write(f"id : { row[0]}")
                    ftr.write(f"\n Driver's Name: {  row[1]}")
                    ftr.write(f" \n Vehicle Type: {  row[2]}")
                    ftr.write(f"\n Start Time : {  row[3]}")


def remove_vehicle():
        number = input("where do you wanna delete data from(id) : ")
        mycursor.execute("delete from parking_slot where vehicle_number = ?", number)
        conn.commit()

def drop_parking():
      mycursor.execute("drop table if exits parking_slot")
      conn.commit()
      print("The table id sucessfully dropped.")

def exit_parking():
      a = input("Enter the vehicle id that is exiting: ")
      exit_time = datetime.datetime.now()
      mycursor.execute("update parking_slot set parking_exit = ? where  vehicle_number = ?", (exit_time,a))
      conn.commit()
      mycursor.execute("select parking_start from parking_slot where vehicle_number = ? ",a)
      rows = mycursor.fetchall()
      startingtime  = rows[0][0]
      format = '%Y-%m-%d %H:%M:%S.%f'
      start_time = datetime.datetime.strptime(startingtime, format)
      time_interval = exit_time - start_time
      total_seconds = int(time_interval.total_seconds())
      h, remainder = divmod(total_seconds, 3600)
      m, _ = divmod(remainder, 60)
      price = 0
      if h== 0 and m >= 0 or h == 1 and m ==0 :
             price = 10
      elif h > 1 :
            Additional_hour = h - 1
            price = 10 + 5* Additional_hour
            if min >= 0:
                   price += 5
      print("Your total fare is :", price)
      print("The total time the vehicle stayed in the parking lot is ", time_interval)
      mycursor.execute("update parking_slot set price = ? where  vehicle_number = ?", (price,a))
      conn.commit()
      


# def display():
#         mycursor.execute("select * from parking_slot")
#         rows = mycursor.fetchall()
#         for row in rows:
#               print(row)


       


        
