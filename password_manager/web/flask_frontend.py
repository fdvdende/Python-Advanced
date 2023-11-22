from password_manager.model.password_broker import PasswordBroker
from password_manager.persistence.store_in_sqlite import retrieve_one

import flask


app = flask.Flask(__name__,
                  static_url_path='',
                  static_folder='static',
                  template_folder='templates')


@app.route('/')
def hello():
    return flask.render_template('home.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if flask.request.method == 'POST':
        login_username = flask.request.form['username']
        login_password = flask.request.form['password']
        broker = PasswordBroker.retrieve(login_username)
        valid_password = broker.validate_password(login_password)
        if valid_password:
            return flask.redirect("/overview")
        else:
            return flask.redirect("/login")
    else:
        return flask.render_template('login.html')


@app.route('/overview', methods=['GET', 'POST'])
def overview():
    return flask.render_template('overview.html')




if __name__ == '__main__':
    app.run(port = 5001)
