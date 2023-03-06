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
