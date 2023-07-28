def doFile(filename, lsname):
    with open(filename, "w") as myfile:
        for name in lsname:
            myfile.write("My name is " + str(name) + '\n')

if __name__ == "__main__":
    lsname = []
    while len(lsname)< 10:
        name= input("enter name: ")
        lsname.append(name)
    for name in lsname:
        print("My name is %s" %(name))
    doFile("myName", lsname)
