# 17. Write a program to check if a given string is a palindrome.  

string = input("Enter Your String : ").lower
original_string = string
reversed_string =""
while(len(string)>0):
    reversed_string += string[-1]
    string= string[:-1]

# check if the original string and reversed string are the same

if original_string == reversed_string:
    print("Given string is palindrome")
else:
    print("Given String is not Palindrome")