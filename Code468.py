import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Aman@321",
  database="mydatabase"
)
mycursor = mydb.cursor()
mycursor.execute("CREATE TABLE person (name VARCHAR(255), fav VARCHAR(255))")
sql = "INSERT INTO person (name, fav) VALUES (%s, %s)"
val = [
 ('John', '154'),
 ('Peter', '154'),
 ('Amy', '155'),
 ('Hannah', ''),
 ('Michael', ''),
]
mycursor.executemany(sql, val)
mydb.commit()
print(mycursor.rowcount, "record was inserted.")