import connector

mycursor = connector.MDBY.mycursor()

DOCTOR_FUNCTIONS = {
    1: "action1",
    2: "Assign Perscription",
}


def perscription(reportID, medicineName, value):
    #get medicine ID from table if it exists
    mycursor.execute('SELECT medicineid WHERE medicinename = %s', (medicineName))
    medicineID = mycursor.fetchone()
    #fetch any existing rows that already have a medicine name attched to the Report ID
    mycursor.execute('SELECT * FROM medicine WHERE reportID = %s, medicineName = %s', (reportID, medicineName))
    medicine = mycursor.fetchone()
    #check if medicine name already exisits in the report ID
    if medicine['reportID'] == reportID & medicine['medicineName'] == medicineName :
        return("Medicine already exists for report ID: %s" , (reportID))
    else: 
        ##IF add perscription
        if value == 'Positive':
            ##Execute SQL Statement to add/update/remove new persciption and reportID
            mycursor.execute('INSERT INTO medicine (medicineID, reportID, medicineName) VALUES (%s, %s, %s)', (medicineID, reportID, medicineName))
            return("Successfully added perscription to patient report ID: %s" , (reportID))
        ##IF remove perscription
        elif value == 'Neagive':
                ##Execute SQL statement to remove perscription from list
                mycursor.execute('DELETE FROM medicine WHERE medicineID = %s AND reportID = %s AND medicineName = %s', (medicineID, reportID, medicineName))
                return("Successfully removed medicine from patient reportID: %s" , (reportID))
        elif value == 'view':
            return(mycursor.execute('SELECT * FROM medicine'))

#def patientInfo():
    #Request patient name/id
#    patientName = 
#    patientID = 