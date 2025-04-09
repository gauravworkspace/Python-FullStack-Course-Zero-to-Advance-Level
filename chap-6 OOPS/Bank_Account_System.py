# 1. Bank Account System
# Create classes for:

# BankAccount: Holds account number, balance.

# Methods: deposit(), withdraw(), check_balance()

class BankAccount:
    def __init__(self,account_number,acc_holder_name,balance=0):
        self.account_number = account_number
        self.acc_holder_name = acc_holder_name
        self.balance = balance

    def deposit(self,amount):
        if(amount>0):
            self.balance += amount
            print(f"{amount} ruppees deposit successfully.")
        else:
            print(f"Your amount is negative or invalid.")
    def withdraw(self,amount):
        if(amount<=self.balance and amount > 0):
            self.balance -= amount
            print(f"{amount} ruppees withdrawn successfully.")
        else:
            print(f"Insufficient amount or invalid value.")
    def checkbalance(self):
        print(f"{self.balance} ruppees is your balance amount.")

# check the functionality

print("Welcome to OOPS Banking System : ")

#Take input for create account

account_number = input("Enter Your Account Number : ")
acc_holder_name = input("Enter Your Account Holder Name : ")

# Create the object firstly
check = BankAccount(account_number,acc_holder_name)

while True:
        # Operation for deposit , withdrawn , checkbalance
    print(f"\n1 . Deposit\n2 . Withdrawn\n3 . Check Balance\n4 . Exit")
    try:
        choice = int(input("Enter Your Choice : "))
    except ValueError:
        print("Enter a valid number please")
        continue    
    if(choice == 1):
        try:
            amount = float(input("Enter Your Amount : "))
            check.deposit(amount)
        except ValueError:
            print("Enter a valid number please")
    elif (choice ==2):
        try:
            amount =float(input("Enter Your Amount : "))
            check.withdraw(amount)
        except ValueError:
            print("Enter a valid number please")
    elif (choice == 3):
        try: 
            check.checkbalance()
        except ValueError:
            print("Enter Your Balance")
    elif (choice== 4):
        try:  
            print(f"Logout Successfully.")
            break
        except ValueError:
            print("Enter a valid number")
    else:
        "Your Choice is invalid"


