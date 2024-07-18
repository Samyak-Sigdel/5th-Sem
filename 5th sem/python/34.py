import mysql.connector
mydb = mysql.connector.connect(
host="localhost",
user="root",
password="",
 database="Database"
)

mycursor = mydb.cursor()
sql = "DELETE FROM Customer WHERE address = %s"
adr = ("Gokarna", )

mycursor.execute(sql, adr)
mydb.commit()
print (mycursor.rowcount, "record(s) deleted")
