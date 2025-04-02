# 12. **Write a function to calculate the factorial of a number iteratively.**

def Factorial(num):
    if num == 0 or num == 1:
        return 1
    if num > 1:
        fact = 1
        for i in range(2,num+1):
            fact = fact*i
        return fact
    
print(Factorial(7))