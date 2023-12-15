# Write a program which will accept required values and find corresponding Area of type with match case Statment
s="""**************************************************
        Area Calculator
**************************************************
        R.Rectangle
        S.Square
        C.Circle
        T.Triangle
        E.Exit
**************************************************"""
print(s)
ip=input("Enter Your Choice: ")
match(ip):
    case 'R':
        l=int(input("Enter value of Length: "))
        b=int(input("Enter Value of Breadth: "))
        print("The Area of rectangle is {}".format(l*b))
    case 'S':
        a=int(input("Enter value of Side: "))
        print("The Area of Square is {}".format(a*a))
    case 'C':
        r=int(input("Enter Value of radius: "))
        print("The Area of Circle is {}".format(3.14*r*r))
    case 'T':
        b=int(input("Enter Value of base: "))
        h=int(input("Enter value of Height: "))
        print("The Area of triangle is {}".format(0.5*b*h))
    case 'E':
        print("Thankyou For using This Application")
    case _:
        print("Your Choice of selection is incorrect....Please try Again!!!!!")
print("Program Excecution Is Completed")

