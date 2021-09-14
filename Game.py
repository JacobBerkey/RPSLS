from Human import Human
from AI import AI
from Player import Player
import random


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
        Human(Player).select_gesture()
        player1_gesture = int(input("What gesture will Player 1 use"))
        Human(Player).select_gesture()
        if self.player2.type == "AI (Computer)":
            player2_gesture = Player.gesture_list[random.randint(1, 5)]
        elif self.player2.type == "Human":
            player2_gesture = int(input("What gesture will Player 2 use?"))
        
        if player1_gesture == "Rock": 
            if player2_gesture == "Rock":
                print(f"Both players selected {player1_gesture}. It's a tie!")
            elif player2_gesture == "Paper":
                print(f"{self.player2.description} beats {self.player1.description} since {player2_gesture} wraps around {player1_gesture}!")
                self.player1.lives -= self.player1.lives
            elif player2_gesture == "Scissors":
                print(f"{self.player1.description} beats {self.player2.description} since {player1_gesture} smashes {player2_gesture}!")
                self.player2.lives -= self.player2.lives
            elif player2_gesture == "Lizard":
                print(f"{self.player1.description} beats {self.player2.description} since {player1_gesture} crushes {player2_gesture}!")
                self.player2.lives -= self.player2.lives
            elif player2_gesture == "Spock":
                print(f"{self.player2.description} beats {self.player1.description} since {player1_gesture} vaporizes {player2_gesture}!")
                self.player1.lives -= self.player1.lives

        if player1_gesture == "Paper": 
            if player2_gesture == "Paper":
                print(f"Both players selected {player1_gesture}. It's a tie!")
            elif player2_gesture == "Scissors":
                print(f"{self.player2.description} beats {self.player1.description} since {player2_gesture} cuts {player1_gesture}!")
                self.player1.lives -= self.player1.lives
            elif player2_gesture == "Rock":
                print(f"{self.player1.description} beats {self.player2.description} since {player1_gesture} covers {player2_gesture}!")
                self.player2.lives -= self.player2.lives
            elif player2_gesture == "Lizard":
                print(f"{self.player2.description} beats {self.player1.description} since {player2_gesture} eats {player1_gesture}!")
                self.player1.lives -= self.player1.lives
            elif player2_gesture == "Spock":
                print(f"{self.player1.description} beats {self.player2.description} since {player1_gesture} disproves {player2_gesture}!")
                self.player2.lives -= self.player2.lives

        if player1_gesture == "Scissors": 
            if player2_gesture == "Scissors":
                print(f"Both players selected {player1_gesture}. It's a tie!")
            elif player2_gesture == "Rock":
                print(f"{self.player2.description} beats {self.player1.description} since {player2_gesture} crushes {player1_gesture}!")
                self.player1.lives -= self.player1.lives
            elif player2_gesture == "Paper":
                print(f"{self.player1.description} beats {self.player2.description} since {player1_gesture} cuts {player2_gesture}!")
                self.player2.lives -= self.player2.lives
            elif player2_gesture == "Lizard":
                print(f"{self.player1.description} beats {self.player2.description} since {player1_gesture} decapitates {player2_gesture}!")
                self.player2.lives -= self.player2.lives
            elif player2_gesture == "Spock":
                print(f"{self.player2.description} beats {self.player1.description} since {player2_gesture} smashes {player1_gesture}!")
                self.player1.lives -= self.player1.lives

        if player1_gesture == "Lizard": 
            if player2_gesture == "Lizard":
                print(f"Both players selected {player1_gesture}. It's a tie!")
            elif player2_gesture == "Rock":
                print(f"{self.player2.description} beats {self.player1.description} since {player2_gesture} crushes {player1_gesture}!")
                self.player1.lives -= self.player1.lives
            elif player2_gesture == "Paper":
                print(f"{self.player1.description} beats {self.player2.description} since {player1_gesture} eats {player2_gesture}!")
                self.player2.lives -= self.player2.lives
            elif player2_gesture == "Scissors":
                print(f"{self.player2.description} beats {self.player1.description} since {player2_gesture} decapitates {player1_gesture}!")
                self.player1.lives -= self.player1.lives
            elif player2_gesture == "Spock":
                print(f"{self.player1.description} beats {self.player2.description} since {player1_gesture} poisons {player2_gesture}!")
                self.player2.lives -= self.player2.lives

        if player1_gesture == "Spock": 
            if player2_gesture == "Spock":
                print(f"Both players selected {player1_gesture}. It's a tie!")
            elif player2_gesture == "Rock":
                print(f"{self.player1.description} beats {self.player2.description} since {player1_gesture} vaporizes {player2_gesture}!")
                self.player2.lives -= self.player2.lives
            elif player2_gesture == "Paper":
                print(f"{self.player2.description} beats {self.player1.description} since {player2_gesture} disproves {player1_gesture}!")
                self.player1.lives -= self.player1.lives
            elif player2_gesture == "Scissors":
                print(f"{self.player1.description} beats {self.player2.description} since {player1_gesture} smashes {player2_gesture}!")
                self.player2.lives -= self.player2.lives
            elif player2_gesture == "Lizard":
                print(f"{self.player2.description} beats {self.player1.description} since {player2_gesture} poisons {player1_gesture}!")
                self.player1.lives -= self.player1.lives

    def display_winner(self):
        if len(self.player1.lives) > len(self.player2.lives):
            print('Player 1 wins!!')
        else:
            print('Player 2 wins!')

