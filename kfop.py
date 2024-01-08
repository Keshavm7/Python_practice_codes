# Kelvin to Fahrenheit function

def kf():
    K=int(input("Enter kelvin value to convert it into Fahrenheit"))
    F = (K-273.15)*(9/5) + 32
    print("The Fahrenheit temperature value is:{}".format(F))