import pickle
def  readrecord():
    with open("emp_data","rb") as fp:
        print("--------------------------------------------------")
        while(True):
            try:
                record=pickle.load(fp)
                for val in record:  # record=[100, 'RS', 2.3, 'Author']
                    print("\t{}".format(val),end="  ")
                print()
            except EOFError:
                print("--------------------------------------------------")
                break
#main program
readrecord() # Function call