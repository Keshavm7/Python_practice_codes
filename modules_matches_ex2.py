# program for implementing Area of different figures using match case statment with modules concept
from circle import circle as c
from rectangle import rect as r
from square import sqop as s
from triangle import trig as t
import sys

p="""=========================================
				Area of Different Figures
=========================================
				1. Circle
				2. Rectangle
				3. Square
				4. Triangle
				5. Exit
========================================="""


print(p)

ch=int(input("Enter your choice: "))
match(ch):
    case 1:
        c()
    case 2:
        r()
    case 3:
        s()
    case 4:
        t()
    case 5:
        print("Thanks for using this program")
        sys.exit()
    case _:
        print("Your choice of selection is incorrect....please try again!!!!")
        
        