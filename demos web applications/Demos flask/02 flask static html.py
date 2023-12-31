from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/<string:page_name>/')
def render_static(page_name):
    return render_template('%s.html' % page_name)

@app.route('/login', methods=['POST', 'GET'])
def login():
    error = None
    if request.method == 'POST':
        print(request.form['username'])
    else:
        error = 'Invalid username/password'
    # the code below is executed if the request method
    # was GET or the credentials were invalid
    return render_template('login.html', error=error)


app.run()