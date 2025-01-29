print(r'''
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
Direction1 = input('You are on a crossword, where do you want to go? '
                   'Type "left" or "right".\n').lower()
if Direction1 == "left":
    Direction2 = input('you are in the lake way. How do you want to go?'
                       'Type "wait" or "swim".\n').lower()
    if Direction2 == "wait":
        Direction3 = input("You arrive at the island unharmed. "
                        "There is house with 3 doors. Type 'red' or "
                        "'yellow' or 'blue'. "
                        "Which colour do you choose?\n").lower()
        if Direction3 == "red":
            print("Burned by fire. Game Over.")
        elif Direction3 == "yellow":
            print("you won the game.")
        elif Direction3 == "blue":
            print("Eaten by beasts. Game Over.")
        else:
            print("your game is over.")

    else:
        print("Attacked by trout. Game Over.")
else:
    print("Fall into a hole. Game Over.")








