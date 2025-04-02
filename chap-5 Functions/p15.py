# 16. **Write a function to remove duplicates from a list.**

def Remove_duplicates(l):
    st= list(set(l))
    return st

l= [1,2,3,4,53,2,4,2]
print(Remove_duplicates(l))