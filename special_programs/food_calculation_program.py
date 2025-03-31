#food calucaltion programs

print("Fast Food Availibilty : ")
print("\n1. Burger\n2. Pizza\n3. Momos\n4. Samosa ")
total_bill = 0
while True:

    # choose the fast food
    choice = int(input("Choose your order  : "))
    if(choice == 0):
        break
    qty = int(input("Enter your quantity : "))

    if(choice == 1):
        price = 40
        print(f"Your burger quantity is {qty} and the price is {qty*price}")
    elif(choice == 2):
        price = 120
        print(f"Your Pizza Quantity is {qty} and Price is {qty*price}")
    elif(choice == 3):
        price = 20
        print(f"Your Momos Quantity is {qty} and Price is {qty*price}")
    elif(choice == 4):
        price = 10
        print(f"Your Samosa Quantity is {qty} and Price is {qty*price}")
    else:
        print("Invalid Choice")
        continue
    total_bill += qty*price
print(f"\n Your Total Bill : ₹{total_bill}")
print(f"Thank you for ordering! Enjoy Your Meal!")
