# 2. **Write a function to check if a number is prime.**

def isPrime(num):
    if num < 2:
        print("Please Enter Greater than 2 : ")
        return 
    
    for i in range(2,int(num**0.5)+1):
        if num % i == 0:
            print("Not Prime")
            return
    else:   
        print("Prime")
    

isPrime(2)
