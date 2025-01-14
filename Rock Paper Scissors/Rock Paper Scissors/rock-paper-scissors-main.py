import random

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

game_images = [rock, paper, scissors]

user_choice = int(input("Let's play! What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

if user_choice < 0 or user_choice > 2:
    print("You typed an invalid number. You lose.")
else:
    print(game_images[user_choice])

    computer_choice = random.randint(0, 2)
    print("Computer chose:" + game_images[computer_choice])

    if user_choice == 0 and computer_choice == 2:
        print("Rock smashes Scissors. You win!")
    elif user_choice == 1 and computer_choice == 0:
        print("Paper covers Rock. You win!")
    elif user_choice == 2 and computer_choice == 1:
        print("Scissors cut paper. You win!")
    elif user_choice == 2 and computer_choice == 0:
        print("Rock smashes Scissors. You lose :(")
    elif user_choice == 1 and computer_choice == 2:
        print("Scissors cut Paper. You lose :(")
    elif user_choice == 0 and computer_choice == 1:
        print("Paper covers Rock. You lose :(")
    else:
        print("Game is a draw.")
