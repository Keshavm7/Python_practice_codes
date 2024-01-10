# python program which will generate multiplication table for a given number
# Data validations: If the no. is 'Zero' raise one exception (ZeroNumError)
#                   If the no. is 'Negative' raise Exception (NegNumError)
#                   If the number is alphanumeric or symbol or string then raise (ValueError)

from Exceptional_handling_ex4_a import ZeroNumError,NegNumError
from Exceptional_handling_ex4_b import Multable
try:
    print("*"*50)
    n=int(input("Enter a number of which you want to generate multiplication table:"))
    print("*"*50)
    
except ZeroNumError:
    print("Dont Enter Zero As input")
except NegNumError:
    print("Don't Enter negative Number")
except ValueError:
    Print("Don't enter Alnums,Alpha,Symbols")
    
else:
    print("*"*50)
    print("The Number You Have Entered is {}".format(n))
    print("*"*50)
    Multable(n)
    
finally:
    print("The program excecution is completed!!!!")
    