from flask_wtf import FlaskForm 
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired


class registerForm(FlaskForm):
    username = StringField("brukernavn", validators=[InputRequired()])
    Password = PasswordField("passord", validators=[InputRequired()])
    submit = SubmitField("register")