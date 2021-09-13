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
        print("Make sure your opponent isn't watching and select your weapon!")
        counter = 0
        for weapon in self.weapons:
            print('Press ' + str(counter) + ' to select ' + weapon)
            counter +=1

    def display_winner(self):
        if len(self.player1.lives) > len(self.player2.lives):
            print('Player 1 wins!!')
        else:
            print('Player 2 wins!')

