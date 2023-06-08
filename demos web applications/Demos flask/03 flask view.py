from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def index():
    return "Flask App!"


@app.route("/users/")
def users():
    users = ["Frank", "Steve", "Alice", "Bruce"]
    return render_template('users.html', **locals())


users = ["A", "B", "C", "D"]

@app.route("/list/", methods=["get", "post"])
def list():

    if request.method == 'POST':
        if 'add_line' in request.form:
            new_line = request.form['new_line']
            users.append(new_line)
        elif 'delete_line' in request.form:
            line_to_delete = request.form['line_to_delete']
            users.remove(line_to_delete)

    return render_template('list.html', users = users)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)