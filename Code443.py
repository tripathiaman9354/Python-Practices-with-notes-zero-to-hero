import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Aman@321"
)
mycursor = mydb.cursor()
mycursor.execute("SHOW DATABASES")
for x in mycursor:
  print(x)
