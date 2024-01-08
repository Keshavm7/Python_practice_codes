# program for implementing arithematic operation using match case statment and exceuting using modules concept
import addop_function as af,subop_function as sf,mulop_function as mf,FloorDivision_function as fd,mdivop_function as md,Exponentiationop_function as ep,divisionop_function as dv

print("*"*50)
print("\t\tArithematic Operations")
print("*"*50)
print("1.Addition")
print("2.Substraction")
print("3.Multiplication")
print("4.Division")
print("5.Floor Division")
print("6.Modulo Division")
print("7.Exponentiation")
print("*"*50)
ch=int(input("Enter your choice of operation: "))
match(ch):
    case 1:
        af.addop()
    case 2:
        sf.subop()
    case 3:
        mf.mulop()
    case 4:
        dv.divop()
    case 5:
        fd.fldivop()
    case 6:
        md.mdop()
    case 7:
        ep.expoop()
    case _:
        print("Your choice of selection is incorrect....please try again!!!!!")


