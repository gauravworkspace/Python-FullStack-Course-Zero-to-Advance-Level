# Write a program to find the largest among three numbers.

num1 = 140
num2 = 100
num3 = 100

# Logic to find the largest among three numbers
if(num1>num2 and num1 > num3):
    print(f"{num1} is the Largest number!")
elif(num2>num1 and num2>num3):
    print(f"{num2} is Largest number!")
else:
    print(f"{num3} is the Largest number!")