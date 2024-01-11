# python program which will implement ATM operations and Funds transaction with exceptional handling

from Exceptional_handling_ATM_Exceptclass import AmtError,InSuffFundError

Balance=50000
def deposit():
    damt=float(input("Enter an amount to deposit: "))
    if(damt<=0):
        raise AmtError
    else:
        global Balance
        Balance=Balance+damt
        print("*"*50)
        print("Dear customer your Account xxxxxxxx2557 is credited with an amount {}".format(damt))
        print("Balance in your Account xxxxxxxx2557 after deposit is {}".format(Balance))
        print("*"*50)

def withdraw():
    global Balance
    wamt=float(input("Enter an amount to Withdraw: "))
    if(wamt>Balance+500):
        raise InSuffFundError
    else:
        Balance=Balance-wamt
        print("*"*50)
        print("Dear Customer your Account xxxxxxxx2557 is debited with an amount {}".format(wamt))
        print("Balance in Your Account xxxxxxxx2557 after withdraw is {}".format(Balance))
        print("*"*50)

def balenq():
    print("*"*50)
    print("Dear Customer your Account xxxxxxxx2557 is having balance:{}".format(Balance))
    print("*"*50)
    