import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Kashyap@1100",
    database="adaptive_test"
)

cursor = db.cursor(dictionary=True)