# 13. **Write a function to generate the Fibonacci sequence up to a specified number.**

# 0 1 1 2 3 5 8 13

def fibonacci_series(num):
    a,b = 0,1 
    print(a,end=" ")    
    print(b,end=" ")
    for _ in range(2,num):
        next_terms= a+b
        print(next_terms,end=" ")
        a,b = b, next_terms

num = int(input("Enter the number :"))
fibonacci_series(num)