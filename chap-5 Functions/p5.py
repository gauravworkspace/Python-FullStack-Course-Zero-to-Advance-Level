# 8. **Write a function to check if a string is a palindrome.**

def Palindrome(string):
    original_string = string
    reversed_string = string[::-1]
    if(original_string == reversed_string):
        print("Palindrome String")
        return
    else:
        print("Not Palindrome String")
    
Palindrome("LAL")