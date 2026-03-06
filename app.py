from flask import Flask, render_template, request, redirect, url_for, session
import mysql.connector
from werkzeug.security import generate_password_hash, check_password_hash

# Opprett Flask-app
app = Flask(__name__)
app.secret_key = "hemmelig123"  # Viktig for å bruke session

# Funksjon: koble til MySQL database
def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="mikail2008",
        password="123Akademiet!",
        database="semesteroppgave_db",
        charset='utf8mb4'  # viktig for å støtte hashede passord korrekt
    )

# Hovedside: viser login/registrer side
@app.route('/')
def home():
    return render_template('index.html')

# Registrer ny bruker
@app.route('/register', methods=['POST'])
def register():
    brukernavn = request.form.get('username')
    passord = request.form.get('password')

    if brukernavn and passord:
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)

        # Sjekk om brukeren allerede finnes
        cursor.execute("SELECT * FROM users WHERE username=%s", (brukernavn,))
        eksisterende = cursor.fetchone()

        if not eksisterende:
            # Lag ny bruker med kryptert passord
            hashed_password = generate_password_hash(passord)
            cursor.execute(
                "INSERT INTO users (username, password) VALUES (%s, %s)",
                (brukernavn, hashed_password)
            )
            conn.commit()

            # Hent den nye brukerens ID
            cursor.execute("SELECT * FROM users WHERE username=%s", (brukernavn,))
            ny_bruker = cursor.fetchone()

            # Lagre info i session
            session['user_id'] = ny_bruker['id']
            session['username'] = ny_bruker['username']

        cursor.close()
        conn.close()

    # Send til welcome-side uansett
    return redirect(url_for('welcome'))

# Logg inn eksisterende bruker
@app.route('/login', methods=['POST'])
def login():
    brukernavn = request.form.get('username')
    passord = request.form.get('password')

    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("SELECT * FROM users WHERE username=%s", (brukernavn,))
    bruker = cursor.fetchone()

    cursor.close()
    conn.close()

    if bruker and check_password_hash(bruker['password'], passord):
        session['user_id'] = bruker['id']
        session['username'] = bruker['username']
        return redirect(url_for('welcome'))

    # Hvis login feil, bli på samme side
    return redirect(url_for('home'))

# Welcome-side, kun tilgjengelig hvis logget inn
@app.route('/welcome')
def welcome():
    if 'user_id' not in session:
        return redirect(url_for('home'))
    return render_template('welcome.html', username=session['username'])

# Logg ut bruker
@app.route('/logout', methods=['POST'])
def logout():
    session.clear()
    return redirect(url_for('home'))

