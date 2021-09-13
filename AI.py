from Player import Player

class AI(Player):
    def __init__(self, lives, type, description):
        Player.lives = lives
        Player.type = type
        Player.description = description
        