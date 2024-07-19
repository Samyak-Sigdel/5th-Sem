import csv
import mysql.connector

# Connect to the MySQL database
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="Database"
)

mycursor = mydb.cursor()

# Read the CSV file
try:
    with open('students.csv', mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            name = row['Name']
            if name.startswith('S') or name.startswith('J'):
                sql = "INSERT INTO 'table' (name) VALUES (%s)"
                val = (name,)
                mycursor.execute(sql, val)

    # Commit the transaction
    mydb.commit()
    print(mycursor.rowcount, "record(s) inserted.")
except FileNotFoundError as e:
    print(f"Error: {e}")

# Close the cursor and the connection
mycursor.close()
mydb.close()
