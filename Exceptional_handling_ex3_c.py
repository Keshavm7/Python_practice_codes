# python program which will calculate div of two numbers and develope programmer defined exception and 
# hit the exception in the case of invalid input data.
from Exceptional_handling_ex3_a import ZeroError
from Exceptional_handling_ex3_b import divop
try:
    print("*"*50)
    a=int(input("Enter value of a: "))
    b=int(input("Enter value of b: "))
    print("*"*50)
    divop(a,b)
except ValueError:
    print("Dont enter alnums,alpha,symbols")
except ZeroError:
    print("Dont enter zero to denominator")

else:
    print("The first value:{}".format(a))
    print("The second value:{}".format(b))
    print("Division({},{}={})".format(a,b,divop(a,b)))
finally:
    print("Program excecution is completed!!!!")