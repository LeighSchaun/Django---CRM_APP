import mysql.connector

database = mysql.connector.connect(
    host='localhost',
    user='root',
    password='bu$yLion72'
)

cursorObject = database.cursor()

cursorObject.execute("CREATE DATABASE leigh")

print("All Done")
