# check the number for even or odd

def check(num):
    if(num%2!=0):
        return "Odd"
    else:
        return "Even"

num =int(input("Enter the number : "))
if num<=0:
    print("Negative number entered")
else:
    print(check(num))