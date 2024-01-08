import shares,time,importlib
def dispshares(s):
    print("*"*50)
    print("\t\tName\t\tPrice\t\t")
    print("*"*50)
    for n,p in s.items():
        print("\t\t{}\t\t{}\t\t".format(n,p))
    print("*"*50)

s=shares.sharesinfo()
dispshares(s)
time.sleep(10)
importlib.reload(shares)
s=shares.sharesinfo()
dispshares(s)
        