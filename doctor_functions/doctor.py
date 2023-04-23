import connector

DOCTOR_FUNCTIONS = {
    1: "change report status"
}

# function by Ved
def changeReportStatus():
    mycursor = connector.MYDB.cursor()
    