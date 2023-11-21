import flask

app = flask.Flask(__name__,
                  static_url_path='',
                  static_folder='static',
                  template_folder='templates')


@app.route('/')
def hello():
    return flask.render_template('home.html')


if __name__ == '__main__':
    app.run()
