# EXERCISE 1

# 1 Make a program that takes inputs like height, width and depth from user and then calculate volume of the cube:
Height = int(input("Enter height of cube in cm^3: \n"))
Width = int(input("Enter Width of cube in cm^3: \n"))
depth = int(input("Enter depth of cube in cm^3: \n"))
volume = Height*Width*depth
if volume >= 1 and volume <= 10:
    print("Extra Small")
elif volume >= 11 and volume <= 25:
    print("Small")
elif volume >= 26 and volume <= 75:
    print("Medium")
elif volume >= 76 and volume <= 100:
    print("Large")
elif volume >= 101 and volume <= 250:
    print("Extra Large")
elif volume >= 256:
    print("Extra-Extra large")


# 2 worker efficiency is determined on the basis of the time
Efficiency = float(input("Enter time taken by worker in hours: \n"))
if Efficiency >= 2 and Efficiency <= 3:
    print("Highly Efficient")
elif Efficiency > 3 and Efficiency <= 4:
    print("Please! Improve speed")
elif Efficiency > 4 and Efficiency <= 5:
    print("You have been demoted to training program to improve speed")
elif Efficiency > 5:
    print("You have to leave the company")

# 3 password identify
password = input("Enter password: ")
if password == "ABC$123" or password == "abc$123":
    print("Welcome!")
else:
    print("Who are you?")
