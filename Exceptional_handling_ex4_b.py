# python program which will generate multiplication table for a given number
# Data validations: If the no. is 'Zero' raise one exception (ZeroNumError)
#                   If the no. is 'Negative' raise Exception (NegNumError)
#                   If the number is alphanumeric or symbol or string then raise (ValueError)

from Exceptional_handling_ex4_a import ZeroNumError,NegNumError
def Multable(n):
    if(n==0):
        raise ZeroNumError
    elif(n<0):
        raise NegNumError
    else:
        for i in range(1,11):
            print("{}*{}={}".format(n,i,n*i))
            