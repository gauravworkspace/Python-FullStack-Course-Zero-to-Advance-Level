# Write a Python program to reverse a given number.

number = 123
reversed_number = 0 

while number>0:
    digit = number % 10 # extract the last digit
    reversed_number = reversed_number * 10 + digit # append the digit
    number = number // 10 # remove the last digit 
    
print("The Reversed of the Given number = ",reversed_number)




