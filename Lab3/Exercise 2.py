# TASK 1

no_of_cities = int(input("Enter number of cities you want to enter: "))

for i in range(0, no_of_cities):
    cityname = input("Enter city name: ")
    population = input("Enter population: ")
    mayor = input("Enter mayor name: ")
    f = open("Docfile.txt", "a")
    f.write("City: " + cityname + " " + "Population: " +
            population+" "+"mayor: " + mayor)

f.close()


f = open("Docfile.txt", "r")
print(f.read())


# TASK 2
# x = open("student.txt","x") to create a file
x = open("student.txt", "a")
x.write("Now We are AI students! ")
x.close()

x = open("student.txt")
print(x.read())
