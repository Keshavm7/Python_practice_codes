# python program which will implement ATM operations and Funds transaction with exceptional handling

from Exceptional_handling_ATM_menu import menu
from Exceptional_handling_ATM_Operations import deposit,withdraw,balenq
import sys
from Exceptional_handling_ATM_Exceptclass import AmtError,InSuffFundError

while(True):
    menu()
    ch=int(input("Enter Your choice of Operation: "))
    match(ch):
        case 1:
            try:
                deposit()
            except ValueError:
                print("Don't enter Alphanumeric Values,Alphabets,Symbols")
            except AmtError:
                print("Don't enter negative or Zero value")
        case 2:
            try:
                withdraw()
            except ValueError:
                print("Don't enter Alphanumeric Values,Alphabets,Symbols")
            except InSuffFundError:
                print("Dear Customer Your Account has Insufficient funds to Withdraw Amount...Please Check The Balance!!!")
        case 3:
            balenq()
        case 4:
            print("Thanx for using this ATM program!!!!")
            sys.exit()
        case _:
            print("Your Choice of Selection is Incorrect...Please try Again!!!!!")
    