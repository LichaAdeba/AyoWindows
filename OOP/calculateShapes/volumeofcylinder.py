class Cylinder(object):
    def __init__(self):
        self.pi =""
        self.height = ""
        self.radius = ""

    def setPi(self, pi):
        self.pi = pi 
    def getPi():
        return self.pi 

    def setHeight(self, height):
        self.height = height 
    def getHeight():
        return self.height 
        
    def set  Radius(self, radius):
        self.radius = radius 
    def getRadius():
        return self.radius 

    def Inputfunction(self):
        self.pi =input("Enter pi: ")
        self.height = input("Enter height: ")
        self.radius = input("Enter Radius: ")

    def calculatevol(self):
        calculateShape =(float(self.pi) *(float(self.radius)* float(self.radius)) * float(self.height))
        print("Volume of cylinder:" + str(calculateShape))


if __name__=='__main__':
    r = Cylinder()
    r.Inputfunction()
    r.calculatevol()