# Fahrenheit to Kelvin: 

def fk():
    F=int(input("Enter Fahrenheit value to convert it into Kelvin"))
    K = (F-32)*(5/9) + 273.15
    print("The kelvin temperature value is:{}".format(K))