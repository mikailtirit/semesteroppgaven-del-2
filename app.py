from flask import Flask, render_template, request, redirect, session
from forms import RegisterForm, LoginForm
from werkzeug.security import generate_password_hash, check_password_hash
import mysql.connector
import requests
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
            session['user_id'] = user['id']
            session.permanent = True
            return redirect('/dashboard')
        else:
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
    session.pop('user_id', None)
    return redirect('/')


@app.route('/dashboard')
def dashboard():
    if 'user' not in session:
        return redirect('/login')

    search = request.args.get('search')

    if search:
        url = f"https://api.themoviedb.org/3/search/movie?api_key=012bab2f58baf6f690135807994e8f9b&language=en-US&query={search}"
    else:
        url = "https://api.themoviedb.org/3/movie/popular?api_key=012bab2f58baf6f690135807994e8f9b&language=en-US&page=1"

    response = requests.get(url)
    data = response.json()

    movies = data['results']

    return render_template(
        'dashboard.html',
        user=session['user'],
        movies=movies
    )


@app.route('/add_favorite', methods=['POST'])
def add_favorite():
    if 'user_id' not in session:
        return redirect('/login')

    movie_title = request.form['movie_title']
    user_id = session['user_id']

    db = mysql.connector.connect(
        host="localhost",
        user="mikail2008",
        password="123Akademiet!",
        database="semesteroppgave_db"
    )

    cursor = db.cursor()

    sql = "INSERT INTO favorites (user_id, movie_title) VALUES (%s, %s)"
    values = (user_id, movie_title)

    cursor.execute(sql, values)
    db.commit()

    return redirect('/dashboard')


@app.route('/favorites')
def favorites():
    if 'user_id' not in session:
        return redirect('/login')

    db = mysql.connector.connect(
        host="localhost",
        user="mikail2008",
        password="123Akademiet!",
        database="semesteroppgave_db"
    )

    cursor = db.cursor(dictionary=True)
    cursor.execute(
        "SELECT movie_title FROM favorites WHERE user_id = %s",
        (session['user_id'],)
    )

    movies = cursor.fetchall()

    return render_template('favorites.html', movies=movies)


if __name__ == '__main__':
    app.run(debug=True)