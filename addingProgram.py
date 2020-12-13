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
    add_employee = input("Would you like to add a new employee? (Y/N): ")
    while add_employee != "Y" and add_employee != "N":
        print("Please enter Y or N!")
        add_employee = input("Would you like to add a new employee?(Y/N): ")

    if add_employee != "Y":
        print("Thanks for using my program!")
    else:
        employee_first = input("Enter new employee first name: ")
        employee_last = input("Enter new employee last name: ")
        employee_start = input("Enter date (i.e. YYYY-MM-DD): ")
        employee_license = input("Enter highest license (A, B, C, D, CDL): ")
        employee_languages = input("Enter the employees languages (English, English-Spanish): ")
        employee_shift = input("Will this employee work shift 1 or shift 2?: ")
        employee_query = "INSERT INTO driver (firstName, lastName, startDate, superiorLicense, languages, shift) VALUES (%s, %s, %s, %s, %s, %s)"
        employee_data = (employee_first, employee_last, employee_start, employee_license, employee_languages, employee_shift)

        try:
            employee_cursor = cm_connection.cursor()
            employee_cursor.execute(employee_query, employee_data)
            cm_connection.commit()
            print("Update Successful")
            employee_cursor.close()
        except mysql.connector.Error as err:
            print("\nEmployee not added")
            print("Error: {}".format(err))

        cm_connection.close()

