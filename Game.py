from Human import Human
from AI import AI
import random

class Game:
    def __init__(self):
        self.player1 = Human(3, "Human 1")

    def run_game(self):
        self.display_welcome()
        self.play_game()
        self.display_winner()

    def play_game(self):
        while (self.player1.lives > 0 and self.player2.lives) > 0:
            self.play_a_round()


    def display_welcome(self):
        print("\nWelcome to Rock, Paper, Scissors, Lizard, Spock!\n")
        player2 = input("Will the second player be a human [Type 'one'] or [Type 'two'] to play against the computer ?\n").lower()
        while player2 != "one" and player2 != "two":
            player2 = input("Will the second player be a human [Type 'one'] or [Type 'two'] to play against the computer ?\n").lower()
        if player2 == "one":
            self.player2 = Human(3, "Human 2")
        if player2 == "two":
            self.player2 = AI(3, "AI (The Computer)")



    def play_a_round(self):
        player1_gesture = self.player1.select_gesture()
        player2_gesture = self.player2.select_gesture()
        
        if player1_gesture == "Rock": 
            if player2_gesture == "Rock":
                print(f"Both players selected {player1_gesture}. It's a tie!")
            elif player2_gesture == "Paper":
                print(f"{self.player2.description} beats {self.player1.description} since {player2_gesture} wraps around {player1_gesture}!")
                self.player1.lives = self.player1.lives - 1
            elif player2_gesture == "Scissors":
                print(f"{self.player1.description} beats {self.player2.description} since {player1_gesture} smashes {player2_gesture}!")
                self.player2.lives = self.player2.lives - 1
            elif player2_gesture == "Lizard":
                print(f"{self.player1.description} beats {self.player2.description} since {player1_gesture} crushes {player2_gesture}!")
                self.player2.lives = self.player2.lives - 1
            elif player2_gesture == "Spock":
                print(f"{self.player2.description} beats {self.player1.description} since {player1_gesture} vaporizes {player2_gesture}!")
                self.player1.lives = self.player1.lives - 1

        if player1_gesture == "Paper": 
            if player2_gesture == "Paper":
                print(f"Both players selected {player1_gesture}. It's a tie!")
            elif player2_gesture == "Scissors":
                print(f"{self.player2.description} beats {self.player1.description} since {player2_gesture} cuts {player1_gesture}!")
                self.player1.lives = self.player1.lives - 1
            elif player2_gesture == "Rock":
                print(f"{self.player1.description} beats {self.player2.description} since {player1_gesture} covers {player2_gesture}!")
                self.player2.lives = self.player2.lives - 1
            elif player2_gesture == "Lizard":
                print(f"{self.player2.description} beats {self.player1.description} since {player2_gesture} eats {player1_gesture}!")
                self.player1.lives = self.player1.lives - 1
            elif player2_gesture == "Spock":
                print(f"{self.player1.description} beats {self.player2.description} since {player1_gesture} disproves {player2_gesture}!")
                self.player2.lives = self.player2.lives - 1

        if player1_gesture == "Scissors": 
            if player2_gesture == "Scissors":
                print(f"Both players selected {player1_gesture}. It's a tie!")
            elif player2_gesture == "Rock":
                print(f"{self.player2.description} beats {self.player1.description} since {player2_gesture} crushes {player1_gesture}!")
                self.player1.lives = self.player1.lives - 1
            elif player2_gesture == "Paper":
                print(f"{self.player1.description} beats {self.player2.description} since {player1_gesture} cuts {player2_gesture}!")
                self.player2.lives = self.player2.lives - 1
            elif player2_gesture == "Lizard":
                print(f"{self.player1.description} beats {self.player2.description} since {player1_gesture} decapitates {player2_gesture}!")
                self.player2.lives = self.player2.lives - 1
            elif player2_gesture == "Spock":
                print(f"{self.player2.description} beats {self.player1.description} since {player2_gesture} smashes {player1_gesture}!")
                self.player1.lives = self.player1.lives - 1

        if player1_gesture == "Lizard": 
            if player2_gesture == "Lizard":
                print(f"Both players selected {player1_gesture}. It's a tie!")
            elif player2_gesture == "Rock":
                print(f"{self.player2.description} beats {self.player1.description} since {player2_gesture} crushes {player1_gesture}!")
                self.player1.lives = self.player1.lives - 1
            elif player2_gesture == "Paper":
                print(f"{self.player1.description} beats {self.player2.description} since {player1_gesture} eats {player2_gesture}!")
                self.player2.lives = self.player2.lives - 1
            elif player2_gesture == "Scissors":
                print(f"{self.player2.description} beats {self.player1.description} since {player2_gesture} decapitates {player1_gesture}!")
                self.player1.lives = self.player1.lives - 1
            elif player2_gesture == "Spock":
                print(f"{self.player1.description} beats {self.player2.description} since {player1_gesture} poisons {player2_gesture}!")
                self.player2.lives = self.player2.lives - 1

        if player1_gesture == "Spock": 
            if player2_gesture == "Spock":
                print(f"Both players selected {player1_gesture}. It's a tie!")
            elif player2_gesture == "Rock":
                print(f"{self.player1.description} beats {self.player2.description} since {player1_gesture} vaporizes {player2_gesture}!")
                self.player2.lives = self.player2.lives - 1
            elif player2_gesture == "Paper":
                print(f"{self.player2.description} beats {self.player1.description} since {player2_gesture} disproves {player1_gesture}!")
                self.player1.lives = self.player1.lives - 1
            elif player2_gesture == "Scissors":
                print(f"{self.player1.description} beats {self.player2.description} since {player1_gesture} smashes {player2_gesture}!")
                self.player2.lives = self.player2.lives - 1
            elif player2_gesture == "Lizard":
                print(f"{self.player2.description} beats {self.player1.description} since {player2_gesture} poisons {player1_gesture}!")
                self.player1.lives = self.player1.lives - 1

        print(f"Player 1 ({self.player1.description}) now has {self.player1.lives} lives left and Player 2 ({self.player2.description}) now has {self.player2.lives} lives left")

    def display_winner(self):
        if self.player1.lives == 0 or self.player2.lives == 0:
            if self.player1.lives > self.player2.lives:
                print(f"Player 1 ({self.player1.description}) wins!!!!")
            else:
                print(f"Player 2 ({self.player1.description}) wins!!!!") 

