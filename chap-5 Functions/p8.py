# 7. **Write a function to return the reverse of a string.**

def Reverse_String(string):
    reversed_string= string[::-1]
    return reversed_string

call_reverse_string = Reverse_String("Gaurav")
print(call_reverse_string)

# 8. **Write a function to check if a string is a palindrome.**

def is_Palindrome(string):
    original_string = string.lower()
    reversed_string= original_string[::-1]
    if(original_string == reversed_string):
        return "Palindrome"
        
    else:
        return "Not Palindrome"
        
print(is_Palindrome("ALAaa"))