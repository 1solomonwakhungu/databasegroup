from flask import Flask, render_template, request, redirect, url_for, session, jsonify
from connector import MYDB

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
        username = request.values.get('username')
        password = request.values.get('password')

        mycursor.execute(
            "SELECT * FROM employee WHERE username = '%s' AND password = '%s'" % (username, password))

        account = mycursor.fetchall()
        # mycursor
        print(account)
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
    if request.method == 'GET':
        return render_template('update.html')

    if request.method == 'POST':
        # Check if the username and password are correct
        username = request.form['username']
        password = request.form['password']

        mycursor.execute('SELECT * FROM employee WHERE username = %s AND password = %s', (
            username, password,))

        account = mycursor.fetchone()
        print(account, username, password)
        if account:
            session['logged_in'] = True
            # session['username'] = account['username']
            return redirect(url_for('home'))
        else:
            return render_template('update.html', error='Invalid username or password')
    else:
        return render_template('update.html')


@app.route('/home', methods=['GET', 'POST'])
def home():
    if session['logged_in'] == True:
        return render_template('home.html')
    return rredirect(url_for('login'))


if __name__ == '__main__':
    app.run(debug=True)
