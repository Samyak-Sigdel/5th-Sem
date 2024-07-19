import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="database"
)

mycursor = mydb.cursor()
sql = "INSERT INTO `table` (name, address) VALUES (%s, %s)"
val = ("Unisha", "Thimi")
mycursor.execute(sql, val)
mydb.commit()
print(mycursor.rowcount, "record inserted.")
