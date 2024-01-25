#Program for Copying the content of One File into Another File

filename=input("Enter any file name: ")
with open(filename,"r") as cp:
    cdata=cp.read()
    destfilename=input("Enter destination file name: ")
    with open(destfilename,"a") as wp:
        wp.write(cdata)
print("Data copied successfully!!!!")

        