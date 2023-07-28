class register(object):
    def __init__(self, firstname, lastname, number, email, address, city, state):
        self.firstname = firstname 
        self.lastname = lastname
        self.number = number
        self. email = email
        self.address = address
        self.city = city 
        self.state = state 
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
def input(self):
    self.setfirstname = input("please enter firstname: ")
    self.setlastname = input("please enter lastname:")
    self.etnumber = input("please enter phonenumer:")
    self.setaddress = input("please enter address: ")
    self.setemail = input("please enter email: ")
    self.setcity = input("please enter city of residence: ")
    self.setstate = input("please enter state of residence: ")
    full = print(str("%s, %s, %s, %s, %s, %s, %s") %(self.getfirstname, self.getlastname, self.getnumber, self.getaddress, self.getemail, self.getcity, self.getstate))
    print(str(full))
            


if __name__=="__main__":
    vote 