# 24. **Write a function to find the length of a string without using the built-in `len()` function.**

def Length_string(string):
    count = 0
    for char in string:
        count+=1
        # print(char,end=" ")
    return count
print(Length_string("This is my program, and I am the programmer"))