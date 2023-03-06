# 1 PYTHON FILE OPEN
# Directory varies from Computer to Computer

# Open and read file
x = open("/Users/taha/Desktop/Artificial Intelligence/Lab3/Examples/demofile.txt")
print(x.read())

# 2 PYTHON FILE WRITE TO AN EXISTING FILE
# append and write into file
x = open("/Users/taha/Desktop/Artificial Intelligence/Lab3/Examples/demofile.txt", "a")
x.write("Taha has low confidence how he can improve it? ")
x.close()

# Now after closing open to check append
x = open("/Users/taha/Desktop/Artificial Intelligence/Lab3/Examples/demofile.txt")
print(x.read())


# Now rewrite over already written something
x = open("/Users/taha/Desktop/Artificial Intelligence/Lab3/Examples/demofile.txt", "w")
x.write("Software development is my field")
x.close()

# Opening
x = open("/Users/taha/Desktop/Artificial Intelligence/Lab3/Examples/demofile.txt")
print(x.read())

# 3 PYTHON FILE CREATE A NEW FILE
f = open("myfile.txt", "x")

# write to create a new file
f = open("myfile.txt", "w")
