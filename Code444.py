import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Aman@321",
  database="mydatabase"
)
#If this page is executed with no error, the database "mydatabase" exists in your system

