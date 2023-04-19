import mysql.connector

# Connect to local sql server
MYDB = mysql.connector.connect(
    host="localhost", user="root", passwd="VedNigam1", database="hospital_db")
