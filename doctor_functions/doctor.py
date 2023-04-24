import connector


DOCTOR_FUNCTIONS = {
    1: "change report status",
    2: "Assign Perscription",
    3: "Patient Info"
}


def perscription(reportID, medicineName, value):
    mycursor = connector.MYDB.cursor()
    # get medicine ID from table if it exists
    mycursor.execute(
        'SELECT medicineId FROM medicine WHERE mediciNename = %s', (medicineName))
    medicineID = mycursor.fetchone()
    medicineID = medicineID['medicineId']

    # fetch any existing rows that already have a medicine name attched to the Report ID
    mycursor.execute(
        'SELECT * FROM medicine WHERE reportId = %s, medicineName = %s', (reportID, medicineName))
    medicine = mycursor.fetchone()

    # check if medicine name already exisits in the report ID
    if medicine['reportId'] == reportID & medicine['medicineName'] == medicineName:
        return ("Medicine already exists for report ID: %s", (reportID))
    else:
        # IF add perscription
        if value == 'Positive':
            # Execute SQL Statement to add/update/remove new persciption and reportID
            mycursor.execute('INSERT INTO medicine (medicineId, reportId, medicineName) VALUES (%s, %s, %s)',
                             (medicineID, reportID, medicineName))
            return ("Successfully added perscription to patient report ID: %s", (reportID))
        # IF remove perscription
        elif value == 'Neagive':
            # Execute SQL statement to remove perscription from list
            mycursor.execute('DELETE FROM medicine WHERE medicineId = %s AND reportId = %s AND medicineName = %s',
                             (medicineID, reportID, medicineName))
            return ("Successfully removed medicine from patient reportID: %s", (reportID))
        elif value == 'view':
            return (mycursor.execute('SELECT * FROM medicine'))

# function by Ved


def changeReportStatus():
    mycursor = connector.MYDB.cursor()

# def patientInfo():
    # Request patient name/id
#    patientName =
#    patientID =
