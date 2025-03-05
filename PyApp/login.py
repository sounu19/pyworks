from utilities import app_config


def login():
    print("***Login Form***")
    while True:
        entered_username = input("Enter Your username: ")
        if entered_username != app_config.username:
            print("Username is Incorrect")
            continue
        entered_password = input("Enter Your Password: ")
        if entered_password != app_config.password:
            print("password is Incorrect")
            continue
        print(f"Login Successfully! Welcome {app_config.full_name}")
