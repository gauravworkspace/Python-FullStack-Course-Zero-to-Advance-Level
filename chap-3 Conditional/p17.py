# 24. Write a program to simulate a simple ATM system (withdraw, balance check).  

balance =100000

while True:
    print("\n1. Check Balance\n2. Withdraw Money\n3. Exit")
    choice = int(input("Enter Choice : "))

    if choice == 1:
        print(f"Balance : ₹{balance}")
    elif choice == 2:
        amount = int(input("Enter withdrawal amount: ₹"))
        if(0<amount<=balance):
            balance-=amount
            print(f"Withdrawal sucessful ! Remaining balanace: ₹{balance}")
        else:
            print("Invalid or insufficient amount !")
    elif choice ==3:
        print(f"Thank you for using the ATM.")
        break
    else:
        print("Invalid Choice! Try again.")