import mysql.connector
from mysql.connector imort errorcode

try:
    cm_connection = mysql.connector.connect(
        user="JakesB",
        password="pyuser5134",
        host="127.0.0.1",
        database="classicmodels")

except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Invalid credentials")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Database not found")
    else:
        print("Cannot connect to database:", err)

else:
    print("Success")
    cm_connection.close()
