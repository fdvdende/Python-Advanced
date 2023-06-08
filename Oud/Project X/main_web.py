from src.models.persistence import PersistenceWithSQLite
from src.models.secret import Secret

import flask


app = flask.Flask(__name__,
                  template_folder = 'templates',
                  static_url_path = '',
                  static_folder = 'static')


@app.route('/')
def index():
    return '<h3>Welkom op de secret secrets "For Your Eyes Only" database.<h3>'


@app.route('/secrets/new', methods=['GET'])
def secret():
    return flask.render_template('secret.html')


@app.route('/secrets', methods=['GET'])
def secrets():
    secrets = [[secret.name, secret.content, secret.owner] for secret in PersistenceWithSQLite.get_secrets()]
    return flask.render_template('secrets.html', data = secrets)


@app.route('/secrets', methods=['POST'])
def new_secret():
    name = flask.request.form['name']
    content = flask.request.form['secret']
    owner = flask.request.form['owner']

    print(name, content, owner)

    secret = Secret(name, content, owner)

    PersistenceWithSQLite.store_secret(secret)

    return 'Your secret has been safely stored.'


    # if user:
    #         if user.check_password(password):
    #             return flask.redirect(flask.url_for('secrets', name=username))
    #         else:
    #             return flask.abort(401)
    # else:
    #     return flask.abort(401)


app.run()