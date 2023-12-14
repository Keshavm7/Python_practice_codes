# Write a python Program which will accept any digit(0-9) and write that digit in words
n=int(input("Enter any Digit between(0-9) or Negative no.: "))
if(n==0):
    print("{} is Zero".format(n))
else:
    if(n==1):
        print("{} is One".format(n))
    else:
        if(n==2):
            print("{} is Two".format(n))
        else:
            if(n==3):
                print("{} is Three".format(n))
            else:
                if(n==4):
                    print("{} is Four".format(n))
                else:
                    if(n==5):
                        print("{} is Five".format(n))
                    else:
                        if(n==6):
                            print("{} is Six".format(n))
                        else:
                            if(n==7):
                                print("{} is Seven".format(7))
                            else:
                                if(n==8):
                                    print("{} is Eight".format(n))
                                else:
                                    if(n==9):
                                        print("{} is Nine".format(n))
                                    else:
                                        print("{} is Negative Number".format(n))
                                        