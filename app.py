from flask import Flask, render_template, request, redirect, session
from forms import RegisterForm, LoginForm
from werkzeug.security import generate_password_hash, check_password_hash
import mysql.connector
import requests
from datetime import timedelta

app = Flask(__name__)
app.config['SECRET_KEY'] = 'devkey'
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(hours=24)

API_KEY = "012bab2f58baf6f690135807994e8f9b"


# Database connection
def connect_db():
    return mysql.connector.connect(
        host="localhost",
        user="mikail2008",
        password="123Akademiet!",
        database="semesteroppgave_db"
    )


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
        db = connect_db()
        cursor = db.cursor(dictionary=True)

        cursor.execute(
            "SELECT * FROM users WHERE username = %s",
            (login_form.username.data,)
        )

        user = cursor.fetchone()

        if user and check_password_hash(user['password'], login_form.password.data):
            session['user'] = user['username']
            session['user_id'] = user['id']
            session.permanent = True
            return redirect('/dashboard')

        error = "Invalid username or password"

    return render_template(
        'login.html',
        login_form=login_form,
        register_form=register_form,
        error=error
    )


@app.route('/register', methods=['POST'])
def register():
    form = RegisterForm()

    if form.validate_on_submit():
        db = connect_db()
        cursor = db.cursor()

        cursor.execute(
            "INSERT INTO users (username, password) VALUES (%s, %s)",
            (
                form.username.data,
                generate_password_hash(form.password.data)
            )
        )

        db.commit()

    return redirect('/login')


@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')


@app.route('/dashboard')
def dashboard():
    if 'user' not in session:
        return redirect('/login')

    search = request.args.get('search')

    if search:
        url = f"https://api.themoviedb.org/3/search/movie?api_key={API_KEY}&query={search}"
    else:
        url = f"https://api.themoviedb.org/3/movie/popular?api_key={API_KEY}"

    movies = requests.get(url).json()['results']

    return render_template(
        'dashboard.html',
        user=session['user'],
        movies=movies
    )


@app.route('/add_favorite', methods=['POST'])
def add_favorite():
    if 'user_id' not in session:
        return redirect('/login')

    db = connect_db()
    cursor = db.cursor()

    cursor.execute(
        "INSERT INTO favorites (user_id, movie_title) VALUES (%s, %s)",
        (session['user_id'], request.form['movie_title'])
    )

    db.commit()
    return redirect('/dashboard')


@app.route('/favorites')
def favorites():
    if 'user_id' not in session:
        return redirect('/login')

    db = connect_db()
    cursor = db.cursor(dictionary=True)

    cursor.execute(
        "SELECT id, movie_title FROM favorites WHERE user_id = %s",
        (session['user_id'],)
    )

    movies = cursor.fetchall()

    return render_template('favorites.html', movies=movies)


@app.route('/delete_favorite/<int:id>', methods=['POST'])
def delete_favorite(id):
    if 'user_id' not in session:
        return redirect('/login')

    db = connect_db()
    cursor = db.cursor()

    cursor.execute(
        "DELETE FROM favorites WHERE id = %s AND user_id = %s",
        (id, session['user_id'])
    )

    db.commit()
    return redirect('/favorites')


@app.route('/recommended')
def recommended():
    if 'user_id' not in session:
        return redirect('/login')

    db = connect_db()
    cursor = db.cursor(dictionary=True)

    cursor.execute(
        "SELECT movie_title FROM favorites WHERE user_id = %s LIMIT 1",
        (session['user_id'],)
    )

    favorite = cursor.fetchone()

    if not favorite:
        return render_template('recommended.html', movies=[])

    search = requests.get(
        f"https://api.themoviedb.org/3/search/movie?api_key={API_KEY}&query={favorite['movie_title']}"
    ).json()

    if not search['results']:
        return render_template('recommended.html', movies=[])

    movie_id = search['results'][0]['id']

    movies = requests.get(
        f"https://api.themoviedb.org/3/movie/{movie_id}/similar?api_key={API_KEY}"
    ).json()['results']

    return render_template('recommended.html', movies=movies)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)