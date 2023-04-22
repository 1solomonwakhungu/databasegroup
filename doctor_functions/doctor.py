from pickle import FALSE
import connector


#DOCTOR_FUNCTIONS:
#    1: "assign prescription"
#    2: "get patient information"
#    3: "go to room"
#    4: "example function"


methods=['PERSCRIPTION', 'PATIENT', 'ROOM']
def Doctor():
    if request.method == 'PERSCRIPTION':
        perscription()
    elif request.method == 'PATIENT':
        patientInfo()
    elif request.method == 'ROOM':
        roomInfo()

def perscription():
    ##Initialize values for add and remove prescriptions
    addPerscrip = False
    removePerscrip = False
    ##Check input
    medicineID = request.form['medicineID']
    reportID = request.form['reportID']
    medicineName = request.form['medicineName']

    ##check if medicine already exisits in table
    mycursor.execute('SELECT * FROM medicine WHERE medicineID = %s, medicineName = %s', (medicineID, medicineName))
    medicine = mycursor.fetchone()
    if medicine[medicineID] == medicineID & medicine[medicineName] == medicineName :
        print("Data already exists in table")
        perscription()
    

    ##IF add perscription
    if addPerscrip == True:
        ##Execute SQL Statement to add/update/remove new persciption and reportID
        mycursor.execute('INSERT INTO medicine (medicineID, reportID, medicineName) VALUES (%s, %s, %s)', (medicineID, reportID, medicineName))
    ##IF remove perscription
    elif removePerscrip == True:
            ##Execute SQL statement to remove perscription from list
            mycursor.execute('DELETE FROM medicine WHERE medicineID = %s AND reportID = %s AND medicineName = %s', (medicineID, reportID, medicineName))

def patientInfo():
    ##Request patient name/id
    patientName = request.form['patientName']
    patientID = request.form['patientID']

def roomInfo():
    ##Request room info?
    roomNo = request.form['roomNo']