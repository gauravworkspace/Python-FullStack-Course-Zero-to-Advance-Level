# 5. Write a program to determine whether a character is a vowel or consonant.  

char = input("Enter any character : ")
vowels = "aeiouAEIOU"
# Logic to check the character is vowel or consonent
if(len(char) == 1 and char.isalpha()):
    if(char in vowels):
     print(f"{char} is vowel")
    else:
     print(f"{char} is consonant")
else:
  print("Please enter a single alphabet character!")