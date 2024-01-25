#Program for Copying the content of One File into Another File


try:
    filename=input("Enter any file name: ")
    with open(filename,"rb") as sf:
        image=sf.read()
        destfile=input("Enter destination file name: ")
        with open(destfile,"ab") as df:
            df.write(image)
        print("Image copied successfully!!!!")
except FileExistsError:
    print("File already exist!!!")
except FileNotFoundError:
    print("File doesnot exist!!!")
        