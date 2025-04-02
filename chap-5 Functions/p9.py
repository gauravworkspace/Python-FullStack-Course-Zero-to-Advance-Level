# 9. **Write a function to count the occurrences of a character in a string.**

def Character_Occurence(string,char):
    string = string.lower()
    char = char.lower()

    return string.count(char)

# Test the function
 
string = "Gaurav"
char ="a"
print(Character_Occurence(string,char))