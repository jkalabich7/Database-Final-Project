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
    employee_first = input("Enter the first name of the employee to delete: ")
    employee_last = input("Enter last name of employee to delete: ")
    employee_query = ( "DELETE FROM driver WHERE firstName = %s AND lastName = %s")
    employee_data = (employee_last, employee_first)
    try:
        employee_cursor = cm_connection.cursor()
        employee_cursor.execute(employee_query, employee_data)
        cm_connection.commit()
        employee_data = (employee_last)
        print("Deleted employee '{} {}' successfully!".format(employee_first, employee_last))
        employee_cursor.close()
    except mysql.connector.Error as err:
        print("\nEmployee not deleted ")
        print("Error {}".format(err))
cm_connection.close()
