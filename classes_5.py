class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return f"Deposited ${amount}. New balance: ${self.balance}"
        else:
            return "Invalid deposit amount."

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            return f"Withdrew ${amount}. New balance: ${self.balance}"
        elif amount <= 0:
            return "Invalid withdrawal amount."
        else:
            return "Insufficient funds."

owner_name = input("Enter the account owner's name: ")
initial_balance = int(input("Enter the initial balance: "))
account = BankAccount(owner_name, initial_balance)

while True:
    print("\nOptions:")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. Exit")
    choice = input("Select an option (1/2/3/4): ")

    if choice == '1':
        amount = int(input("Enter the deposit amount: "))
        print(account.deposit(amount))
    elif choice == '2':
        amount = int(input("Enter the withdrawal amount: "))
        print(account.withdraw(amount))
    elif choice == '3':
        print(f"Account balance for {account.owner}: ${account.balance}")
    elif choice == '4':
        print("Exiting. Thank you!")
        break
    else:
        print("Invalid option. Please select a valid option.")
