from Player import Player

class Human(Player):
    def __init__(self, lives, description):
        self.lives = lives
        self.description = description

    def select_gesture(self):
        print(f"\nMake sure your human opponent isnt watching and select from the below gestures\n")
        counter = 0
        for gesture in self.gesture_list:
            print("Type " + str(counter) + " to select " + gesture + "\n")
            counter +=1
        
        while True:
            try:
                selected_gesture = int(input("Select your gesture from the options above. \n\n"))
            
            except ValueError:
                print("Sorry I don\'t understand that!")
                continue
            if selected_gesture > 4:
                print("ERROR: Please type a number 0-4")
            else:
                 return self.gesture_list[selected_gesture]