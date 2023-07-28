class Project(object):
    def __init__(self, name1, name2, name3,name4,name5, name6,name7, name8, name9,name10 ):
        self.name1 = name1
        self.name2 = name2
        self.name3 = name3
        self.name4 = name4
        self.name5 = name5
        self.name6 = name6
        self.name7 = name7
        self.name8 = name8
        self.name9 = name9
        self.name10 = name10
    def setname1(self,name1):
        self.name1 = name1
    def getName1(self, name1):
        return self.name1
    def setname2(self,name2):
        self.name2 = name2
    def getName2(self, name2):
        return self.name2
    def setname3(self,name3):
        self.name3 = name3
    def getName3(self, name3):
        return self.name3
    def setname4(self,name4):
        self.name4 = name4
    def getName4(self, name4):
        return self.getname4
    def setname5(self,name5):
        self.name5 = name5
    def getName5(self, name5):
        return self.name5
    def setname6(self,name6):
        self.name6 = name6
    def getName6(self, name6):
        return self.name6
    def setname7(self,name7):
        self.name7 = name7
    def getName8(self, name8):
        return self.name8
    def setname9(self,name9):
        self.name9 = name9
    def getName9(self, name9):
        return self.name9
    def setname10(self,name10):
        self.name10 = name10
    def getName1(self, name10):
        return self.name10
    def start(self):
        self.showProject()
    def showName(self):
        self.name1= input("name1: ")
        self.name2= input("name2: ")
        self.name3= input("name3: ")
        self.name4= input("name4: ")
        self.name5= input("name5: ")
        self.name6= input("name6: ")
        self.name7= input("name7: ")
        self.name8= input("name8: ")
        self.name9= input("name9: ")
        self.name10= input("name10: ")

    def printName(self):
        print("%s" %(self.name1)),
        print("%s" %(self.name2)),
        print("%s" %(self.name3)),
        print("%s" %(self.name4)),
        print("%s" %(self.name5)),
        print("%s" %(self.name6)),
        print("%s" %(self.name7)),
        print("%s" %(self.name8)),
        print("%s" %(self.name9)),
        print("%s" %(self.name10))
def isEqual(self,x):
    return x == 10
def doFile(filename, self):
    
    with open(filename, "w") as myfile:
        for i in range(500):
            i=i+1
            if isEqual(i):
                exit()
            else:
                myfile.write(print(printName(self)) + str(i)+"\n")


if __name__=="__main__":
    showName(Project)
    printName(Project)
    g =input("enter file name: ")
    doFile(g, Project)


    
    
