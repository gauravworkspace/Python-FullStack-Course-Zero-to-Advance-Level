# Write a Python program to check whether a number is even or odd.

num = int(input("Ente any positive integer : "))

if(num==0):
    print("0 is not odd and even number!")
elif(num%2==0):
    print("Given Number is Even!")
else:
    print("Given Number is Odd!")
