import connector

RECEPTIONIST_FUNCTIONS = {
    1: "view all doctors",
    2: "assign nurse to room"
}

# function by Alaan


def assign_nurse_room(nurse_id, room_number):
    mycursor = connector.MYDB.cursor()

    mycursor.execute('SELECT * FROM nurse WHERE essn = %s', (nurse_id,))
    nurse = mycursor.fetchone()
    if nurse is None:
        return {}

    mycursor.execute('SELECT * FROM room WHERE roomNo = %s', (room_number,))
    room = mycursor.fetchone()
    if room is None:
        return {}

    mycursor.execute('SELECT * FROM nurse WHERE roomID = %s AND essn != %s', (room['roomID'], nurse_id))
    assigned_nurse = mycursor.fetchone()
    if assigned_nurse is not None:
        return {}

    mycursor.execute('UPDATE nurse SET roomID = %s WHERE essn = %s', (room['roomID'], nurse_id))
    connector.MYDB.commit()

    return nurse

# function by Solomon


def view_doctors():
    mycursor = connector.MYDB.cursor()
    mycursor.execute('SELECT * FROM doctorinfoview')
    doctors = mycursor.fetchall()
    return doctors
