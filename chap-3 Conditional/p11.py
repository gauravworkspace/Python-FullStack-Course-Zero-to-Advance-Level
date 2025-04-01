# 18. Write a program to determine if a given number is an Armstrong number.  

number = int(input("Enter the number : "))
num_of_digits = len(str(number))
sum_of_powers = 0

temp = number # store original number

while(temp > 0):
    digit = temp % 10 # extract the last digit
    sum_of_powers = sum_of_powers + digit**num_of_digits
    temp = temp // 10 # Remove the last digit


# Check Armstrong condition
if(number == sum_of_powers):
    print("The Given Number is an Armstrong")
else:
    print("The Given number is not Armstrong")
