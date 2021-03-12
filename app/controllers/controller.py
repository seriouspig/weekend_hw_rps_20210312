from flask import render_template, request, redirect
from app import app
from app.models.game import Game
from app.models.player import Player
import random

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/<choice1>/<choice2>')
def result(choice1, choice2):
    player_1 = Player("Player 1", choice1)
    player_2 = Player("Player 2", choice2)
    new_result = Game.game_result(player_1, player_2)
    return render_template('result.html', result=new_result)

@app.route('/gamestart')
def gamestart():
    return render_template('gamestart.html')

@app.route('/<choice1>')
def p2choice(choice1):
    return render_template('p2choice.html')

@app.route('/cpu/gamestart_cpu')
def gamestart_cpu():
    return render_template('gamestart_cpu.html')

@app.route('/cpu/<choice1_cpu>')
def p2choice_cpu(choice1_cpu):
    weapon_list = ["rock", "paper", "scissors"]
    cpu_choice = random.choice(weapon_list)
    return render_template('p2choice_cpu.html', cpu_choice = cpu_choice)

@app.route('/cpu/<choice1>/<choice2>')
def result_cpu(choice1, choice2):
    player_1 = Player("Player 1", choice1)
    player_2 = Player("Computer", choice2)
    new_result = Game.game_result(player_1, player_2)
    return render_template('result_cpu.html', result=new_result)