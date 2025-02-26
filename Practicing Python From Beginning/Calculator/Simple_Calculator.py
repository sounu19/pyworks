def add(x, y):
    return x + y
def subtract(x, y):
    return x - y
def multiply(x, y):
    return x * y
def divide(x, y):
    if y == 0:
        return "Error! Division by Zero"
    return x / y
def calculator():
    while True:
        print("\nSelect Operation:")
        print("1. Addition (+)")
        print("2. Subtraction (-)")
        print("3. Multiplication (*)")
        print("4. Division (/)")
        print("5. Exit")

        choice = input("Enter Your Choice")
        if choice == "5":
            print("Exiting! Good Bye!")
            break
        if choice in["1", "2", "3", "4"]:
            try:
                num1 = float (input("Enter First Number"))
                num2 = float(input("Enter Second Number"))
            except:
                ValueError
                print("Invalid Selection! Please select from 1,2,3,4")
                continue

        if choice == "1":
            print(f"Addition of {num1} + {num2} = {add(num1,num2)}")
        elif choice == "2":
            print(f"Subtraction of {num1} - {num2} = {subtract(num1,num2)}")
        elif choice == "3":
            print(f"Multiplication of {num1} * {num2} = {multiply(num1, num2)}")
        elif choice == "3":
            print(f"Division of {num1} / {num2} = {divide(num1, num2)}")
        else:
            print("Invalid Selection")
calculator()

