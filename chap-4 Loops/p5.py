# 13. Check whether a given number is prime or not.  

number = 37

if  number > 1:
    for i in range(2,int(number ** 0.5)+1):
        if(number%i== 0):
            print("Not Prime")
            break
    else:
        print("Prime")
else:
    print("Not Prime")