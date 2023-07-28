def isEven(p):
    return p % 2 == 0 
def doFile(filename):
    with open(filename, "w") as hwfile:
        for i in range(500):
            i = i +1
            #hwfile.write("Number i:"+str(i)+" is even \n") if isEven(i) else hwfile.write("Number i:"+str(i)+" is odd \n")
            if isEven(i):
                hwfile.write("Number i:"+str(i)+" is even \n")
            else:
                hwfile.write("Number i:"+str(i)+" is odd \n")
if __name__=="__main__":
    g =input('filename:')
    doFile(g)
    