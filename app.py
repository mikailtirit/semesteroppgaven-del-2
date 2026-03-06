from flask import Flask, render_template, request, redirect, url_for, session
import mysql.connector
from werkzeug.security import generate_password_hash, check_password_hash

# Opprett Flask-app
app = Flask(__name__)
app.secret_key = "k39fj29FJ#9fj29fJ$"  # Holder innloggingen trygg

# Funksjon: Koble til MySQL
def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="mikail2008",
        password="123Akademiet!",
        database="semesteroppgave_db"
    )

# FORSIDE: viser register/login-side
@app.route('/')
def home():
    return render_template('index.html')

# REGISTRER NY BRUKER
@app.route('/register', methods=['POST'])
def register():
    brukernavn = request.form.get('username')
    passord = request.form.get('password')

    if brukernavn and passord:
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)

        # Sjekk om brukeren allerede finnes
        cursor.execute("SELECT * FROM users WHERE username = %s", (brukernavn,))
        eksisterende = cursor.fetchone()

        if not eksisterende:
            hashed_password = generate_password_hash(passord)
            cursor.execute(
                "INSERT INTO users (username, password) VALUES (%s, %s)",
                (brukernavn, hashed_password)
            )
            conn.commit()

        cursor.close()
        conn.close()

    return redirect(url_for('home'))

# LOGG INN
@app.route('/login', methods=['POST'])
def login():
    brukernavn = request.form.get('username')
    passord = request.form.get('password')

    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("SELECT * FROM users WHERE username = %s", (brukernavn,))
    bruker = cursor.fetchone()

    cursor.close()
    conn.close()

    # Sjekk passord
    if bruker and check_password_hash(bruker['password'], passord):
        session['user_id'] = bruker['id']
        session['username'] = bruker['username']
        return redirect(url_for('welcome'))
        

    return redirect(url_for('home'))

# WELCOME-SIDE
@app.route('/welcome')
def welcome():
    if 'user_id' not in session:
        return redirect(url_for('home'))
    return render_template('welcome.html', username=session['username'])

if __name__ == '__main__':
    app.run(debug=True)