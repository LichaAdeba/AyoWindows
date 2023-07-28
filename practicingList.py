class Classes(object):
    def __init__ (self, name):
        self.name = name 
    def setName(self, name):
        self.name = name 
    def getName (self):
        return self.name
class classmate(object):
    def __init__(self, fullname, grade):
        self.fullname = fullname 
        self.grade = grade
    def setFullname(self, fullname):
        self.fullname = fullname 
    def getFullname(self):
        return self.fullname 
    def setGrade(self, grade):
        self.grade = grade 
    def getGrade(self):
        return self.getgrade
class OnBoarding(object):
    def __init__(self, classes):
        self.classes= classes
    def start(self):
        User=input("Hello")
        self.showClasses()
    def showClasses(self):
        print("PLease select one of the following classes:")
        i = 1 
        for classs in self.classes:
            print("%s, %s"%(i, classs.getName()))
            i = i+1
        classinput = input("")
        cl = int(classinput)
        self.classs= self.classes[cl - 1]
        print("you selected %s"%(self.classs.getName()))
        self.classroom()
    def classroom(self):
        self.fullname= input("enter fullname: ")
        self.grade = input("enter grade: ")
        self.printout()
    def printout(self):
        print("Here is full information")
        print("Fullname: %s " %(self.fullname))
        print("grade: %s" %(self.grade))
        print("class selected: %s" %(self.classs.getName()))

if __name__== "__main__":
    listofClasses= []
    maths = Classes("math")
    sciences = Classes("science")
    listofClasses.append(maths)
    listofClasses.append(sciences)
    ob= OnBoarding(listofClasses)
    ob.start()
