# Program for accepting Two Integer Value and perform Division
# Robust program

try:
    a=input("Enter value of a: ")
    b=input("Enter value of b: ")
    s1=int(a)
    s2=int(b)
    div=s1/s2
except ZeroDivisionError:
    print("Don't enter zero at denominator")
except ValueError:
    print("Don't enter alphanumbericals,alphabets,symbols")
else:
    print("The first value:{}".format(s1))
    print("The second value:{}".format(s2))
    print("Division({},{})={}".format(s1,s2,round(div,2)))
finally:
    print("The program excecution is completed!!!!!")
    
    
    

    
