from flask import render_template
from application_poker import app


@app.route('/')
def index():
    return render_template('test.html')


@app.route('/poker')
def launch_poker_game():
    return render_template('poker.html')