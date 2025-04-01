# 14. Reverse a given number using a loop.  

number = int(input("Enter the number : "))

reversed_number = 0
for digit in range(1,len(str(number))+1):
     digit = number % 10 
     reversed_number = (reversed_number * 10) + digit
     number = number // 10 

print(reversed_number)