# 14. **Write a function to find the maximum number in a list.**

def Maximum(list):
    check1= min(list)
    check2= max(list)
    return check1, check2
ans=Maximum([1,2,3,4,5,6])

print(ans)