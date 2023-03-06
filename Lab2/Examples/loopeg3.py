# Fixed a Letter from a to e and then ask the user to guess that letter until correct letter entered.
value = "c"
uservalue = input("guess number from a to e:   ")
while (uservalue != value):
    print("Incorrect")
    uservalue = input("guess number from a to e:   ")

print("Welcome, User")
