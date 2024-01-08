# Demonstarting nature of value 
n=input("Enter any type of value: ")
print("*"*50)
if(n.isalpha()):
    print("{} is Alphabet.".format(n))
if(n.isdigit()):
    print("{} is Numerical value".format(n))
if(n.isspace()):
    print("{} is space symbol.".format(n))
if(n.isalnum() and not n.isalpha() and not n.isdigit()):
    print("{} is Alphanumeric Value.".format(n))
if(not n.isalnum() and not n.isalpha() and not n.isdigit() and not n.isspace()):
    print("{} is Special Symbol.".format(n))
print("*"*50)