def signup():
    global username, password, full_name
    print("**Sign up**")
    full_name = input("Enter Full Name: ")
    username = input("Enter Username: ")
    password = input("Enter Password: ")
    print("Signup successful! You can now log in.")

def signin():
    global username, password
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
def main():
    signup()
    signin()
main()