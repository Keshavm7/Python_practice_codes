#Program for Reading employee Records from employee File
import pickle
def readrecord():
    with open("emp_data","rb") as rp:
        while(True):
            try:
                record=pickle.load(rp)
                for val in record:
                    print("{}\t".format(val),end=" ")
                    print()
            except EOFError:
                print("*"*50)
                break 
            
                
        
readrecord()