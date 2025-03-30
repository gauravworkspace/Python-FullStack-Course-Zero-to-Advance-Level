# Write a Python program to find the ASCII value of a character entered by the user.

char = input("Enter the character to know ASCII Value : ")

if(len(char)==1):
    ascii_value= ord(char)
    print(f"ASCII Value of A is {ascii_value}")
else:
    print("Please Enter a Single Character !")
