import connector

RECEPTIONIST_FUNCTIONS = {
    1: "view all doctors",
    2: "assign nurse to room"
}

# function by Alaan


def assign_nurse_room(nurse_id, room_number):
    mycursor = MYDB.cursor()
    mycursor.execute('SELECT * FROM employee WHERE essn = %s', (nurse_id,))
    nurse = mycursor.fetchone()
    if nurse is None:
        return {}

    mycursor.execute(
        'SELECT * FROM room WHERE room_number = %s', (room_number,))
    room = mycursor.fetchone()
    if room is None:
        return {}

    mycursor.execute(
        'SELECT * FROM room_assignment WHERE room_number = %s AND checkout_date IS NULL', (room_number,))
    current_assignment = mycursor.fetchone()
    if current_assignment is not None:
        return {}

    mycursor.execute(
        'INSERT INTO room_assignment (room_number, nurse_id, checkin_date) VALUES (%s, %s, NOW())', (room_number, nurse_id))
    MYDB.commit()
    return nurses

# function by Solomon


def view_doctors():
    mycursor = connector.MYDB.cursor()
    mycursor.execute('SELECT * FROM doctorinfoview')
    doctors = mycursor.fetchall()
    return doctors
