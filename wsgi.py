# pylint: disable=missing-docstring

from flask import Flask, session, render_template, request
from flask_session import Session
from game import Game

app = Flask(__name__)

# Check Configuration section for more details
SESSION_TYPE = 'filesystem'
app.config.from_object(__name__)
Session(app)

@app.route('/')
def home():
    if not 'score' in session:
        session['score']=0

    game = Game(session['score'])
    return render_template('home.html', curr_score=0, score=session['score'], grid=game.grid)


@app.route('/check', methods=["POST"])
def check():
    game = Game(session['score'])
    game.grid = list(request.form['grid'])
    word = request.form['word']
    is_valid = game.is_valid(word)
    if is_valid:
        session['score']+=game.CurrScore()

    return render_template('check.html', is_valid=is_valid, curr_score=game.CurrScore(), score=session['score'], grid=game.grid, word=word)
