from flask import render_template, Blueprint

login_blueprint = Blueprint(
    'login',
    __name__,
    static_folder = 'static',
    template_folder = 'templates'
)


@login_blueprint.route('/')
def index():
    return render_template('login/login.html')
