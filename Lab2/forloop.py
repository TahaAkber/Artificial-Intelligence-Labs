
# 1 a program that lists the countries in the set
clist = ["Canada", "USA", "Mexico", "Australia"]
for i in range(len(clist)):
    print(clist[i])

# 2 loop that counts from 0 to 100
number = 0
while number <= 100:
    print(number)
    number += 1

# 3 multiplication table using loop
number = int(input("Enter a number you want to find table of: "))
sum = 0
for i in range(1, 10+1):
    sum = i*number
    print(sum)

# 4 output from 10 to 1
i = 10
while i > 0:
    print(i)
    i -= 1

# 5 sum the numbers from 100 to 200

i = 100
range = 200
sum = 0
while i <= range:
    sum = i+sum
    print(sum)
    i = i+1
