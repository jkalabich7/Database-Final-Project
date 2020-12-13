import mysql.connector
from mysql.connector import errorcode

try:
    cm_connection = mysql.connector.connect(
        user="truck_user",
        password="truck",
        host="127.0.0.1",
        database="trucks")

except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Invalid credentials")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Database not found")
    else:
        print("Cannot connect to database:", err)

else:
    question = input("Chose an option: 1 - Truck Information, 2 - Driver Infomation, 3 - Delivery History (Enter 1, 2, or 3): ")
    while question != "1" and question != "2" and question != "3":
        print("Please enter 1, 2, or 3!")
        question = input("Chose an option: 1 - Truck Information, 2 - Driver Infomation, 3 - Delivery History (Enter 1, 2, or 3): ")

    if question == '1':
        truck_cursor = cm_connection.cursor()
        truck_query = "SELECT make, model, nickName, grossVehicleWeight, licenseRequired, maxDistance, VIN FROM truck"
        truck_data = (truck_query, )
        truck_cursor.execute(truck_query,)

        print()
        print("The following is a list of all relevant truck information:")
        print('-' * 40)
        for row in truck_cursor.fetchall():
            print("Make:{}, Model:{}, Nick Name:{}, Gross Vehicle Weight: {}lbs, License Needed: {}, Maximum Distance: {} miles, VIN: {}".format(row[0], row[1], row[2], row[3], row[4], row[5], row[6]))
        truck_cursor.close()
        cm_connection.close()

    elif question == '2':
        driver_cursor = cm_connection.cursor()
        driver_query = "SELECT firstName, lastName, startDate, superiorLicense, languages, shift FROM driver"
        driver_data = (driver_query,)
        driver_cursor.execute(driver_query, )
        print()
        print("The following is a list of all relevant driver information:")
        print('-' * 40)
        for row in driver_cursor.fetchall():
            print(
                "Name: {} {}, Hire Date: {}, License Endorsements: {}, Languages: {}, Shift: {} ".format(row[0], row[1], row[2], row[3], row[4], row[5]))
        driver_cursor.close()
        cm_connection.close()

    elif question == '3':
        delivery_cursor = cm_connection.cursor()
        delivery_query = "SELECT firstName, lastName, make, model, deliveryAddress, deliveryDate FROM driver INNER JOIN truckdriver ON driver.driverId=truckdriver.driverID INNER JOIN truck ON truck.truckId=truckdriver.driverId;"
        delivery_data = (delivery_query,)
        delivery_cursor.execute(delivery_query, )
        print()
        print("The following is a list of all recorded deliveries:")
        print('-' * 40)
        for row in delivery_cursor.fetchall():
            print(
                "'{} {}' used the '{} {}' to deliver to '{}' on '{}' ".format(row[0], row[1], row[2], row[3], row[4], row[5]))
        delivery_cursor.close()
        cm_connection.close()


