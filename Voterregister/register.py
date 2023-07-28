class register(object):
    def __init__(self):
        self.firstname = ""
        self.lastname = ""
        self.number = ""
        self.email = ""
        self.address = ""
        self.city = ""
        self.state = ""
    def setfirstname(self, firstname):
        self.firstname = firstname 
    def getfirstname(self):
        return self.firstname
    def setlastname(self, lastname):
        self.lastname = lastname
    def getlastname(self):
        return self.lastname
    def setnumber(self, number):
        self.number = number
    def getnumber(self):
        return self.number
    def setemail(self, email):
        self. email = email
    def getemail(self):
        return self.email
    def setaddress(self, address):
        self.address = address
    def getaddress(self):
        return self.address
    def setcity(self, city):
        self.city = city 
    def getcity(self):
        return self.city
    def setstate(self, state):
        self.state = state 
    def getstate(self):
        return self.state
    def inputInfo(self):
        self.firstname = input("please enter firstname: ")
        self.lastname = input("please enter lastname:")
        self.number = input("please enter phonenumer:")
        self.address = input("please enter address: ")
        self.email = input("please enter email: ")
        self.city = input("please enter city of residence: ")
        self.state = input("please enter state of residence: ")
    def Totalsregister(self):
        input("please confirm information")
        full = print(str("%s, %s, %s, %s, %s, %s, %s \n") %(self.firstname, self.lastname, self.number, self.address, self.email, self.city, self.state))
        print(str(full g))
    def Total(self):
        with open("voterregister.csv", "a") as myfile:
            full = "%s, %s, %s, %s, %s, %s, %s \n" % (self.firstname, self.lastname, self.number, self.address, self.email, self.city, self.state)
            myfile.write(full)    

if __name__=="__main__":
    r = register()
    r.inputInfo()
    r.Totalsregister()
    r.Total()
    