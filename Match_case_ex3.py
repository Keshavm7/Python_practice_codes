# Write a program for Temperature conversion calculator using match case statment
print("*"*50)
print("\tTemperature Conversion Calculator")
print("*"*50)
print("\t1.Fahrenheit to Celsius")
print("\t2.Fahrenheit to Kelvin")
print("\t3.Celsius to Fahrenheit")
print("\t4.Celsius to Kelvin")
print("\t5.Kelvin to Celsius")
print("\t6.Kelvin to Fahrenheit")
print("\t7.Exit")
print("*"*50)
ip=int(input("Enter your choice: "))
match(ip):
    case 1:
        F=float(input("Enter value: "))
        c=(F-32)*(5/9)
        print("Temperature in C:{}".format(c))
    case 2:
        F=float(input("Enter value: "))
        K = (F-32)*(5/9) + 273.15
        print("Temperature in K:{}".format(K))
    case 3:
        C=float(input("Enter value: "))
        F = C*(9/5) + 32
        print("Temperature in F:{}".format(F))
    case 4:
        C=float(input("Enter value: "))
        K= C + 273.15
        print("Temperature in K:{}".format(K))
    case 5:
        K=float(input("Enter value: "))
        C = K - 273.15
        print("Temperature in C:{}".format(C))
    case 6:
        K=float(input("Enter Value: "))
        F=(K-273.15)*(9/5) + 32
        print("Temperature in F:{}".format(F))
    case 7:
        print("Thanks for using this Calculator")
    case _:
        print("Please Enter valid Input")
print("Program Excecution is completed")

        