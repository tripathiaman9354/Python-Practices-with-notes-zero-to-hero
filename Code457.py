import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Aman@321",
  database="mydatabase"
)
mycursor = mydb.cursor()
sql = "SELECT * FROM customers WHERE address = %s"
adr = ("Lowstreet 4", )
mycursor.execute(sql, adr)
myresult = mycursor.fetchall()
for x in myresult:
  print(x)
