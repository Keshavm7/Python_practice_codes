print("*"*50)
print("\tArithmatic Calculator")
print("*"*50)
print("\t1.Addition")
print("\t2.Substraction")
print("\t3.Multiplication")
print("\t4.Division")
print("\t5.Modulo Division")
print("\t6.Exponentiation")
print("\t7.Exit")
print("*"*50)
s=int(input("Enter Your Choice: "))
match(s):
    case 1:
        a=int(input("Enter first value: "))
        b=int(input("Enter Second Value: "))
        print("The Addition of {} and {} is {}".format(a,b,a+b))
    case 2:
        a=int(input("Enter first value: "))
        b=int(input("Enter Second Value: "))
        print("The Substraction of {} and {} is {}".format(a,b,a-b))
    case 3:
        a=int(input("Enter first value: "))
        b=int(input("Enter Second Value: "))
        print("The Multiplication of {} and {} is {}".format(a,b,a*b))
    case 4:
        a=int(input("Enter first value: "))
        b=int(input("Enter Second Value: "))
        print("The Division of {} and {} is {}".format(a,b,a/b))
    case 5:
        a=int(input("Enter first value: "))
        b=int(input("Enter Second Value: "))
        print("The Modulo Division of {} and {} is {}".format(a,b,a%b))
    case 6:
        a=int(input("Enter first value: "))
        b=int(input("Enter Second Value: "))
        print("The Exponentiation of {} and {} is {}".format(a,b,a**b))
    case 7:
        print("Thank you for using this Application")
    case _:
        print("Your choice of selection is incorrect...Please try again!!!!!")
print("Program Excecution is Completed")
