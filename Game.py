from Human import Human
from AI import AI

class Game:
    def __init__(self):
        self.player1 = Human(3, "Human 1")

    def run_game(self):
        self.display_welcome()
        self.play_game()
        self.display_winner()

    def play_game(self):
        while self.player1.lives > 0 and self.player2.lives > 0:
            self.player_turn()

    def play_turn(self):
        pass
        
    def display_welcome(self):
        print("Welcome to Rock, Paper, Scissors, Lizard, Spock!")
        player2 = int(input("Will the second player be a human [Type '1'] or [Type '2'] to play against the computer ?"))
        if player2 == 1:
            self.player2 = Human(3, "Human 2")
        if player2 == 2:
            self.player2 = AI(3, "AI (The Computer)")

    def player_turn(self):
        pass

    def display_winner(self):
        if len(self.player1.lives) > len(self.player2.lives):
            print('Player 1 wins!!')
        else:
            print('Player 2 wins!')

