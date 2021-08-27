#import random module 
import random

#create an input asking for the user to select rock, paper or scissors. 0 is for rock, 1 is for paper and 2 is for scissors
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, and 2 for Scissors. \n" ))

#create a variable for the computer to choose an option
computer_choice = random.randint(0,2)
print(f"Computer chose {computer_choice}")

#create an if statement to code the game
if user_choice >= 3 or user_choice < 0:
  print("You typed an invalid number, you lose.")
elif user_choice == 0 and computer_choice == 2:
  print("You win")
elif computer_choice == 0 and user_choice == 2:
  print("You lose")
elif computer_choice > user_choice:
  print("You lose")
elif computer_choice == user_choice:
  print("Draw")

