print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
q1 = input(print('You\'re at a cross road.\nYou see a paved walk at the left side that faces the sun, '
                 'and a bridge far away to the right.\n'
                 'Where do you want to go?\nType "left" to take the path facing the sun or "right" to take tha path that leads to the bridge.\n')).lower()
if q1 == "left":
    q2 = input(print('You walk for 300m and finally reaches a river bank. '
                     'A massive river flows in front of you leading to an island filled with thick vegetation.\n'
                     'You have an experience in diving into deep waters.\n'
                     'Do you wish to jump into the lake and start swimming or wait for a boat to come?\n'
                     'Type "swim" to swim across or "wait" to wait for a boat.\n')).lower()
    if q2 == "wait":
        q3 = input(print('You wait for 30 minutes and a boat finally appears.\n'
                         'You arrive at the island unharmed.\n'
                         'Walking through th dense forest, you finally come across a house with 3 doors - a red door, a blue door and a yellow door.\n'
                         'Which door would you choose to enter into?\n'
                         'Type "red" for opening the red door, "blue" for opening the blue door, "yellow" for opening the yellow door, or "neither" for exploring the rest of the island.\n')).lower()
        if q3 == "yellow":
            print("Yay! The treasure shines in front of you. You win.")
        elif q3 == "red":
            print("Oh No! The house burns down right as you enter inside.\nGame over.")
        elif q3 == "blue":
            print("Oh No! As you enter, 10 hungry goblins jumps in front of you.\n"
                  "There's no way to escape.\nGame over.")
        else:
            print("You ended up searching the whole island but did not find the treasure.\nA group of thugs attack you and steal your belongings.\nYou are too tired to move.\nGame over.")

    else:
        print("Oh no! A vicious crocodile appeared out of nowhere and attacked you.\nGame over.")
else:
    print ("Oh no! You fell into a hole before reaching the bridge.\nGame Over.")
