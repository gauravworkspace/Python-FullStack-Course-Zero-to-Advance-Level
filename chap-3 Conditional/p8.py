# 14. Write a program to check whether a given number is prime.  

number = 5

if(number > 1):
    for i in range(2,int(number**0.5)+1):
        if number % i == 0:
            print("Not the Prime number")
            break
    else:
        print("The number is prime")
else:
    print("The Number is not prime")