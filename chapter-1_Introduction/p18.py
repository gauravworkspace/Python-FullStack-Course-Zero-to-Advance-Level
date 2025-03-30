# Write a program to check whether a given number is a prime number.

number = 0

if(number>1):
    for i in range(2,int(number**0.5)+1):
        if(number%i == 0):
            print("The Given number is not Prime .")
            break
    else:
        print("The Given number is Prime .")
else:
    print("The Given number is not prime .")