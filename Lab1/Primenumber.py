#Check wether given no is prime or not
# def Isprime(Value):
#     Check = 0
#     i = 0
#     for i in range(1, Value+1):
#         if Value % i == 0:
#             Check = Check+1
#     if Check == 2:
#         print("Number is Prime")
#     else:
#         print("number is not prime")
#
#
# Value = int(input("Enter a number to check? \n"))
# Isprime(Value)

#Print all prime numbers between anyrange
# def prime(lower, upper):
#     for number in range(lower, upper+1):
#         if number > 1:
#             for i in range(2, number):
#                 if (number % i) == 0:
#                     break
#             else:
#                 print(number)
#
# lower = int(input("Enter the lower value:"))
# upper = int(input("Enter the upper value:"))
#
# prime(lower, upper)

#Iterate list to check the existence of prime numbers

# myList = [7,8,9,4,3,13,17,22,23]
# l = len(myList)
# for i in range(0 , l):
#     c = 0
#     for j in range(2,myList[i]):
#         if myList[i]%j == 0:
#             c=1
#             break
#     if c == 0:
#         print(myList[i], " is prime number")
#     else:
#         print(myList[i], " is Not Prime")