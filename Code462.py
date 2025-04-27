import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Aman@321",
  database="mydatabase"
)
mycursor = mydb.cursor()
sql = "DROP TABLE customers"
mycursor.execute(sql)
#If this page was executed with no error(s), you have successfully deleted the "customers" table.
