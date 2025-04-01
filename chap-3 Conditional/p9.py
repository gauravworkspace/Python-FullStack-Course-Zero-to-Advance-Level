# 16. Write a program to check if a given number is a palindrome.  

number = 123
reversed_number = 0
original_number =number
while number > 0:
    digit= number % 10 # extract the last digit
    reversed_number = (reversed_number * 10)+ digit
    number = number // 10  # remove the last digit
if(original_number == reversed_number ):
    print("Given number is Palindrome")
else:
    print("Given number is not Palindrome")