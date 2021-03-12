from app.models.player import *

def game_result(player1, player2):
    if player1.choice == player2.choice:
        return "Draw"
    elif player1.choice == "rock":
        if player2.choice == "paper":
            return player2.name + " wins by playing " + player2.choice
        else:
            return player1.name + " wins by playing " + player1.choice
    elif player1.choice == "paper":
        if player2.choice == "rock":
            return player1.name + " wins by playing " + player1.choice
        else:
            return player2.name + " wins by playing " + player2.choice
    elif player1.choice == "scissors":
        if player2.choice == "paper":
            return player1.name + " wins by playing " + player1.choice
        else:
            return player2.name + " wins by playing " + player2.choice
   