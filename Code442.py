import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Aman@321"
)
mycursor = mydb.cursor()
mycursor.execute("CREATE DATABASE mydatabase")
#If this page is executed with no error, you have successfully created a database.
