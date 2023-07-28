class Departments(object):
    def __init__ (self, name):
        self.name = name 
    def setName(self, name):
        self.name = name 
    def getName (self):
        return self.name
class Members(object):
    def __init__(self, fullname, address, placeOfWork):
        self.fullname = fullname 
        self.address = address
        self.placeOfWork = placeOfWork
    def setFullname(self, fullname):
        self.fullname = fullname 
    def getFullname(self):
        return self.fullname 
    def setAddress(self, address):
        self.address = address 
    def getAddress(self):
        return self.getaddress
    def setPlaceofWork(self, placeOfWork):
        self.placeOfWork = placeOfWork
    def getPlaceofwork (self, placeOfWork):
        return self.placeOfWork   
    

class OnBoarding(object):
    def __init__(self,departments):
        self.departments=departments

    def start(self):
        newuser=input("Are you a nem member of this church?(yes or no)")
        if newuser=="yes":
            self.showDepartments()
        else:
            print("This application is for only new users.")
            exit()

    def showDepartments(self):
        print("Please select a department from the below list:")
        i=1
        for department in self.departments:
            print("%s %s" % (i,department.getName()))
            i=i+1
        departmentinput=input("")
        dept=int(departmentinput)
        self.department=self.departments[dept-1]
        print("You selected %s " %(self.department.getName()))
        self.provideKYC()
    def provideKYC(self):
        self.fullname=input("Please enter your fullname:")
        self.placeofwork=input("Please enter your place of work:")
        self.address=input("Please enter your address:")
        self.generatePrintOut()

    def generatePrintOut(self):
        print("Thank you for joining our workforce")
        print("Your details are below:")
         
        print("Place of work: %s" %(self.placeofwork))
        print("Address: %s" %(self.address))
        print("Department to join: %s" % (self.department.getName()))
        print("Someone will contact you from %s department next week" %(self.department.getName()))


if __name__=="__main__":
    listOfDepartments=[]
    hushering = Departments("Hushers")
    choir =Departments("Choir")
    listOfDepartments.append(hushering) 
    listOfDepartments.append(choir)
    ob= OnBoarding(listOfDepartments)
    ob.start()



