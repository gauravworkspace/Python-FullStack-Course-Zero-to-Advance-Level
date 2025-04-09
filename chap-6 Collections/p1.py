# Creating a List
# Accessing List Elements
# Adding Elements to List
# Updating Elements into List
# Removing Elements from the List
# Iterating Over Lists

# Creating a list
l1 = [1,2,3,"Hello",3.0,"Boy"]
print(l1)
# Accessing List elements
print(l1[0])
print(l1[1])

# adding elements in list
l1.append(3)
print(l1)

# updating elements into list
l1[2] = 53
print(l1)

# Removing elements 
l1.remove(2)
print(l1)

#iterating over list
for i in l1:
    print(i,end=" ")

# length
print("\n")
print(len(l1))
l1.append([2,3,4,5])
print(l1)

# sorting list and ascending
l2 = [1,3,4,5,6,3,2,5,8]
l2.sort()
print(l2)

# reversing a list 
l2.reverse()
print(l2)

# finding the largest and smallest 
print("Largest Number :",max(l2))
print("Smallest Number :",min(l2))