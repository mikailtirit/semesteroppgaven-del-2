from flask import Flask, render_template, request, redirect
from forms import RegisterForm
from werkzeug.security import generate_password_hash, check_password_hash
import mysql.connector

app = Flask(__name__)
app.config['SECRET_KEY'] = 'devkey'

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()

    if request.method == 'POST':
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

        return "User saved to database!"

    return render_template('register.html', form=form)


    @app.route('/login', methods= ['GET', 'POST'])
    def login():
        form = LoginForm()
