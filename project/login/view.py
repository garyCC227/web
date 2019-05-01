from flask import render_template, Blueprint,redirect,request,flash
from project.models import *
from flask_login import login_user, login_required, current_user, logout_user

login_blueprint = Blueprint(
    'login',
    __name__,
    static_folder = 'static',
    template_folder = 'templates'
)


@login_blueprint.route('/')
def index():
    return render_template('login/login.html')

@login_blueprint.route('/check_login', methods=['POST','GET'])
def check_login():
    if request.method == 'POST':
        username = request.form.get('username');
        password = request.form.get('pass')

        #getting user detail from database
        dataManager = UserDataManager()
        print(username, password)
        if dataManager.authentication(username, password):
            user = dataManager.get_user(username)
            login_user(user, remember=True)
            print("1")
            return redirect(url_for('index'))
        else:
            #show a error message that username or password is wron
            flash("Wrong usernmae or password!!!")

    return redirect(url_for('login.index'))

@login_blueprint.route('/sign_up')
def register():
    return render_template('login/sign_up.html')

@login_blueprint.route('/logout')
@login_required
def log_out():
    logout_user()
    flash("Logged out successfully !!")
    return redirect(url_for('login.index'))
