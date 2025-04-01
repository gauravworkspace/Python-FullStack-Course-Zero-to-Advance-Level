# 1. **Write a function to calculate the factorial of a number.**

def factorial(num):
    if num<0:
        print("Factorial is not defined for negative numbers.")
    elif num == 0 and num == 1:
        return 1
    else:
        fact = 1
        for i in range(2,num+1):
            fact*=i
        return fact 
        
num = int(input("Enter the number = "))
print(f"factorial of {num} is {factorial(num)}")
