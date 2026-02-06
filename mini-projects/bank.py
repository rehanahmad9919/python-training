# Bank Management System - Mini Project
# File Handling in Python

def display_accounts():
    with open("bank.txt", "r") as file:
        print("\nAccount Details")
        print("------------------------------")
        print("AccNo  Name     Balance")

        for line in file:
            acc, name, bal = line.split()
            print(acc, " ", name, " ", bal)


def deposit():
    acc_no = input("Enter Account Number: ")
    amount = int(input("Enter deposit amount: "))

    accounts = []

    with open("bank.txt", "r") as file:
        for line in file:
            acc, name, bal = line.split()
            bal = int(bal)

            if acc == acc_no:
                bal += amount
                print("Deposit Successful!")

            accounts.append(f"{acc} {name} {bal}")

    with open("bank.txt", "w") as file:
        for record in accounts:
            file.write(record + "\n")


def withdraw():
    acc_no = input("Enter Account Number: ")
    amount = int(input("Enter withdrawal amount: "))

    accounts = []

    with open("bank.txt", "r") as file:
        for line in file:
            acc, name, bal = line.split()
            bal = int(bal)

            if acc == acc_no:
                if amount <= bal:
                    bal -= amount
                    print("Withdrawal Successful!")
                else:
                    print("Insufficient Balance!")

            accounts.append(f"{acc} {name} {bal}")

    with open("bank.txt", "w") as file:
        for record in accounts:
            file.write(record + "\n")


def check_balance():
    acc_no = input("Enter Account Number: ")

    with open("bank.txt", "r") as file:
        for line in file:
            acc, name, bal = line.split()

            if acc == acc_no:
                print("\nAccount Holder:", name)
                print("Balance:", bal)
                return

    print("Account not found!")


# -------- Main Menu --------
while True:
    print("\n----- Bank Menu -----")
    print("1. Display all accounts")
    print("2. Deposit money")
    print("3. Withdraw money")
    print("4. Check balance")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        display_accounts()
    elif choice == "2":
        deposit()
    elif choice == "3":
        withdraw()
    elif choice == "4":
        check_balance()
    elif choice == "5":
        print("Thank you for using the bank system!")
        break
    else:
        print("Invalid choice! Try again.")
