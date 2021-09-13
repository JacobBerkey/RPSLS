from Human import Human
from AI import AI

class Game:
    def __init__(self):
        self.player1 = Human(3, "Human", "Human 1")
        self.player2 = AI(3, "AI (Computer)", "Computer")

    def display_welcome(self):
        pass

    def player_turn(self):
        pass

    def show_player_options(self):
        pass

    def display_winner(self):
        pass

