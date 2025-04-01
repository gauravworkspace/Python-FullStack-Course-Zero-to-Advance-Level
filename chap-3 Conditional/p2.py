# 8. Write a program to check if a given number is divisible by both 5 and 11.  

num = 55

if(num % 5 == 0 and num% 11 == 0):
    print("The Given Number is divisible by both 5 and 11")
elif(num%5 == 0):
    print("The Given Number is divisble by 5 only!")
else:
    print("The Given Number is divisible by 11 only")