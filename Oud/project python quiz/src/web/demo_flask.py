from flask import Flask, render_template, request

from models.game import Game

app = Flask(__name__)


@app.route("/")
def index():
    return render_template('index.html')

@app.route("/question")
def question():
    game = Game()
    content = {
        'id': game.qa.id,
        'question': game.qa.question,
        'answer': game.qa.answer,
        'keywords': game.qa.keywords
    }
    return render_template('question.html', content = content)


@app.route("/question/<id>/check")
def check(id):
    response = request.args.get('response')

    game = Game(id = id)
    keyword = game.qa.compare_to_keyword(response)

    return {'id':int(id), 'response':response, 'keyword':keyword}


app.run()