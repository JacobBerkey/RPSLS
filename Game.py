from Human import Human
from AI import AI

class Game:
    def __init__(self):
        self.player1 = Human(3, "Human", "Human 1")
        self.player2 = AI(3, "AI (Computer)", "Computer")

    def display_welcome(self):
        print("Welcome to Rock, Paper, Scissors, Lizard, Spock!")
        player2 = int(input("Will the second player be a human [Press 1] or [Press 2] to play the AI?"))
        if player2 == 1:
            self.player2 = Human(3, "Human", "Human 2")
        if player2 == 2:
            pass

    def player_turn(self):
        pass

    def show_player_options(self):
        pass

    def display_winner(self):
        pass

