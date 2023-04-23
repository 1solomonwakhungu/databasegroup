import connector

RECEPTIONIST_FUNCTIONS = {
    1: "view all doctors",
    2: "assign nurse to room"
}

def assign_nurse_room();

# function by Solomon
def view_doctors():
    mycursor = connector.MYDB.cursor()
    mycursor.execute('SELECT * FROM doctorinfoview')
    doctors = mycursor.fetchall()
    return doctors
