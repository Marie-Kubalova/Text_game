# This is a text based game I'm working on to practice Python
# Created on 13/02/2022
#
#
#

import time
game_over = 0
choiceA = ["a", "A"]
choiceB = ["b", "B"]
choiceC = ["c", "C"]
empty = ["", " "]
yes = ["y", "Y", "yes", "YES", "Yes"]
no = ["n", "N", "no", "NO", "No"]
key = 0
upstairs = 0


def intro():
    print("A loud creak awakens you, and you slowly realise you're alone, "
          "\nlying on a wooden floor. You're used to sleeping on the floor as your girlfriend tends "
          "\nto hog the entire bed most nights, but you don't recognise the room at all but at the same time, it seems"
          "\n oddly familiar. "
          "\nYou stand up and look around, all you can see in the darkness is an entrance to a spiral staircase and "
          "\nan old armoire in the corner. Are you going up, down, or do you examine the armoire?")
    time.sleep(1)
    print("""
    A. Upstairs
    B. Downstairs
    C. Open the armoire""")
    choice = input("Which option do you choose? ")
    if choice in choiceA:
        option_top(upstairs)
    elif choice in choiceB:
        option_down()
    elif choice in choiceC:
        option_arm(key, upstairs)
    elif choice in empty:
        print("Please enter a response")
        intro()
    else:
        print("Invalid response")
        intro()


def option_arm(key, upstairs):

    if key == 1:
        option_unlock_arm()

    else:
        print("There's a strange rattling sound coming from inside of the armoire. Curious, you try and open the doors "
              "\n but it seems like the doors are locked shut. Staircase it is then, where are you going? ")
    time.sleep(1)
    print("""
    A. Upstairs
    B. Downstairs""")

    choice = input("Which option do you choose? ")
    if choice in choiceA:
        if upstairs == 0:
            option_top(upstairs)
        else:
            print("You've already fully explored that area. Please choose a different route.")
            option_start()
    elif choice in choiceB:
        option_down()
    else:
        print("Invalid response, please try again")
        option_arm(key, upstairs)


def option_unlock_arm():
    print("Your little ornamental key seems to be the perfect size to fit in the lock.The rattling sound grows"
          "\n stronger, as if whatever is inside was able to sense your presence.")
    time.sleep(1)
    choice = input("Would you like to unlock the armoire?(Y/N)")
    if choice in yes:
        print("You put the key in and unlock the doors. A ghoul jumps out and attacks you. You try and fight back"
              "but you're unarmed and it soon overpowers you. The last thing you see as you're bleeding out on the "
              "cold wooden floor is an inscription on the ceiling above. It reads: Game over ")
        quit()

    elif choice in no:
        print("You step away from the armoire, and the rattling sounds grow weaker. Maybe it's best to not"
              "\n open this right now. You're unarmed and not ready for a fight. ")
    else:
        print("Invalid response, please try again. ")
        option_unlock_arm()


def option_top(upstairs):
    if upstairs == 0:
        print(
            "You're slowly making your way up the spiral staircase but you're soon "
            "\nmet with an impenetrable wall of rubble from the collapsed floor above you. "
            "\nYou gaze upon the night sky through the hole in the ceiling, pondering where you "
            "\nare as you don't recognise any of the constellations. " 
            "\nAs you look back down, you see glimpse of light in the corner of your eye, a moon-lit reflection "            
            "\nof something shiny attached to what seems to be a thin rod or a stick. "
            "\nThe light is too dim to tell without "
            "\ngetting a closer look. Will you: ")
        time.sleep(1)
        print("""
    A. Reach out and grab the shiny object
    B. Return to where you started
    C. Decide to go all the way down the stairs, since this route is clearly blocked""")
        choice = input()
        if choice in choiceA:
            option_chain()
        elif choice in choiceB:
            option_start()
        elif choice in choiceC:
            option_down()
        else:
            print("Invalid input, please try again")
            option_top(upstairs)

    else:
        print("You've already fully explored that area. Please choose a different route.")
        option_start()


def option_chain():
    print("You grab the shiny object and immediately realise it's a chain. You decide to pull it out to have a "
          "\ncloser look but the stick is in the way. You put all your strength into one last pull and the chain "
          "\nfinally breaks through what you thought was a stick, loosening some of the rubble in its wake."
          "\nThe chain glistens in the pale moonlight and attached to it is a small ornamental key"
          "\nA few stones and a human skull lands by your feet and suddenly you realise it was not a stick you broke"
          "\nwhen you were trying to pull the chain out. The skulls bears strange marks on its surface, as if someone"
          "\nor something had etched spiral patterns into it. There is a strange, captivating energy radiating from"
          "\nthe skull. What do you do next?"
          )
    global key
    key = 1
    global upstairs
    upstairs = 1
    time.sleep(1)
    option_skull()


def option_skull():
    print("""
    A. Run back to where you started
    B. Pick up the skull
    C. Do nothing""")
    choice = input()
    if choice in choiceA:
        option_start()
    elif choice in choiceB:
        print("You pick up the skull and you suddenly feel a burning sensation in your hands that quickly spreads"
              "\nto the rest of your body. You look at your arms and you see the pattern from the skull burning into"
              "\nyour flesh. You scream in agony as you're burning to a crisp. Maybe next time don't touch weird"
              "\nlooking human remains just for the fun of it.")
        quit()
    elif choice in choiceC:
        print("You decide to just stand there but soon you hear rumbling coming from the mound of rubble. Small stones"
              "\nare falling from the rubble, bouncing off the floor towards you. You should probably run before the"
              "\nwalls collapse.")
        choice = input("What do you do now? ")
        time.sleep(1)
        print("""
        A. Run 
        B. Keep standing there like a lemon.
        """)
        if choice in choiceA:
            print("You safely made it back!")
            option_start()
        else:
            print("A giant stone crushed you to death. Not sure what else you expected. ")
            quit()


def option_start():
    print("You're back where you started. All you can see in the darkness is an entrance to a spiral staircase and "
          "\nan old armoire in the corner. Are you going up, down, or do you examine the armoire? ")
    time.sleep(1)
    print("""
    A. Upstairs
    B. Downstairs
    C. Examine the armoire""")
    choice = input("Which option do you choose? ")
    if choice in choiceA:
        option_top(upstairs)
    elif choice in choiceB:
        option_down()
    elif choice in choiceC:
        option_arm(key, upstairs)
    else:
        print("Invalid response, please try again.")
        option_start()

def option_down():
