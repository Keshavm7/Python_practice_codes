#if_elif_else_stmtex3.py
d={0:"ZERO",1:"ONE",2:"TWO",3:"THREE",4:"FOUR",5:"FIVE",6:"SIX",7:"SEVEN",8:"EIGHT",9:"NINE",-1:"-ONE",-2:"-TWO",-3:"-THREE",-4:"-FOUR",-5:"-FIVE",-6:"-SIX",-7:"-SEVEN",-8:"-EIGHT",-9:"-NINE"}
dig=int(input("Enter a Digit:")) # d= 0  1   2  3  4 5 6 7 8 9
res= d.get(dig)  if d.get(dig)!=None else "+Ve Number" if dig>0 else "-VE Number"
print("{} is {}".format(dig,res))