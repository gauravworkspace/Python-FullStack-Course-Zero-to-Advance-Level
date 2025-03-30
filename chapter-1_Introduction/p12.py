# Write a program to print the multiplication table of a given number.

number = 5

for i in range(1,11):
    temp = number * i
    # Print the table of given number 
    print(f"{number} x {i} = {temp}")