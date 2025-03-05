
from modules import config
def login():
    while True:
        entered_username = input("Enter Your username")
        if entered_username != username:
            print("Username is Incorrect")
            continue
        entered_password = input("Enter Your Password")
        if entered_password != password:
            print("password is Incorrect")
            continue
        print(f"Login Successfully! Welcome {full_name}")
        break
login()