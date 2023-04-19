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
    if request.method == 'POST':
        # Check if the username and password are correct
        username = request.form['username']
        password = request.form['password']

        mycursor.execute(
            'SELECT * FROM employee WHERE username = %s AND password = %s', (username, password,))

        # Fetch one record and return result
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
        return render_template('doctor_func.html', action=action)
    else:
        return redirect(url_for('login'))


@app.route('/receptionist/<int:action>')
def receptionists(action):
    if session.get('logged_in'):
        return render_template('receptionist_func.html', action=action)
    else:
        return redirect(url_for('login'))


@app.route('/logout')
def logout():
    session['logged_in'] = False
    return redirect(url_for('login'))


if __name__ == '__main__':
    app.run(debug=True)
