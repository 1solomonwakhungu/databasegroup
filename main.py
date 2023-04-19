from flask import Flask, render_template, request, redirect, url_for, session
import mysql.connector

# Connect to local sql server
mydb = mysql.connector.connect(host = "localhost", user = "root", passwd = "VedNigam1", database = "hospital_db")
mycursor = mydb.cursor()

app = Flask(__name__, static_url_path='',
            static_folder='./static',
            template_folder='./templates')
app.secret_key = 'QB*&jy1MlTK@aA#gn&OEG*m4zzUk4F'


@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Check if the username and password are correct
        username = request.form['username']
        password = request.form['password']

        mycursor.execute('SELECT * FROM employee WHERE username = %s AND password = %s', (username, password,))
        
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
        return render_template('buttons.html')
    else:
        return redirect(url_for('login'))


@app.route('/logout')
def logout():
    session['logged_in'] = False
    return redirect(url_for('login'))


if __name__ == '__main__':
    app.run(debug=True)