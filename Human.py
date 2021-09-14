from Player import Player

class Human(Player):
    def __init__(self, lives, description):
        self.lives = lives
        self.description = description

    def select_gesture(self):
        print("Make sure your opponent isn't watching and type your gesture!")
        counter = 0
        for gesture in self.gesture_list:
            print("Press " + str(counter) + " to select " + gesture)
            counter +=1
        
        selected_gesture = int(input("Select your gesture from the options above."))
        
        return self.gesture_list[selected_gesture]
        
