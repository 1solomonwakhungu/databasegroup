import connector

RECEPTIONIST_FUNCTIONS = {
    1: "view all doctors",
}


# function by Solomon
def view_doctors():
    mycursor = connector.MYDB.cursor()
    mycursor.execute('SELECT * FROM doctorinfoview')
    doctors = mycursor.fetchall()
    return doctors
