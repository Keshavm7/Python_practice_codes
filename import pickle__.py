import pickle
def  searchrecord():
    with open("emp_data","rb") as fp:
        print("--------------------------------------------------")
        records=[]
        while(True):
            try:
                record=pickle.load(fp)
                records.append(record)
            except EOFError:
                break
            
            
searchrecord()