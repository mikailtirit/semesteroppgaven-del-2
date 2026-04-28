from flask import Flask, render_template, request, redirect, session
from forms import RegisterForm, LoginForm
from werkzeug.security import generate_password_hash, check_password_hash
import mysql.connector

app = Flask(__name__)
app.config['SECRET_KEY'] = 'devkey'



@app.route('/')
def home():
    return render_template('home.html', user=session.get('user'))


@app.route('/login', methods=['GET', 'POST'])
def login():
    login_form = LoginForm()
    register_form = RegisterForm()


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
            return redirect('/')
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


