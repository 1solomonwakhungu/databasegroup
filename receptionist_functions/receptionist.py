import random
import connector

import mysql.connector

# Connect to local sql server
try:
    MYDB1 = mysql.connector.connect(
        host="localhost", user="root", passwd="VedNigam1", database="hospital_db")
except KeyboardInterrupt:
    exit()
except Exception as e:
    print(e)
# Execute statement and only get one result


RECEPTIONIST_FUNCTIONS = {
    1: "view all doctors",
    2: "assign nurse to room",
    3: "create appointment",
    4: "view all nurses",
}

# function by Alaan


def assign_nurse_room(nurse_id, room_number):
    mycursor = connector.MYDB.cursor()

    mycursor.execute(
        'UPDATE nurse SET roomId = %s WHERE essn = %s', (room_number, nurse_id))
    connector.MYDB.commit()

    return {'success': True, 'message': 'Nurse assigned to room'}

# function by Solomon


def view_doctors():
    mycursor = connector.MYDB.cursor()
    mycursor.execute('SELECT * FROM doctorinfoview')
    doctors = mycursor.fetchall()
    return doctors

# function by Solomon


def view_nurses():
    mycursor = connector.MYDB.cursor()
    mycursor.execute(
        'SELECT firstname, lastname, departmentName, roomId, reportId FROM department, nurse, employee WHERE department.departmentId = nurse.departmentId AND nurse.essn = employee.essn')
    nurses = mycursor.fetchall()
    return nurses

def create_appointment(date, time):
    mycursor = MYDB1.cursor()
    appointmentID = str(random.randint(0, 99999)).zfill(5) # generate a 5 digit random appointment ID
    sql_query = "INSERT INTO appointment (appointmentID, date, time) VALUES (%s, %s, %s)"
    appointment_data = (appointmentID, date, time)
    mycursor.execute(sql_query, appointment_data)
    MYDB1.commit()
    return {'message' : 'added appointment'}