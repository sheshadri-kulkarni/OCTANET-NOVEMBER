import random
from datetime import datetime

class User:
    def __init__(self, user_id, pin):
        self.user_id = user_id
        self.pin = pin

class Account:
    def __init__(self, user, balance=0):
        self.user = user
        self.balance = balance
        self.transactions = []

    def deposit(self, amount):
        self.balance += amount
        self.transactions.append((datetime.now(), 'Deposit', amount))

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            self.transactions.append((datetime.now(), 'Withdrawal', amount))
        else:
            print("Insufficient funds!")

    def transfer(self, recipient, amount):
        if amount <= self.balance:
            self.balance -= amount
            recipient.balance += amount
            self.transactions.append((datetime.now(), 'Transfer to ' + recipient.user.user_id, amount))
        else:
            print("Insufficient funds!")

    def display_transactions(self):
        print("\nTransaction History:")
        for date, action, amount in self.transactions:
            print(f"{date} - {action}: {amount}")

class ATM:
    def __init__(self, users):
        self.users = users
        self.current_user = None

    def authenticate_user(self, user_id, pin):
        for user in self.users:
            if user.user_id == user_id and user.pin == pin:
                self.current_user = user
                return True
        return False

    def display_menu(self):
        print("\nATM Menu:")
        print("1. Transactions History")
        print("2. Withdraw")
        print("3. Deposit")
        print("4. Transfer")
        print("5. Quit")

    def run(self):
        print("Welcome to the ATM!")
        user_id = input("Enter User ID: ")
        pin = input("Enter PIN: ")

        if self.authenticate_user(user_id, pin):
            account = Account(self.current_user)
            while True:
                self.display_menu()
                choice = input("Enter choice (1-5): ")

                if choice == '1':
                    account.display_transactions()
                elif choice == '2':
                    amount = float(input("Enter withdrawal amount: "))
                    account.withdraw(amount)
                elif choice == '3':
                    amount = float(input("Enter deposit amount: "))
                    account.deposit(amount)
                elif choice == '4':
                    recipient_id = input("Enter recipient's User ID: ")
                    recipient = next((u for u in self.users if u.user_id == recipient_id), None)
                    if recipient:
                        amount = float(input("Enter transfer amount: "))
                        account.transfer(Account(recipient), amount)
                    else:
                        print("Recipient not found.")
                elif choice == '5':
                    print("Thank you for using the ATM. Goodbye!")
                    break
                else:
                    print("Invalid choice. Please try again.")

if __name__ == "__main__":
    # Sample user data
    users = [User("user1", "1234"), User("user2", "5678")]

    # Run the ATM application
    atm = ATM(users)
    atm.run()
