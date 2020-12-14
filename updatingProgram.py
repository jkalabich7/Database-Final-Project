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
    employee_first = input("Enter employee first name: ")
    employee_last = input("Enter employee last name: ")

    column = input("Enter item to update (firstName, lastName, startDate, superiorLicense, or languages): ")
    prompt = "Enter new value for {}: ".format(column)
    value = input(prompt)

    employee_query = ("Update driver SET " + column + "= %s WHERE firstName = %s AND lastName = %s")
    employee_data = (value, employee_first, employee_last)

try:
    truck_cursor = cm_connection.cursor()
    truck_cursor.execute(employee_query, employee_data)
    cm_connection.commit()
    print("Update Successful")
    truck_cursor.close()
except mysql.connector.Error as err:
    print("\nEmployee not updated")
    print("Error: {}".format(err))

cm_connection.close()

