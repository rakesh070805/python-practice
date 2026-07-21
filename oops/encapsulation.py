class Student:
    def __init__(self, name):
        self.name = name




class BankAccount:

    def __init__(self, name, acc_no, balance):
        self.name = name
        self.acc_no = acc_no
        self.__balance = balance      # Private variable

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print("Amount Deposited:", amount)
        else:
            print("Invalid amount")

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            print("Amount Withdrawn:", amount)
        else:
            print("Insufficient Balance")

    def check_balance(self):
        print("Current Balance:", self.__balance)

    def display(self):
        print("\n--- Account Details ---")
        print("Name:", self.name)
        print("Account Number:", self.acc_no)
        self.check_balance()


# Create Object
acc = BankAccount("Rakesh", 123456789, 10000)

# Display Details
acc.display()

# Deposit Money
acc.deposit(5000)
acc.check_balance()

# Withdraw Money
acc.withdraw(3000)
acc.check_balance()

# Try to access private variable
try:
    print(acc.__balance)
except AttributeError:
    print("Private variable cannot be accessed directly.")

# Final Details
acc.display()
