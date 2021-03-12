from flask import render_template, request, redirect
from app import app
from app.models.game import game_result
from app.models.player import Player

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/<choice1>/<choice2>')
def result(choice1, choice2):
    player_1 = Player("Player 1", choice1)
    player_2 = Player("Player 2", choice2)
    new_result = game_result(player_1, player_2)
    return render_template('result.html', result=new_result)

@app.route('/gamestart')
def gamestart():
    return render_template('gamestart.html')

@app.route('/<choice1>')
def p2choice(choice1):
    return render_template('p2choice.html')

