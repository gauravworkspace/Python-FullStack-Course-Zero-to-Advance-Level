# WAP to create a calculator 

def add(a,b):
     result= a+b
     return result
def subtract(a,b):
     result= a-b
     return result
def multiply(a,b):
     result = a*b
     return result
def divide(a,b):
     result = a/b
     return result

# take input from user

num1 = int(input("Enter the number1 : "))
num2 = int(input("Enter the number2 : "))
print("\n1. Sum\n2. Subtract\n3. Multiply\n4. Divide")
choice = int(input("Enter Your Operation "))

if(choice == 1):
    print("Addition ",add(num1,num2))
elif choice == 2:
    print("Substract ",subtract(num1,num2))
elif choice == 3:
    print("Multiply ",multiply(num1,num2))
elif choice == 2:
    print("Divide ",divide(num1,num2))
else:
    print("Invalid")

    

     

