import random

def rock_paper_scissors():
    print("Welcome to Rock, Paper, Scissors!")
    print("Rules: Rock beats Scissors, Scissors beats Paper, and Paper beats Rock.")

    choices = ["rock", "paper", "scissors"]

    while True:

        player_choice = input("Enter your choice (rock, paper, scissors) or 'quit' to exit: ").lower()


        if player_choice == "quit":
            print("Thanks for playing! Goodbye!")
            break


        if player_choice not in choices:
            print("Invalid choice. Please enter 'rock', 'paper', or 'scissors'.")
            continue


        computer_choice = random.choice(choices)
        print(f"Computer chose: {computer_choice}")


        if player_choice == computer_choice:
            print("It's a tie!")
        elif (player_choice == "rock" and computer_choice == "scissors") or \
             (player_choice == "scissors" and computer_choice == "paper") or \
             (player_choice == "paper" and computer_choice == "rock"):
            print("You win!")
        else:
            print("You lose!")