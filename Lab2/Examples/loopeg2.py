# counting positive and negative numbers
# number of positive and negative no
pcount = 0
ncount = 0
count = int(input("How many numbers you want: "))
i = 1
while i <= count:
    num = int(input("Enter number: "))
    if (num >= 0):
        pcount += 1
    else:
        ncount += 1
    i += 1
print("Positive ", pcount)
print("Negative ", ncount)
