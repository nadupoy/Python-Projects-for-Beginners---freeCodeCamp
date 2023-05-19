import random

options = ("rock", "paper", "scissors")
computer_choice = random.choice(options)

player_choice = input("Rock, Paper, Scissors? ")
player_choice = player_choice.lower()

if computer_choice == "rock":
    if player_choice == "rock":
        print("It's a tie. 👔")
    elif player_choice == "paper":
        print("Paper 📃  beats rock 🪨. Player wins!")
    elif player_choice == "scissors":
        print("Rock 🪨  beats scissors ✂️. Computer wins!")
elif computer_choice == "paper":
    if player_choice == "rock":
        print("Paper 📃  beats rock 🪨. Computer wins!")
    elif player_choice == "paper":
        print("It's a tie. 👔")
    elif player_choice == "scissors":
        print("Scissors ✂️  beats paper 📃. Player wins!")
elif computer_choice == "scissors":
    if player_choice == "rock":
        print("Rock 🪨  beats scissors ✂️. Player wins!")
    elif player_choice == "paper":
        print("Scissors ✂️  beats paper 📃. Computer wins!")
    elif player_choice == "scissors":
        print("It's a tie. 👔")