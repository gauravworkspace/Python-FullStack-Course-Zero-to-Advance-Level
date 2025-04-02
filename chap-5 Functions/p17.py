# 18. **Write a function to find the common elements between two lists.**

def Find_Common(l1,l2):
    return list(set(l1) & set(l2))

l1 = [1,2,3,4,5,3,2]
l2=[5,6,7,8,2,3]
print(Find_Common(l1,l2))