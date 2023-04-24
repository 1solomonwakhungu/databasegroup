import connector

RECEPTIONIST_FUNCTIONS = {
    2: "create an appointment",
}
# function by Ajay
def create_appointment(patient_id, doctor_id, appointment_date, appointment_time):
    mycursor = connector.MYDB.cursor()
    sql_query = "INSERT INTO appointment (patient_id, doctor_id, appointment_date, appointment_time) VALUES (%s, %s, %s, %s)"
    appointment_data = (patient_id, doctor_id, appointment_date, appointment_time)
    mycursor.execute(sql_query, appointment_data)
    connector.MYDB.commit()
    print("Appointment created successfully!")