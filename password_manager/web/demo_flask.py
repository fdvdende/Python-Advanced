import flask

app = flask.Flask(__name__)



@app.route('/')
def hello():
    s = '''\
<html>
<head>
  <title>Demo Flask</title>
</head>
<body>
  <h1>Hello world! Welcome to Flask.</h1>
</body>
</html>'''
    return s



@app.route('/welcome/<string:name>')
def welcome(name):
    s = f'''\
<html>
<head>
  <title>Demo Flask</title>
</head>
<body>
  <h1>Welcome {name.title()}.</h1>
  <p>How do you do?</>
</body>
</html>'''
    return s


@app.route('/help')
def help():
    s = f'''\
<html>
<head>
  <title>Help on endpoints</title>
</head>
<body>
  <h1>Endpoints</h1>
  <ul>
    <li><a href="/">/</a></li>
    <li><a href="/help">/help</a></li>
    <li><a href="/welcome/<name>">/welcome/<name></a></li>
  </ul>
</body>
</html>'''
    return s



if __name__ == '__main__':
    app.run()
