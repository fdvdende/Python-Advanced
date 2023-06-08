import flask
from flask import Flask

app = Flask(__name__,
            template_folder = 'templates',
            static_url_path = '',
            static_folder = 'static')


@app.route("/")
def hello():
    s = "<h1 style='color:#888800;'>Hello World!</h1>"
    s += '<p>Dit is een paragraaf met volledige onzin</p>'
    return s


@app.route("/info")
def info():
    return '<h3>No information on this page.</h3>'


@app.route("/login", methods=['GET'])
def login():
    return flask.render_template('simple_login.html')


@app.route("/login", methods=['POST'])
def handle_login():
    username = flask.request.form['username']
    password = flask.request.form['password']
    print(username, password)
    return 'You are logged in.'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
