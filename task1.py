#Fellow
#Fellow Jitster says:a. create a python program that asks a person to enter 10 names and 
#prints out all the names on a new line after the 10th name 
#Fellow Jitster says:b. modify this program to write the names to a file and stops after the 10th name 

#a. create list of names
def doFile(Filename,names):
    with open(Filename, 'w') as myfile:
        for name in names:
            myfile.write("The names are  "+str(name)+ "\n")
if __name__=="__main__":
    names=[]
    while len(names)<10:
        name=input("Please enter a name:")
        names.append(name)
    #print("Number of names %s " %(len(names)))
    for name in names:
        print("The names are %s "%(name))

    doFile("mydemo.txt",names)

        
