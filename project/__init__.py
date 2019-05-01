from flask import Flask, session,redirect,url_for,render_template
from flask_login import LoginManager
import os

app = Flask(__name__)
app.config['SECRECT_KEP'] = 'Strong'
app.secret_key = 'any random string'

from project.login.view import login_blueprint
app.register_blueprint(login_blueprint, url_prefix='/login')

login_manager = LoginManager()
login_manager.init_app(app)

from project.models import UserDataManager

@login_manager.user_loader
def load_user(username):
    userdata = UserDataManager()
    return userdata.get_user(username)

@app.route('/')
def index():
    return render_template('index.html')

#data file
USERDATA = 'project/database/userdata.json'
