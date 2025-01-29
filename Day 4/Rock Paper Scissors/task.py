rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
game_images = ["Rock","Paper","Scissors"]
user_choice= int(input("What do you Choose? Type 0 for Rock or Type 1 for Paper or Type 2 for Scissors\n"))
if user_choice >=0 and user_choice <=2:
    print(game_images[user_choice])
import random
computer_choice = random.randint(0,2)
print("computer_choice is:")
print(game_images[computer_choice])

if user_choice >= 3 or user_choice < 0:
    print("You typed an invalid number. You lose!")
elif user_choice == 0 and computer_choice == 2:
    print("you win!")
elif user_choice == 2 and computer_choice == 0:
    print("You lose!")
elif user_choice > computer_choice:
    print("you win!")
elif computer_choice > user_choice:
    print("You lose!")
elif computer_choice == user_choice:
    print("You draw")