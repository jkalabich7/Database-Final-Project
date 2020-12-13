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
    truck_cursor = cm_connection.cursor()
    truck_query = "SELECT firstName, lastName, superiorLicense FROM driver WHERE superiorLicense = %s"
    license_desired = input("Which endorsement is necessary for this delivery? (A, B, C, D, or CDL): ")
    license_data = (license_desired, )
    truck_cursor.execute(truck_query, license_data)

    print()
    print("The following employees have a '{}' endorsement and can and take the delivery:".format(license_desired))
    print('-'*40)
    for row in truck_cursor.fetchall():
        print("{} {} has a {} endorsement.".format(row[0], row[1], row[2]))

    truck_cursor.close()
    cm_connection.close()