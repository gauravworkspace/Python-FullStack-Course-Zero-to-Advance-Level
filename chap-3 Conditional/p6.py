# 12. Write a program to check if a number is a three-digit number.  

number = input("Enter Your numbe : ").strip() # Remove the extra spaces

#handlin negative numbers
if(number.startswith('-')):
    num = number[1:]
else:
    num =number
if(len(number)==3 and number.isdigit()):
    print("Three Digit Number")
else:
    print("No Three Digit number")