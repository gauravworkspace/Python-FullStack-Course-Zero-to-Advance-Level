#  Write a program to check whether a given character is uppercase or lowercase.  
char = input("Enter Your character :")

if(char.islower()):
    print("Lowercase")
elif(char.isupper()):
    print("Uppercase")
else:
    print("Capitalize form")