import connector

RECEPTIONIST_FUNCTIONS = {
    1: "view all doctors",
    2: "assign nurse to room",
    3: "",
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
