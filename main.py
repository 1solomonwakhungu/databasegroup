from flask import Flask, render_template, request, redirect, url_for, session

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

        print("[*] LOGIN:", username, password)
        if username == 'admin' and password == 'password':
            session['logged_in'] = True
            return redirect(url_for('home'))
        else:
            return render_template('login.html', error='Invalid username or password')
    else:
        return render_template('login.html')


@app.route('/home')
def home():
    if session.get('logged_in'):
        return render_template('home.html')
    else:
        return redirect(url_for('login'))


@app.route('/logout')
def logout():
    session['logged_in'] = False
    return redirect(url_for('login'))


if __name__ == '__main__':
    app.run(debug=True)
