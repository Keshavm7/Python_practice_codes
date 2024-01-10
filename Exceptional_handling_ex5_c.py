# python program which will validate name of person or place or product 
# Data Validation: Write Your Name: Sameer -----> valid
#                  Write Your Name: Sameer12,$ameer ------>Invalid    

from Exceptional_handling_ex5_b import word
from Exceptional_handling_ex5_a import InapWordError
try:
    print("*"*50)
    w=input("Enter your name or Place name or product name: ")
    print("*"*50)
    word(w)
    
except InapWordError:
    print("Don't enter name/text includes Symbol,digit,alnum..try again!!!!!")
    
else:
    print("*"*50)
    print("The text You have entered is valid.....and it is {}".format(w))
    print("*"*50)
    
finally:
    print("The program execution is completed!!!!")
    
    