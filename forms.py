from flask_wtf import FlaskForm 
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired


class RegisterForm(FlaskForm):
    username = StringField("brukernavn", validators=[InputRequired()])
    password = PasswordField("passord", validators=[InputRequired()])
    submit = SubmitField("register")

    
class LoginForm(FlaskForm):
    username = StringField("brukernavn", validators=[InputRequired()])
    password = PasswordField("passord", validators=[InputRequired()])
    submit = SubmitField("login")