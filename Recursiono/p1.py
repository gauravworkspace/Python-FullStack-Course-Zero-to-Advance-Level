# print the number from 1 to 5
def show(n):
    if(n==0):
        return 
    print(n)
    show(n-1)
show(5)