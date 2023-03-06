a = float(input("Please enter a number, I'll get its square root: "))
if a > 0:
    print("number is greater than 0,So I can calculate its square root")
    root = a**(1/2)
    print("Square root of ", a, "is", root)
else:
    print("Cannot calculate square root")
print("Thanks for input")
