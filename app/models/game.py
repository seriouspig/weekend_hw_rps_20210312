from app.models.player import *

def game_result(player1, player2):
    if player1.choice == player2.choice:
        return "Draw"
    elif player1.choice == "rock":
        if player2.choice == "paper":
            return "Player 2 wins by playing paper!"
        else:
            return "Player 1 wins by playing rock!"
    elif player1.choice == "paper":
        if player2.choice == "rock":
            return "Player 1 wins by playing paper!"
        else:
            return "Player 2 wins rock!"
    elif player1.choice == "scissors":
        if player2.choice == "paper":
            return "Player 1 wins by playing scissors!"
        else:
            return "Player 2 wins by playing paper!"
   