import flask
from flask import Flask

from project_c.models.persistence import Persistence

app = Flask(__name__,
            template_folder = 'project_c/templates',
            static_url_path = '',
            static_folder = 'static')


@app.route('/')
def index():
    return flask.render_template('index.html')


@app.route('/login', methods=['GET'])
def login():
    return flask.render_template('login.html')


@app.route('/login', methods=['POST'])
def process_login():
    username = flask.request.form['username']
    password = flask.request.form['password']

    persistence = Persistence()
    user = persistence.get_user(username)

    if user:
            if user.check_password(password):
                return flask.redirect(flask.url_for('secrets', name=username))
            else:
                return flask.abort(401)
    else:
        return flask.abort(401)


@app.route('/<name>')
def user_name(name):
    return f'<h1 style="color:#AA0000">The name is {name}</h1>'


@app.route('/users')
def users():
    persistence = Persistence()
    user_names = persistence.get_user_names()
    return flask.render_template('users.html', names = user_names)


@app.route('/users/<name>/secrets')
def secrets(name):
    persistence = Persistence()
    user = persistence.get_user(name)
    return flask.render_template('secrets.html', user_name = name, secrets = user.secrets)


app.run()