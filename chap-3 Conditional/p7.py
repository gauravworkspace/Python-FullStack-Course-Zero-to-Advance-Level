# 13. Write a program to check if a number is a perfect square.  

number = int(input("Enter the number : "))

# Logic to check the perfect square
sqrt_value= (number** 0.5)

if(sqrt_value == int(sqrt_value)):
    print("Perfect Square")
else:
    print("Not Perfect Square")