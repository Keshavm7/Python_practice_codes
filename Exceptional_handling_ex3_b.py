# python program which will calculate div of two numbers and develope programmer defined exception and 
# hit the exception in the case of invalid input data.
from Exceptional_handling_ex3_a import ZeroError

def divop(a,b):
    if(b==0):
        raise ZeroError
    else:
        return(a/b)
        
    

