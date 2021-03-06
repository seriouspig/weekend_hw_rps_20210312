from flask import render_template, request, redirect, g
from app import app
from app.models.game import Game
from app.models.player import Player
import random

global player_1_name 
global player_2_name

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/<choice1>/<choice2>')
def result(choice1, choice2):
    global player_1_name
    global player_2_name
    player_1 = Player(player_1_name, choice1)
    player_2 = Player(player_2_name, choice2)
    new_result, new_winner = Game.game_result(player_1, player_2)
    return render_template('result.html', result=new_result, winner=new_winner)

@app.route('/gamestart')
def gamestart():
    return render_template('gamestart.html', p1name = player_1_name)

@app.route('/<choice1>')
def p2choice(choice1):
    return render_template('p2choice.html', p2name = player_2_name)

@app.route('/cpu/gamestart_cpu')
def gamestart_cpu():
    # player_1_name = create_name_cpu.player_1_name
    return render_template('gamestart_cpu.html', p1name = player_1_name)

@app.route('/cpu/<choice1_cpu>')
def p2choice_cpu(choice1_cpu):
    weapon_list = ["rock", "paper", "scissors"]
    cpu_choice = random.choice(weapon_list)
    return render_template('p2choice_cpu.html', cpu_choice = cpu_choice)

@app.route('/cpu/<choice1>/<choice2>')
def result_cpu(choice1, choice2):
    global player_1_name
    player_1 = Player(player_1_name, choice1)
    player_2 = Player("Computer", choice2)
    new_result, new_winner = Game.game_result(player_1, player_2)
    return render_template('result_cpu.html', result=new_result, winner=new_winner)

@app.route('/get_name_cpu')
def get_name_cpu():
    return render_template('get_name_cpu.html')

@app.route('/get_name_cpu', methods=['POST'])
def create_name_cpu():
    global player_1_name
    player_1_name = request.form['name1']
    return render_template('get_name_cpu.html')

@app.route('/get_name')
def get_name():
    return render_template('get_name.html')

@app.route('/get_name', methods=['POST'])
def create_name():
    global player_1_name
    global player_2_name
    player_1_name = request.form['name1']
    player_2_name = request.form['name2']
    return render_template('get_name.html')

@app.route('/settings')
def get_settings():
    return render_template('settings.html')
