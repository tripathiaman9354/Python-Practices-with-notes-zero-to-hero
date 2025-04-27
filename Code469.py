import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Aman@321",
  database="mydatabase"
)
mycursor = mydb.cursor()
mycursor.execute("CREATE TABLE product (name VARCHAR(255), id VARCHAR(255))")
sql = "INSERT INTO product (name, id) VALUES (%s, %s)"
val = [
 ('Chocolate Heaven', '154'),
 ('Tasty Lemons', '155'),
 ('Vanilla Dreams', '156'),
]
mycursor.executemany(sql, val)
mydb.commit()
print(mycursor.rowcount, "record was inserted.")
