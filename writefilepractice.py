def doFile(filename):
    with open(filename, "w") as myfile:
        for i in range(500):
            i=i+1
            myfile.write("hellotalk "+ str(i)+"\n")

if __name__=="__main__":
    print("You will be asked for a filename")
    print("it will print 1-499")
    g = input("please enter filename:")
    doFile(g)