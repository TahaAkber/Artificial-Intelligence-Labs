def celsiustofahrenheit(value):
    formula = 0
    formula = (9/5 * value) + 32.
    return formula


def fahrenheittocelsius(value1):
    formula = 0
    formula = (value1 - 32) * 5/9
    return formula


value = float(input("Enter a Degree in Celsius(°C)\n"))
print("Temperature in Fahrenheit is", celsiustofahrenheit(value), "°F")
print("      ")
value1 = float(input("Enter a Degree in Fahrenheit(°F)\n"))
print("Temperature in Celsius is", fahrenheittocelsius(value1), "°C")
