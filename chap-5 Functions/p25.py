# 27. **Write a function to convert a number from decimal to binary.**

def Convertor(num):
    binary = ""
    while num>0:
        binary = str(num%2) + binary
        num =num//2
    return binary if binary else "0"

#example
print(Convertor(10))