def doReadFile(x):
    with open(x,"r") as openedfile:
        information=openedfile.read()
        print(information)
if __name__=="__main__":
    print("program read file")
    myfile=input("please enter name of file:")
    doReadFile(myfile)
    