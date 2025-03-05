from signup import signup
from login import login


def main():
    print("/n Welcome ")
    while True:
        choice_var = input("Do You Already Have an Account? Y/n: ")
        if choice_var == "Y" or choice_var == "y":
            login()
        elif choice_var == "N" or choice_var == "n":
            print("Please Signup First!")
            signup()
            login()
        else:
            print("Invalid Selection, Try Again")
            break
if __name__ == '__main__':
    main()