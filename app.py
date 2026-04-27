from flask import Flask, render_template, request, redirect
from forms import RegisterForm
from werkzeug.security import generate_password_hash, check_password_hash

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

        return f"Username: {username} | Hashed Password: {hashed_password}"

    return render_template('register.html', form=form)