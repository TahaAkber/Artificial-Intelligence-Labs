# TASK 1
# print("For Square of numbers ")
mylist = [2, 3, 4, 5, 6, 7, 8, 9, 10]
# For Square of numbers in a list
for i in mylist:
    sum= lambda i:i*i
    print(sum(i))

print("        ")
print("For Cube of numbers ")

# For cube of numbers in a list
for i in mylist:
    cube = lambda i:i*i*i
    print(cube(i))

print("        ")

# TASK 2
starts_with = lambda x: True if x.startswith('S') else False
print(starts_with('Samsung'))
starts_with = lambda x: True if x.startswith('S') else False
print(starts_with('SonyXperia'))
starts_with = lambda x: True if x.startswith('S') else False
print(starts_with('Xperia'))

print("        ")

# TASK 3
# first we import datetime module, then we put date time and year into a using lambda variables then we print eachone
import datetime
now = datetime.datetime.now()
print(now)
year = lambda x: x.year
month = lambda x: x.month
day = lambda x: x.day
t = lambda x: x.time()
print(year(now))
print(month(now))
print(day(now))
print(t(now))
