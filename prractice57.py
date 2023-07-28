def isEven(x): 
    return x % 2 == 0 
def doFile(filename):
    with open(filename, 'w') as practice57:
        for i in range(100000): 
            if isEven(i):
                practice57.write(str(i) + '\n')
if __name__=="__main__":
    g = input("filename:")
    doFile(g)