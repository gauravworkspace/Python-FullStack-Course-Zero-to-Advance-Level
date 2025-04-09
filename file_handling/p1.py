# open file 
file =open('hello.txt','r')

# read fil e
# file = open('hello.txt','r')
# content = file.readlines()
# print(content)
# file.close()

# write mode
file= open('hello1.txt','w')
file.write("Namaste!, kaise ho?")
file.close()
# write mode override the data second time write

# Append mode
file = open('hello1.txt','a')
file.write("\n AChha hun")
file.close()
# ye override nhi krta 
