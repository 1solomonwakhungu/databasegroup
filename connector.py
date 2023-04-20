import mysql.connector

# Connect to local sql server
try:
    MYDB = mysql.connector.connect(
        host="localhost", user="root", passwd="VedNigam1", database="hospital_db")
except KeyboardInterrupt:
    exit()
except Exception as e:
    print(e)
# Execute statement and only get one result
