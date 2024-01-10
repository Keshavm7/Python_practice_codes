# python program which will generate multiplication table for a given number
# Data validations: If the no. is 'Zero' raise one exception (ZeroNumError)
#                   If the no. is 'Negative' raise Exception (NegNumError)
#                   If the number is alphanumeric or symbol or string then raise (ValueError)

class ZeroNumError(Exception):pass
class NegNumError(Exception):pass