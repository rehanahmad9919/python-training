class Account:
    def __init__(self, account_no, holder_name, pin, amount):
        self.__account_no = account_no
        self.__holder_name = holder_name
        self.__pin = pin
        self.__amount = amount
        self.__locked = False

    @property
    def pin(self):
        return self.__pin

    @property
    def locked(self):
        return self.__locked

    def lock_account(self):
        self.__locked = True

    def change_pin(self, old_pin, new_pin):
        if old_pin == self.__pin:
            self.__pin = new_pin
            print("\n✅ PIN changed successfully.")
        else:
            print("\n❌ Old PIN incorrect.")

    def show_balance(self):
        print(f"\n💰 Current Balance: ₹{self.__amount}")

    def deposit(self, amt):
        if amt > 0:
            self.__amount += amt
            print("\n✅ Deposit successful.")
        else:
            print("\n❌ Invalid amount.")

    def withdraw(self, amt):
        if amt <= 0:
            print("\n❌ Invalid amount.")
        elif amt <= self.__amount:
            self.__amount -= amt
            print("\n✅ Withdrawal successful.")
        else:
            print("\n❌ Insufficient balance.")

    def display(self):
        print("\n📄 --- Account Details ---")
        print("Account No   :", self.__account_no)
        print("Holder Name :", self.__holder_name)
        print("Balance     :", self.__amount)


# Dictionary to store accounts
accounts = {
    12345: Account(12345, "Amit Singh", 9919, 5000),
    12349: Account(12349, "Manoj Verma", 1973, 5000),
    12347: Account(12347, "Imran Ahmad", 8810, 5000)
}


while True:
    print("\n🏦 ===== BANK ATM SYSTEM ===== 🏦")

    try:
        acc_no = int(input("🔢 Enter Account Number: "))
    except ValueError:
        print("❌ Invalid input.")
        continue

    if acc_no not in accounts:
        print("❌ Account does not exist.")
        continue

    account = accounts[acc_no]

    if account.locked:
        print("🚫 This account is locked. Contact bank.")
        continue

    # PIN login (3 attempts)
    attempts = 3
    while attempts > 0:
        pin = int(input("🔐 Enter PIN: "))
        if pin == account.pin:
            print("\n✅ Login successful!")
            break
        else:
            attempts -= 1
            print(f"❌ Wrong PIN. Attempts left: {attempts}")

    if attempts == 0:
        account.lock_account()
        print("🚫 Account locked due to multiple wrong attempts.")
        continue

    # Account menu
    while True:
        print("\n📌 --- ACCOUNT MENU ---")
        print("1️⃣  View Balance")
        print("2️⃣  Deposit Money")
        print("3️⃣  Withdraw Money")
        print("4️⃣  Display Account Details")
        print("5️⃣  Change PIN")
        print("6️⃣  Logout")

        try:
            ch = int(input("👉 Enter choice: "))
        except ValueError:
            print("❌ Invalid input.")
            continue

        if ch == 1:
            account.show_balance()

        elif ch == 2:
            amt = int(input("💵 Enter amount to deposit: "))
            account.deposit(amt)

        elif ch == 3:
            amt = int(input("💸 Enter amount to withdraw: "))
            account.withdraw(amt)

        elif ch == 4:
            account.display()

        elif ch == 5:
            old_pin = int(input("🔐 Enter old PIN: "))
            new_pin = int(input("🆕 Enter new PIN: "))
            account.change_pin(old_pin, new_pin)

        elif ch == 6:
            print("\n👋 Logged out successfully.")
            break

        else:
            print("❌ Invalid option.")
