# program for implementing temperature converter using match case statment with modules concept
from cel_kelvin import ck
from kfop import kf
from fkop import fk
from kcop import kc 
from fcop import fc 
from cfop import cf
import menu_temperature_converter as m 
import sys

ch=int(input("Enter your choice :"))
match(ch):
    case 1:
        ck()
    case 2:
        kf()
    case 3:
        fk()
    case 4:
        kc()
    case 5:
        fc()
    case 6:
        cf()
    case 7:
        print("Thanks for using this program")
        sys.exit()
    case _:
        print("Your choice of selection is incorrect......try again")
