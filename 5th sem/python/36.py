import mysql.connector
mydb = mysql.connector.connect( 
    host="localhost", 
    user="root",
    password="",
    database="Database"
)
mycursor = mydb.cursor()
sql = "SELECT * FROM Customer WHERE address = %s"
adr=("Gokarna", )
mycursor.execute(sql, adr)
myresult = mycursor.fetchall()
for x in myresult:
    print(x)
