import random

class Player():

    def __init__(self, name, choice):
        self.name = name
        self.choice = choice


    def random_cpu():
        weapon_list = ["rock", "paper", "scissors"]
        return random.choice(weapon_list)
