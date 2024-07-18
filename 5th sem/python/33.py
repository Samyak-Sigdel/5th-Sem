import mysql.connector

mydb = mysql.connector.connect(
host="localhost",
user="root",
password="",
 database="Database"
)
mycursor = mydb.cursor()
sql="INSERT INTO Customer (name, address) VALUES (%s, %s)"
val = ("Ram", "Pulchowk")
mycursor.execute(sql, val)
mydb.commit()
print(mycursor.rowcount, "record inserted.")
