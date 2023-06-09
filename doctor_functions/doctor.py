import connector


DOCTOR_FUNCTIONS = {
    1: "change report status",
    2: "Assign Perscription",
    3: "Patient Info"
}


def perscription(medicineID, reportID, medicineName, value):
    mycursor = connector.MYDB.cursor()

    # IF add perscription
    if value == 'Positive':
            # Execute SQL Statement to add/update/remove new persciption and reportID
            mycursor.execute('INSERT INTO medicine (medicineId, reportId, medicineName) VALUES (%s, %s, %s)',(medicineID, reportID, medicineName))
            connector.MYDB.commit()
            return "Successfully added perscription medicine"
        # IF remove perscription
    if value == 'Neagive':
            # Execute SQL statement to remove perscription from list
            mycursor.execute('DELETE FROM medicine WHERE medicineId = %s AND reportId = %s AND medicineName = %s',(medicineID, reportID, medicineName))
            connector.MYDB.commit()
            return "Successfully removed perscription from medicine"
        

# function by Ved
def changeReportStatus(reportId, newReportStatus):
    mycursor = connector.MYDB.cursor()
    mycursor.execute(
        'UPDATE report SET labResults = %s WHERE reportId = %s', (newReportStatus, reportId))
    connector.MYDB.commit()

    return "successfully updated report status"



def patientInfo():
    mycursor = connector.MYDB.cursor()
    mycursor.execute(
        'SELECT * FROM patientInfoView'
    )
    patients = mycursor.fetchall()
    return patients
