import random

user_choice = input("Choose and enter a choice (rock, paper, scissors): ")
available_actions = ["rock", "paper", "scissors"]
computer_choice = random.choice(available_actions)
print(f"\nYou chose {user_choice} and computer chose {computer_choice}.\n")

if user_choice == computer_choice:
    print(f"Both of them selected {user_choice}. It's a tie!")
elif user_choice == "rock":
    if computer_choice == "scissors":
        print("Rock smashes scissors! You win!")
    else:
        print(f"Paper covers rock! You lose.")
elif user_choice == "paper":
    if computer_choice == "rock":
        print("Paper covers rock! You win!")
    else:
        print("Scissors cuts paper! You lose.")
elif user_choice == "scissors":
    if computer_choice == "paper":
        print("Scissors cuts paper! You win!")
    else:
        print("Rock smashes scissors! You lose.")