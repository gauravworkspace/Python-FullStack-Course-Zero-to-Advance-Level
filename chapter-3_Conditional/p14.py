# 21. Write a program to determine if a number is prime or composite using nested if-else.  

num = int(input("Enter Your Number : "))

if(num>1):
    is_prime = True #Assume  number is prime
    for i in range(2,int(num**0.5)+1):
        if num % i == 0:
            is_prime = False
            break

    # Use of Nested if-else
    if(is_prime):
        print(f"{num} is the prime nmber.")
    else:
        print(f"{num} is the composite number.")
elif num == 1:
    print(f"{num} is neither prime or composite number.")
else:
    print("Please enter a positive integer greater than 0 .")