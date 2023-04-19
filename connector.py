import mysql.connector

# Connect to local sql server
try:
    MYDB = mysql.connector.connect(
        host="localhost", user="root", passwd="VedNigam1", database="hospital_db")
    mycursor = MYDB.cursor()
except KeyboardInterrupt:
    exit()
except Exception as e:
    print(e)
# Execute statement and only get one result


def fetch_one(sql_statement):
    mycursor.execute(sql_statement)
    return mycursor.fetchone()


def fetch_all(sql_statement):
    mycursor.execute(sql_statement)
    return mycursor.fetchall()
