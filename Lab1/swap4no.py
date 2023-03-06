def swap(a, b, c, d):
    i = 0
    j = 0
    j = a
    a = d
    d = j
    i = b
    b = c
    c = i
    return a, b, c, d


a = int(input("Enter 1st number a:\n"))
b = int(input("Enter 2nd number b:\n"))
c = int(input("Enter 3rd number c:\n"))
d = int(input("Enter 4th number d:\n"))
print(swap("d= "+str(a), "c= "+str(b), "b= "+str(c), "a="+str(d)))
