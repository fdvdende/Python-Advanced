from flask import Flask, request, render_template

from project_cypher.cypher.caesar import Caesar

app = Flask(__name__,
            template_folder = 'templates',
            static_url_path = '',
            static_folder = 'static')


@app.route('/encrypt', methods = ['GET', 'POST'])
def encrypt():

    if request.method == 'POST':
        original = request.form['original']
        cypher = Caesar(3)
        encrypted = cypher.encrypt(original)
    else:
        original = ''
        encrypted = ''

    data = {
        'original': original,
        'encrypted': encrypted
    }
    return render_template('encrypt.html', **data)


app.run()
