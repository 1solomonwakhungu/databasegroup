from flask import Flask, render_template, request, redirect, url_for, session, jsonify
from connector import MYDB
import mysql.connector

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

        sql = "SELECT * FROM employee WHERE username = '%s' AND password = '%s'" % (
            username, password)
        mycursor.execute(
            "SELECT * FROM employee WHERE username = '%s' AND password = '%s'" % (username, password))

        account = mycursor.fetchone()

        print(sql)
        print(username, password, account)
        if account:
            session['logged_in'] = True
            # session['username'] = account['username']
            return redirect(url_for('home'))
        else:
            return render_template('login.html', error='Invalid username or password')
    else:
        return render_template('login.html')


@app.route('/updatePass', methods=['GET', 'POST'])
def update():
    conn = mysql.connector.connect(
        host="localhost", user="root", passwd="VedNigam1", database="hospital_db")
    if request.method == 'GET':
        return render_template('update.html')

    if request.method == 'POST':
        # Check if the username and password are correct
        username = request.form['username']
        password = request.form['password']

        # db_cursor = MYDB.cursor()
        sql = f"UPDATE employee SET password = '{password}' WHERE username = '{username}'"
        conn.autocommit = True
        mycursorr = conn.cursor()
        values = (username, password)
        mycursorr.execute(sql)

        print(sql)

        return render_template('update.html', error='Password Not Updated')
    else:
        return render_template('update.html')


@app.route('/home', methods=['GET', 'POST'])
def home():
    if session['logged_in'] == True:
        return render_template('home.html')
    return redirect(url_for('login'))


if __name__ == '__main__':
    app.run(debug=True)
