from flask import Flask, session,redirect,url_for
from flask_login import LoginManager
import os

app = Flask(__name__)
app.config['SECRECT_KEP'] = 'Strong'
app.secret_key = 'any random string'

from project.login.view import login_blueprint
app.register_blueprint(login_blueprint, url_prefix='/login')

@app.route('/')
def index():
    return redirect(url_for('login.index'))
