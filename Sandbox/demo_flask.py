from flask import Flask, request, render_template

app = Flask(__name__,
            template_folder = 'templates',
            static_url_path = '',
            static_folder = 'static')


@app.route('/')
def index():
    html = """
    <h1 style="color:darkred;">Hello world!</h1>
    <a href='/help'>Go to help page</a>
    """
    return html


@app.route('/help')
def help():
    html = """
    <h2>Welkom to the help page of this website.</h2>
    <a href='/'>Back to home page</a>
    """
    return html


@app.route('/name')
def name():
    name = request.args.get('username') or 'Stranger'
    html = f"""
    <h2>Your name is {name}</h2>
    <a href='/'>Back to home page</a>
    """
    return html


@app.route('/login', methods = ['GET', 'POST'])
def form():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        print(f'Login: {username} - {password}')
    else:
        username = ''
        password = ''
    html = """
    <h2>Enter your credentials:</h2>
    <form method="post">
        <label>Username</label><input type="text" name="username">
        <br>
        <label>Password</label><input type="password" name="password">
        <br>
        <input type="submit" value="Login">
    </form>
    """
    return html


@app.route('/hello')
def hello():
    querystring = request.query_string.decode('utf-8').upper()
    return render_template('hello.html', data = querystring)


app.run()
