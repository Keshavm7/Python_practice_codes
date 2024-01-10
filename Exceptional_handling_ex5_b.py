# python program which will validate name of person or place or product 
# Data Validation: Write Your Name: Sameer -----> valid
#                  Write Your Name: Sameer12,$ameer ------>Invalid    

from Exceptional_handling_ex5_a import InapWordError
def word(w):
    if(w.isdigit()==True) or (w.isspace()==True) or (not w.isalpha()==True):
        raise InapWordError