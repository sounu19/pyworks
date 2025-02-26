import random

def number_guessing_game():
    target_number = random.randint(1,100)
    attempts = 0
    max_attempts = 10

    print("______Welcome to Number Guessing Game!______")
    print("I am thinking of a number between 1 to 100")
    print(f"you have {max_attempts} attempts to guess the number/\n")


    while attempts<max_attempts:
        try:
            guess = int(input("Enter your Guess: "))
            attempts += 1

            if guess < target_number:
                print("Too Low\n")
            elif guess > target_number:
                print("Too High\n")
            else:
                print(f"Congratulations! You have guessed the number in {attempts} attempts")
                return

        except ValueError:
            print(f"Sorry for You! you have run out of attempts. the number was {target_number}.")






