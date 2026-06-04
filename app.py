# Importerer det vi trenger for å bygge nettsiden
from flask import Flask, render_template, request, redirect, session

# Importerer skjemaene for registrering og innlogging
from forms import RegisterForm, LoginForm

# Importerer funksjoner som brukes til å hashe passord
# og sjekke passord ved innlogging
from werkzeug.security import generate_password_hash, check_password_hash

# Importerer MySQL slik at vi kan koble nettsiden til databasen
import mysql.connector

# Importerer requests slik at vi kan hente filmdata fra TMDB API
import requests




# Oppretter Flask-applikasjonen
app = Flask(__name__)

# Hemmelig nøkkel som Flask bruker til sessions
app.config['SECRET_KEY'] = 'devkey'



# API-nøkkel til TMDB
API_KEY = "012bab2f58baf6f690135807994e8f9b"


# --------------------------------------------------
# DATABASE
# --------------------------------------------------

# Kobler nettsiden til MySQL-databasen
# Denne funksjonen brukes hver gang vi skal hente
# eller lagre data i databasen
def connect_db():
    return mysql.connector.connect(
        host="localhost",
        user="mikail2008",
        password="123Akademiet!",
        database="semesteroppgave_db"
    )


# --------------------------------------------------
# HJEMMESIDE
# --------------------------------------------------

# Starter på forsiden
@app.route('/')
def home():

    # Hvis brukeren allerede er innlogget
    # sendes han direkte til dashboardet
    if 'user' in session:
        return redirect('/dashboard')

    return render_template('home.html')


# --------------------------------------------------
# INNLOGGING
# --------------------------------------------------

@app.route('/login', methods=['GET', 'POST'])
def login():

    # Lager skjemaene som brukes på siden
    login_form = LoginForm()
    register_form = RegisterForm()

    error = None

    # Kjører når brukeren sender inn innloggingsskjemaet
    if login_form.validate_on_submit():

        # Kobler til databasen
        db = connect_db()
        cursor = db.cursor(dictionary=True)

        # Henter brukeren med det oppgitte brukernavnet
        # %s brukes for å beskytte mot SQL Injection
        cursor.execute(
            "SELECT * FROM users WHERE username = %s",
            (login_form.username.data,)
        )

        user = cursor.fetchone()

        # Sjekker om brukeren finnes
        # og om passordet stemmer
        if user and check_password_hash(
            user['password'],
            login_form.password.data
        ):

            # Lagrer brukerinformasjon i session
            session['user'] = user['username']
            session['user_id'] = user['id']

            # Gjør session permanent
            session.permanent = True

            return redirect('/dashboard')

        # Feilmelding hvis innlogging feiler
        error = "Invalid username or password"

    return render_template(
        'login.html',
        login_form=login_form,
        register_form=register_form,
        error=error
    )


# --------------------------------------------------
# REGISTRERING
# --------------------------------------------------

@app.route('/register', methods=['POST'])
def register():

    form = RegisterForm()

    if form.validate_on_submit():

        db = connect_db()
        cursor = db.cursor()

        # Hasher passordet før det lagres
        # Dette gjør at passordet ikke lagres som vanlig tekst
        hashed_password = generate_password_hash(
            form.password.data
        )

        
        # Lagrer ny bruker i databasen
        cursor.execute(
            "INSERT INTO users (username, password) VALUES (%s, %s)",
            (
                form.username.data,
                hashed_password
            )
        )

        db.commit()

    return redirect('/login')


# --------------------------------------------------
# LOGG UT
# --------------------------------------------------

@app.route('/logout')
def logout():

    # Sletter all session-informasjon
    # slik at brukeren logges ut
    session.clear()

    return redirect('/')


# --------------------------------------------------
# DASHBOARD
# --------------------------------------------------

@app.route('/dashboard')
def dashboard():

    # Sender brukeren til login hvis han ikke er innlogget
    if 'user' not in session:
        return redirect('/login')

    # Henter søkeord fra søkefeltet
    search = request.args.get('search')

    # Hvis brukeren søker etter en film
    if search:
        url = (
            f"https://api.themoviedb.org/3/search/movie"
            f"?api_key={API_KEY}&query={search}"
        )

    # Hvis ingen søk er gjort
    # vis populære filmer
    else:
        url = (
            f"https://api.themoviedb.org/3/movie/popular"
            f"?api_key={API_KEY}"
        )

    # Henter filmdata fra TMDB
    movies = requests.get(url).json()['results']

    return render_template(
        'dashboard.html',
        user=session['user'],
        movies=movies
    )





if __name__ == '__main__':
    app.run(debug=True)