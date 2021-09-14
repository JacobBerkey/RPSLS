from Player import Player
import random
import time

class AI(Player):
    def __init__(self, lives, description):
        self.lives = lives
        self.description = description

    def select_gesture(self):
        
        
        print(f"{self.description} is now computing its gesture selection!")



        counter = 0
        for gesture in self.gesture_list:
            print(f"{self.description} is now computing its gesture selection!")
            
            if counter % 2 == 0:
                print(f"Should I choose {self.gesture_list[counter]}?! **********")
            else:
                print(f"Should I choose {self.gesture_list[counter]}?! ##########")
            time.sleep(1)
            counter +=1

        print(f"I, {self.description} selected my gesture! Prepare to lose!")

        return Player.gesture_list[random.randint(1, 5)]

        