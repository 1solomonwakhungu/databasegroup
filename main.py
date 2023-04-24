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

        mycursor.execute('SELECT * FROM employee WHERE username = %s AND password = %s', (
            username, password,))

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


@app.route('/doctor/<int:action>')
def doctors(action):
    if session.get('logged_in'):
        action_name = ""
        data = {}
        match action:
            case 1:
                action_name = "change report status"
                data = doctor.changeReportStatus()
            case _:
                action_name = ""

        # Information passwed to the html template
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

        match action:
            case 1:
                action_name = "view all doctors"
                data = receptionist.view_doctors()
            case 2:
                action_name = "example"
            case _:
                action_name = ""

        # Information passed to the html template
        context = {
            'action_name': action_name,
            'action': action,
            'data': data,
        }
        return render_template('receptionist_func.html', context=context)

        if request.method == 'POST':
            if action == 2:
                nurse_id = request.form['nurse_id']
                room_number = request.form['room_number']
                result = receptionist.assign_nurse_room(nurse_id, room_number)
                return redirect(url_for('receptionists', action=2))
        else:
            match action:
                case 1:
                    action_name = "view all doctors"
                    data = receptionist.view_doctors()
                case 2:
                    action_name = "assign nurse to room"

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
