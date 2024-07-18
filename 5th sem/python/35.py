import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="Database"
)

mycursor = mydb.cursor()
sql = "UPDATE Customer SET address = %s WHERE address = %s"
val = ("Gokarna", "Pulchowk")

mycursor.execute(sql, val)
mydb.commit()
print(mycursor.rowcount, "record(s) affected")
