from flask import Flask, render_template, request, redirect, url_for, session, jsonify
from connector import MYDB
import receptionist_functions.receptionist as receptionist
import doctor_functions.doctor as doctor

app = Flask(__name__, static_url_path='',
            static_folder='./static',
            template_folder='./templates')
app.secret_key = 'QB*&jy1MlTK@aA#gn&OEG*m4zzUk4F'

mycursor = MYDB.cursor()


@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')

    if request.method == 'POST':
        # Check if the username and password are correct
        username = request.form['username']
        password = request.form['password']

        mycursor.execute(
            "SELECT * FROM employee WHERE username = '%s' AND password = '%s'" % (username, password))

        account = mycursor.fetchone()

        print("[*] LOGIN:", username, password)
        if account:
            session['logged_in'] = True
            # session['username'] = account['username']
            return redirect(url_for('home'))
        else:
            return render_template('login.html', error='Invalid username or password')
    else:
        return render_template('login.html')


@app.route('/home')
def home():
    if session.get('logged_in'):
        doctor_func = doctor.DOCTOR_FUNCTIONS
        recept_func = receptionist.RECEPTIONIST_FUNCTIONS

        context = {
            'doctor_func': doctor_func,
            'recept_func': recept_func,
        }
        return render_template('home.html', context=context)
    else:
        return redirect(url_for('login'))


@app.route('/doctor/<int:action>', methods=['GET', 'POST'])
def doctors(action):
    if session.get('logged_in'):
        action_name = ""
        data = {}

        if request.method == 'POST':
            # other fucnitons go here as if statments of action == number
            if action == 1:
                action_name = "Report Status"
                reportID = request.form["reportId"]
                newReportStatus = request.form["newReportStatus"]
                data = doctor.changeReportStatus(reportID, newReportStatus)

            if action == 2:
                action_name = "Assign Perscription"
                reportID = request.form['report_id']
                medicineName = request.form['medicine_name']
                value = request.form['submit']
                data = doctor.perscription(reportID, medicineName, value)
            else:
                if action == 3:
                    action_name = "Patient Info"
                    data = doctor.patientInfo()
                # Function 3 Here
            # Information passed to the html template
        context = {
            'action_name': action_name,
            'action': action,
            'data': data
        }
        return render_template('doctor_func.html', context=context)
    else:
        return redirect(url_for('login'))


@app.route('/receptionist/<int:action>', methods=['GET', 'POST'])
def receptionists(action):
    if session.get('logged_in'):
        action_name = ""
        data = {}

        if request.method == 'POST':
            if action == 2:
                nurse_id = request.form['nurse_id']
                room_number = request.form['room_number']
                result = receptionist.assign_nurse_room(nurse_id, room_number)

                context = {
                    'action_name': "assign nurse to room",
                    'action': 2,
                    'data': result,
                }
                return render_template('receptionist_func.html', context=context)
                # return redirect(url_for('receptionists', action=2))
            if action == 3:
                date = request.form['date']
                time = request.form['time']
                data = receptionist.create_appointment(
                    date, time)
                data = jsonify(data)            
                context = {
                    'action_name': "create appointment",
                    'action': 3,
                    'data': data,
                }
                return render_template('receptionist_func.html', context=context)
        else:
            match action:
                case 1:
                    action_name = "view all doctors"
                    data = receptionist.view_doctors()
                case 2:
                    action_name = "assign nurse to room"
                case 4:
                    action_name = "view nurses"
                    data = receptionist.view_nurses()

            # Information passed to the html template
            context = {
                'action_name': action_name,
                'action': action,
                'data': data,
            }
            return render_template('receptionist_func.html', context=context)

    else:
        return redirect(url_for('login'))


@app.route('/logout')
def logout():
    session['logged_in'] = False
    return redirect(url_for('login'))


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html')


if __name__ == '__main__':
    app.run(debug=True)
