from flask import Flask, render_template, request, redirect
from forms import RegisterForm
from werkzeug.security import generate_password_hash, check_password_hash