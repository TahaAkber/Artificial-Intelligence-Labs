a = int(input("Enter a number: "))
if a == 0:
    a = 1
elif a == 1:
    a = 0
elif a > 2 or a < 0:
    print("You have entered number between:")
print(a)
