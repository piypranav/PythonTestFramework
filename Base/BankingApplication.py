import sys

class Customer:


    bankName = "DURGABANK"

    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance

    def withdraw(self, amount):
        if self.balance < amount:
            print("Not sufficient balance, cannot withdraw")
            sys.exit()

        self.balance = self.balance - amount
        print("New Amount is: ", self.balance)

    def deposit(self, amount):
        self.balance = self.balance + amount
        print("New Balance after deposit is: ", self.balance)

print("Welcome to Bank: " + Customer.bankName)
name=input("Enter your name: ")
c=Customer(name)
while True:
    print("Please Enter: \n1) w - Withdraw\n2) d - Deposit\n3) e - Exit")
    option=input("Please enter your choice: ")
    if option.lower() == 'w':
        amount = float(input("Enter amount to withdraw: "))
        c.withdraw(amount)
    elif option.lower() == 'd':
        amount = float(input("Enter amount to deposit: "))
        c.deposit(amount)
    elif option.lower() == 'e':
        print("Hey ", name, " your balance in our bank is: ", c.balance)
        sys.exit()
    else:
        print("Wrong input provided, please enter again")
