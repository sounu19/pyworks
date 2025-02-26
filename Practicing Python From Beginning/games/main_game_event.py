from games import Number_Guessing_Game as ngg
from games import Alphabet_Guessing_Game as agg
from games import Rock_Paper_Scissors as rps
from random import choice

'''def main():
    while True:
        cont_var = input("Want to play a Number Guessing Game? Y/n: ")
        if cont_var == "Y" or cont_var == "y":
            number_guessing_game()
        elif cont_var == "n" or cont_var == "N":
            print("Game Over")
            break
        else:
            print("Invalid Selection, Try Again")

if "__main__" == main():
    main()'''

def main():
    while True:
        print("\nSelect a game to play:")
        print("1. Number Guessing Game")
        print("2. Alphabet Guessing Game")
        print("3. Rock, Paper, Scissors")
        print("4. Exit")
        choice = input("Enter Your Choice to start (1 / 2 / 3 / 4): ")

        if choice == "1":
            ngg.number_guessing_game()
        elif choice == "2":
            agg.alphabet_guessing_game()
        elif choice == "3":
            rps.rock_paper_scissors()
        elif choice == "4":
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid Selection, Please Try Again..!"3)
main()

