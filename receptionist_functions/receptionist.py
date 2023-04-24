import connector

RECEPTIONIST_FUNCTIONS = {
    1: "view all doctors",
    2: "create an appointment",
}


# function by Solomon
def view_doctors():
    mycursor = connector.MYDB.cursor()
    mycursor.execute('SELECT * FROM doctorinfoview')
    doctors = mycursor.fetchall()
    return doctors


# function by Ajay
def create_appointment(patient_id, doctor_id, appointment_date, appointment_time):
    mycursor = connector.MYDB.cursor()
    sql_query = "INSERT INTO appointment (patient_id, doctor_id, appointment_date, appointment_time) VALUES (%s, %s, %s, %s)"
    appointment_data = (patient_id, doctor_id,
                        appointment_date, appointment_time)
    try:
        mycursor.execute(sql_query, appointment_data)
        mycursor.MYDB.commit()
    except Exception as e:
        return {"message": "Error creating appointment"}
    return {"message": "Appointment created successfully"}
