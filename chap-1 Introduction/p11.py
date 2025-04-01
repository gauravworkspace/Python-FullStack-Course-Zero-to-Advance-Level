# Write a Python program to find the factorial of a given number.

number = int(input("Enter the number : "))

# Logic to find the factorial
fact = 1 

# Using for loop 
for i in range(1,number+1):
    fact = fact*i
# Display the result 
print("Factorial of ",number , "is " ,fact)