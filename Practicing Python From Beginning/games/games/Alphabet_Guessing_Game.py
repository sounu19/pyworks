import random
import string


def alphabet_guessing_game():
    target_alphabet = random.choice(string.ascii_lowercase)
    attempts = 0
    max_attempts = 6

    print("___Welcome to the Alphabet Guessing Game___")
    print(f"I am thinking of a letter from 'a' to 'z'. Can You Guess it in {max_attempts} attempts?")

    while attempts < max_attempts:
        guess = input("Enter Your Guess..!").lower()
        attempts += 1

        if len(guess) != 1 or guess not in string.ascii_lowercase:
            print("Please enter a valid single alphabet from 'a' to 'z'")
            continue
        if guess == target_alphabet:
            print(f"Congratulations! You have guessed the '{target_alphabet}' letter correctly in '{attempts}' attempts\n")
            return

        if guess < target_alphabet:
            print("Try a higher letter!")
        else:
            print("Try a lower Letter!")

        print(f"Attempts left : {max_attempts-attempts}")

    print(f"Sorry! You ran out of attempts! The correct letter was '{target_alphabet}'")