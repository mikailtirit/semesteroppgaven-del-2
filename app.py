from flask import Flask, render_template, request, redirect, session
from forms import RegisterForm, LoginForm
from werkzeug.security import generate_password_hash, check_password_hash
import mysql.connector
from datetime import timedelta 

app = Flask(__name__)
app.config['SECRET_KEY'] = 'devkey'

app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(hours=24)


@app.route('/')
def home():
    if 'user' in session:
        return redirect('/dashboard')  
    return render_template('home.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    login_form = LoginForm()
    register_form = RegisterForm()
    error = None


    if login_form.validate_on_submit():
        username = login_form.username.data
        password = login_form.password.data

        db = mysql.connector.connect(
            host="localhost",
            user="mikail2008",
            password="123Akademiet!",
            database="semesteroppgave_db"
        )

        cursor = db.cursor(dictionary=True)

        sql = "SELECT * FROM users WHERE username = %s"
        cursor.execute(sql, (username,))
        user = cursor.fetchone()

        if user and check_password_hash(user['password'], password):
            session['user'] = user['username']
            session.permanent = True
            return redirect('/dashboard')
        else:
            return "Invalid login"

    return render_template(
        'login.html',
        login_form=login_form,
        register_form=register_form
    )



@app.route('/register', methods=['POST'])
def register():
    form = RegisterForm()

    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data

        hashed_password = generate_password_hash(password)

        db = mysql.connector.connect(
            host="localhost",
            user="mikail2008",
            password="123Akademiet!",
            database="semesteroppgave_db"
        )

        cursor = db.cursor()

        sql = "INSERT INTO users (username, password) VALUES (%s, %s)"
        values = (username, hashed_password)

        cursor.execute(sql, values)
        db.commit()

        return redirect('/login')

    return redirect('/login')



@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect('/')


@app.route('/dashboard')
def dashboard():
    if 'user' not in session:
        return redirect('/login')
    
    return render_template('dashboard.html', user=session['user'])


